"""
Main Application for DTM Testsing
"""


import sys
import time

import max_ble_hci
from max_ble_hci import utils as hci_utils
from max_ble_hci.data_params import DataPktStats

# pylint: disable=no-name-in-module,c-extension-no-member
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QLabel,
    QSlider,
    QComboBox,
    QSpinBox,
    QPushButton
)

# pylint: enable=no-name-in-module,c-extension-no-member

import ble_util

from ui_mainwindow import Ui_MainWindow

TAB_TX = 0
TAB_RX = 1


class RxStatsThread(QThread):
    """RX Stats worker thread"""

    early_exit = False
    data_ready = Signal(list)

    def __init__(self, hci: max_ble_hci.BleHci = None, update_rate=1):
        super().__init__()
        self.hci = hci
        self.update_rate = update_rate

    def run(self):
        """Run worker thread"""
        self.early_exit = False

        while not self.early_exit:
            stats, code = self.hci.get_test_stats()

            self.data_ready.emit([stats, code])
            time.sleep(self.update_rate)

    def stop(self):
        """Stop worker thread"""
        self.early_exit = True

    def quit(self):
        """Quit worker thread"""
        self.early_exit = True


class CommonInputGroup:
    """Internal grouping of common inputs"""

    # pylint: disable=too-many-arguments
    def __init__(
        self, port_select, baud_rate_select, channel_label, channel_select, phy_select
    ) -> None:
        self.port_select: QComboBox = port_select
        self.baud_rate_select: QSpinBox = baud_rate_select
        self.channel_label: QLabel = channel_label
        self.channel_select: QSlider = channel_select
        self.phy_select: QComboBox = phy_select
        

    def set_channel_label(self, channel: int):
        """Set channel label

        Parameters
        ----------
        channel : int
            channel to set label to
        """
        assert (
            self.channel_select.minimum() <= channel <= self.channel_select.maximum()
        ), f"Channel out of range {channel}"

        self.channel_label.setText(f"Channel {channel}")

    def refresh_port_select(self):
        """Refresh serial ports"""
        ports = hci_utils.get_serial_ports()
        self.port_select.clear()
        self.port_select.insertItems(0, ports)

    def selected_port(self) -> str:
        """Get Current selected

        Returns
        -------
        str
            Serial port string
        """
        return self.port_select.currentText()

    def selected_baud(self) -> int:
        """Get current selected baud rate

        Returns
        -------
        int
            Baudrate
        """
        return self.baud_rate_select.value()
    
    def set_baud(self, baud: int):
        """Set baud rate 

        Parameters
        ----------
        baud : int
            Baudrate
        """
        self.baud_rate_select.setValue(baud)

    def selected_phy(self) -> str:
        """Get Current Select PHY

        Returns
        -------
        str
            PHY
        """
        return self.phy_select.currentText()

    def selected_channel(self) -> int:
        """Get current selected channel

        Returns
        -------
        int
            Channel
        """
        return self.channel_select.value()

    def enable_serial_inputs(self, enable=True):
        """Enable/Disable serial inputs

        Parameters
        ----------
        enable : bool, optional
            Enable or disable, by default True
        """
        self.port_select.setEnabled(enable)
        self.baud_rate_select.setEnabled(enable)
    


    

