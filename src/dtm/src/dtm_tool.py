"""
Main Application for DTM Testsing
"""


import sys
import time

import ble_hci
from ble_hci import utils as hci_utils
from ble_hci.data_params import DataPktStats
# pylint: disable=no-name-in-module,c-extension-no-member
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# pylint: enable=no-name-in-module,c-extension-no-member

import ble_util

from ui_mainwindow import Ui_MainWindow

TAB_TX = 0
TAB_RX = 1


class RxStatsThread(QThread):
    """RX Stats worker thread"""

    early_exit = False
    data_ready = Signal(list)

    def __init__(self, hci: ble_hci.BleHci = None, update_rate = 1):
        super().__init__()
        self.hci = hci
        self.update_rate = update_rate 

    def run(self):
        """Run worker thread"""
        self.early_exit = False

        while not self.early_exit:
            stats, code  = self.hci.get_test_stats()
        
            self.data_ready.emit([stats, code])
            time.sleep(self.update_rate)

    def stop(self):
        """Stop worker thread"""
        self.early_exit = True

    def quit(self):
        """Quit worker thread"""
        self.early_exit = True


class MainWindow(QMainWindow):
    """
    App Main Window
    """
    RX_DEFAULT_UPDATE_RATE=1

    def __init__(self):
        super().__init__()
        self.rx_is_init = False
        self.win = Ui_MainWindow()
        self.win.setupUi(self)

        self.win.tab_mode.setCurrentIndex(TAB_TX)

        self.refresh_port_select()
        self.win.baud_rate_select_tx.setValue(hci_utils.DEFAULT_BAUDRATE)
        self.refresh_port_select(is_tx=False)
        self.win.baud_rate_select_rx.setValue(hci_utils.DEFAULT_BAUDRATE)

        self.win.phy_select_tx.insertItems(0, ble_util.AVAILABLE_PHYS)
        self.win.phy_select_rx.insertItems(0, ble_util.AVAILABLE_PHYS)

        self.win.packet_type_select_tx.insertItems(0, ble_util.TX_PACKET_TYPE_OPTIONS)
        self.win.power_select_tx.insertItems(0, ble_util.AVAILABLE_TX_POWERS)
        self.win.power_select_tx.setCurrentIndex(len(ble_util.AVAILABLE_TX_POWERS) - 1)

        self.win.channel_select_tx.valueChanged.connect(self.slider_value_changed)
        self.win.channel_select_rx.valueChanged.connect(self.slider_value_changed)

        self.win.packet_len_select_tx.valueChanged.connect(self.slider_value_changed)
        self.win.start_stop_btn_tx.clicked.connect(self.tx_dtm_btn_click)
        self.win.start_stop_btn_rx.clicked.connect(self.rx_dtm_btn_click)

        self._set_rx_update_rate_label(self.RX_DEFAULT_UPDATE_RATE)
        self.win.update_rate_slider.valueChanged.connect(self._refresh_rx_update_rate)

        self.win.reset_hci.clicked.connect(self._reset_hci)
        self.set_channel_label(0, TAB_TX)
        self.set_channel_label(0, TAB_RX)
        self.set_packet_len_label(0)

        self.tx_test_started = False
        self.rx_test_started = False

        self.rx_stats_thread = RxStatsThread()
        self.rx_stats_thread.data_ready.connect(self._update_rx_stats)
    def _refresh_rx_update_rate(self):
        actual_rate: float = self.win.update_rate_slider.value() / 10
        self.rx_stats_thread.update_rate = actual_rate
        self._set_rx_update_rate_label(actual_rate)
    


    def _set_rx_update_rate_label(self, update_rate):
        self.win.update_rate_label.setText(f'Update Rate (s) - {update_rate : .1f}')


    def _update_rx_stats(self, data):

        stats: DataPktStats
        stats, _ = data

        self.win.rx_ok_label.setText(f'RX OK - {stats.rx_data}')
        self.win.rx_crc_label.setText(f'RX CRC - {stats.rx_data_crc}')
        self.win.rx_timeout_label.setText(f'RX Timeout - {stats.rx_data_timeout}')
        self.win.rx_per_label.setText(f"PER  - {stats.per() * 100 : .2f}")

    def refresh_port_select(self, is_tx=True):
        """
        Refreshes available ports in port selector
        """
        ports = hci_utils.get_serial_ports()

        if is_tx:
            self.win.port_select_tx.clear()
            self.win.port_select_tx.insertItems(0, ports)
        else:
            self.win.port_select_rx.clear()
            self.win.port_select_rx.insertItems(0, ports)

    def set_channel_label(self, channel, tab=TAB_TX):
        """
        Sets the label to show the channel
        """
        if tab == TAB_TX:
            self.win.channel_label_tx.setText(f"Channel {channel}")
        else:
            self.win.channel_label_rx.setText(f"Channel {channel}")

    def set_packet_len_label(self, packet_len):
        """
        Sets the label to show the packet length
        """
        self.win.packet_len_label_tx.setText(f"Packet Length {packet_len}")

    def slider_value_changed(self):
        """
        Updates Labels whenever slider values are moved
        """
        tab = TAB_TX
        if self._state_tab_is_tx():
            channel = self.win.channel_select_tx.value()
        else:
            channel = self.win.channel_select_rx.value()
            tab = TAB_RX

        self.set_channel_label(channel, tab)
        self.set_packet_len_label(self.win.packet_len_select_tx.value())

    def _get_selected_port(self, tab=TAB_TX):
        if tab == TAB_TX:
            return self.win.port_select_tx.currentText()

        return self.win.port_select_rx.currentText()

    def _state_tab_is_tx(self):
        return self.win.tab_mode.currentIndex() == 0

    def _reset_hci(self):
        if self._state_tab_is_tx():
            port = self.win.port_select_tx.currentText()
            baud_rate = self.win.baud_rate_select_tx.value()
        else:
            if self.rx_stats_thread.isRunning():
                self.rx_stats_thread.hci.reset()
                return

            port = self.win.port_select_rx.currentText()
            baud_rate = self.win.baud_rate_select_rx.value()

        hci = ble_hci.BleHci(port_id=port, baud=baud_rate)
        
        try:
            hci.reset()
        except TimeoutError:
            self.show_basic_msg_box('Timeout occured resetting device')
    
    def rx_dtm_btn_click(self):
        """
        Starts or Stops DTM test
        """

        port = self.win.port_select_rx.currentText()
        baud_rate = self.win.baud_rate_select_rx.value()
        if self.tx_test_started and port == self._get_selected_port(TAB_TX):
            self.show_basic_msg_box("Cannot use the same port for both TX and RX")
            return

        hci = ble_hci.BleHci(port_id=port, baud=baud_rate)
        self.rx_stats_thread.hci = hci

        try:
            hci.reset()
        except TimeoutError:
            self.show_basic_msg_box("Timeout occured: Failed to reset devices!")

        if not self.rx_test_started:
            channel = int(self.win.channel_select_rx.value())
            phy = ble_util.TX_PHY_TYPES[self.win.phy_select_tx.currentText()]

            try:
                hci.rx_test(channel=channel, phy=phy)

                self.win.port_select_rx.setEnabled(False)
                self.win.baud_rate_select_rx.setEnabled(False)
                
                self.win.start_stop_btn_rx.setText("STOP RX")
                self.rx_stats_thread.start()
                self.rx_test_started = True
            except TimeoutError:
                self.show_basic_msg_box("Failed to start test")

        else:
            self.win.port_select_rx.setEnabled(True)
            self.win.baud_rate_select_rx.setEnabled(True)

            self.win.start_stop_btn_rx.setText("START RX")
            self.rx_stats_thread.stop()
            self.rx_test_started = False
            try:
                hci.end_test()
            except TimeoutError:
                self.show_basic_msg_box("Failed to end test!")

    def tx_dtm_btn_click(self):
        """
        Starts or Stops DTM test
        """
        
        port = self.win.port_select_tx.currentText()
        baud_rate = self.win.baud_rate_select_tx.value()

        if self.rx_test_started and port == self._get_selected_port(TAB_RX):
            self.show_basic_msg_box("Cannot use the same port for both TX and RX")
            return

        hci = ble_hci.BleHci(port_id=port, baud=baud_rate)

        try:
            hci.reset()
        except TimeoutError:
            self.show_basic_msg_box("Failed to reset devices!")

        if not self.tx_test_started:
            tx_power = int(self.win.power_select_tx.currentText().split("dbm")[0])
            channel = int(self.win.channel_select_tx.value())
            payload = ble_util.TX_PACKET_TYPES[
                self.win.packet_type_select_tx.currentText()
            ]
            phy = ble_util.TX_PHY_TYPES[self.win.phy_select_tx.currentText()]
            packet_len = self.win.packet_len_select_tx.value()

            try:
                hci.set_adv_tx_power(tx_power)
                hci.tx_test(
                    channel=channel, phy=phy, payload=payload, packet_len=packet_len
                )
                
                self.win.port_select_tx.setEnabled(False)
                self.win.baud_rate_select_tx.setEnabled(False)
                
                self.win.start_stop_btn_tx.setText("STOP")
                self.tx_test_started = True
            except TimeoutError:
                self.show_basic_msg_box("Failed to start test")

        else:
            self.win.port_select_tx.setEnabled(True)
            self.win.baud_rate_select_tx.setEnabled(True)
            
            self.tx_test_started = False
            self.win.start_stop_btn_tx.setText("START")
            try:
                hci.end_test()
            except TimeoutError:
                self.show_basic_msg_box("Failed to end test!")

    def show_basic_msg_box(self, msg):
        """
        Display a basic message box with a given message
        """
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec()

    def disable_tx_inputs(
        self,
    ):
        """
        Disable all inputs used for DTM testing
        to prevent alterations before stopping the test
        """
        self.win.port_select_tx.setEnabled(False)
        self.win.baud_rate_select_tx.setEnabled(False)


    def enable_inputs(self):
        """
        Enable all DTM inputs
        """
        self.win.port_select_tx.setEnabled(True)
        self.win.baud_rate_select_tx.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