class MainWindow(QMainWindow):
    """
    App Main Window
    """

    RX_DEFAULT_UPDATE_RATE = 1

    def __init__(self):
        super().__init__()
        self.rx_is_init = False
        self.win = Ui_MainWindow()
        self.win.setupUi(self)

        self.common = [
            CommonInputGroup(
                port_select=self.win.port_select_tx,
                baud_rate_select=self.win.baud_rate_select_tx,
                channel_label=self.win.channel_label_tx,
                channel_select=self.win.channel_select_tx,
                phy_select=self.win.phy_select_tx,
                
            ),
            CommonInputGroup(
                port_select=self.win.port_select_rx,
                baud_rate_select=self.win.baud_rate_select_rx,
                channel_label=self.win.channel_label_rx,
                channel_select=self.win.channel_select_rx,
                phy_select=self.win.phy_select_rx,
                
            ),
        ]

        self.win.tab_mode.setCurrentIndex(TAB_TX)

        self.common[TAB_TX].refresh_port_select()
        self.common[TAB_RX].refresh_port_select()
        self.common[TAB_TX].set_baud(hci_utils.DEFAULT_BAUDRATE)
        self.common[TAB_RX].set_baud(hci_utils.DEFAULT_BAUDRATE)

        self.common[TAB_TX].phy_select.insertItems(0, ble_util.AVAILABLE_PHYS)
        self.common[TAB_RX].phy_select.insertItems(0, ble_util.AVAILABLE_PHYS)

        self.common[TAB_TX].channel_select.valueChanged.connect(self.slider_value_changed)
        self.common[TAB_RX].channel_select.valueChanged.connect(self.slider_value_changed)
        
        
        self.win.packet_type_select_tx.insertItems(0, ble_util.TX_PACKET_TYPE_OPTIONS)
        self.win.power_select_tx.insertItems(0, ble_util.AVAILABLE_TX_POWERS)
        self.win.power_select_tx.setCurrentIndex(len(ble_util.AVAILABLE_TX_POWERS) - 1)


        self.win.packet_len_select_tx.valueChanged.connect(self.slider_value_changed)
        
        self.win.start_stop_btn_tx.clicked.connect(self.tx_dtm_btn_click)
        self.win.start_stop_btn_rx.clicked.connect(self.rx_dtm_btn_click)

        self._set_rx_update_rate_label(self.RX_DEFAULT_UPDATE_RATE)
        self.win.update_rate_slider.valueChanged.connect(self._refresh_rx_update_rate)

        self.win.reset_hci.clicked.connect(self._reset_hci)
        self.common[TAB_TX].set_channel_label(0)
        self.common[TAB_RX].set_channel_label(0)

        self._set_packet_len_label(0)

        self.tx_test_started = False
        self.rx_test_started = False

        self.rx_stats_thread = RxStatsThread()
        self.rx_stats_thread.data_ready.connect(self._update_rx_stats)

    def _refresh_rx_update_rate(self):
        actual_rate: float = self.win.update_rate_slider.value() / 10
        self.rx_stats_thread.update_rate = actual_rate
        self._set_rx_update_rate_label(actual_rate)

    def _set_rx_update_rate_label(self, update_rate):
        self.win.update_rate_label.setText(f"Update Rate (s) - {update_rate : .1f}")

    def _update_rx_stats(self, data):
        stats: DataPktStats
        stats, _ = data

        self.win.rx_ok_label.setText(f"RX OK - {stats.rx_data}")
        self.win.rx_crc_label.setText(f"RX CRC - {stats.rx_data_crc}")
        self.win.rx_timeout_label.setText(f"RX Timeout - {stats.rx_data_timeout}")
        self.win.rx_per_label.setText(f"PER  - {stats.per() : .2f}")

    def _set_packet_len_label(self, packet_len):
        """
        Sets the label to show the packet length
        """
        self.win.packet_len_label_tx.setText(f"Packet Length {packet_len}")

    def slider_value_changed(self):
        """
        Updates Labels whenever slider values are moved
        """
        tab = self.win.tab_mode.currentIndex()
        self.common[tab].set_channel_label(self.common[tab].channel_select.value())

        if tab == TAB_TX:
            self._set_packet_len_label(self.win.packet_len_select_tx.value())

    def _reset_hci(self):
        tab = self.win.tab_mode.currentIndex()

        if tab == TAB_RX and self.rx_stats_thread.isRunning():
            self.rx_stats_thread.hci.reset()
            return

        port = self.common[tab].port_select.currentText()
        baud_rate = self.common[tab].baud_rate_select.value()

        hci = max_ble_hci.BleHci(port_id=port, baud=baud_rate)

        try:
            hci.reset()
        except TimeoutError:
            self._show_basic_msg_box("Timeout occured resetting device")

    def rx_dtm_btn_click(self):
        """
        Starts or Stops DTM test
        """

        port = self.common[TAB_RX].selected_port()
        baud_rate = self.common[TAB_RX].selected_baud()

        if self.tx_test_started and port == self.common[TAB_TX].selected_port():
            self._show_basic_msg_box("Cannot use the same port for both TX and RX")
            return

        hci = max_ble_hci.BleHci(port_id=port, baud=baud_rate)
        self.rx_stats_thread.hci = hci

        try:
            hci.reset()
            hci.reset_test_stats()
        except TimeoutError:
            self._show_basic_msg_box("Timeout occured: Failed to reset devices!")

        if not self.rx_test_started:
            channel = int(self.common[TAB_RX].selected_channel())
            phy = ble_util.TX_PHY_TYPES[self.common[TAB_RX].selected_phy()]

            try:
                hci.rx_test(channel=channel, phy=phy)

                self.common[TAB_RX].enable_serial_inputs(False)

                self.win.start_stop_btn_rx.setText("STOP RX")
                self.rx_stats_thread.start()
                self.rx_test_started = True
            except TimeoutError:
                self._show_basic_msg_box("Failed to start test")

        else:
            self.common[TAB_RX].enable_serial_inputs()
            self.win.start_stop_btn_rx.setText("START RX")
            self.rx_stats_thread.stop()
            self.rx_test_started = False
            try:
                hci.end_test()
                hci.reset_test_stats()
            except TimeoutError:
                self._show_basic_msg_box("Failed to end test!")

    def tx_dtm_btn_click(self):
        """
        Starts or Stops DTM test
        """

        port = self.common[TAB_TX].selected_port()
        baud_rate = self.common[TAB_TX].selected_baud()

        if self.rx_test_started and port == self.common[TAB_RX].selected_port():
            self._show_basic_msg_box("Cannot use the same port for both TX and RX")
            return

        hci = max_ble_hci.BleHci(port_id=port, baud=baud_rate)

        try:
            hci.reset()
        except TimeoutError:
            self._show_basic_msg_box("Failed to reset devices!")

        if not self.tx_test_started:
            tx_power = int(self.win.power_select_tx.currentText().split("dbm")[0])
            channel = int(self.common[TAB_TX].selected_channel())
            payload = ble_util.TX_PACKET_TYPES[
                self.win.packet_type_select_tx.currentText()
            ]
            phy = ble_util.TX_PHY_TYPES[self.common[TAB_TX].selected_phy()]
            packet_len = self.win.packet_len_select_tx.value()

            try:
                hci.set_adv_tx_power(tx_power)
                hci.tx_test(
                    channel=channel, phy=phy, payload=payload, packet_len=packet_len
                )

                self.common[TAB_TX].enable_serial_inputs(False)

                self.win.start_stop_btn_tx.setText("STOP")
                self.tx_test_started = True
            except TimeoutError:
                self._show_basic_msg_box("Failed to start test")

        else:
            self.common[TAB_TX].enable_serial_inputs()

            self.tx_test_started = False
            self.win.start_stop_btn_tx.setText("START")
            try:
                hci.end_test()
            except TimeoutError:
                self._show_basic_msg_box("Failed to end test!")

    def _show_basic_msg_box(self, msg):
        """
        Display a basic message box with a given message
        """
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
