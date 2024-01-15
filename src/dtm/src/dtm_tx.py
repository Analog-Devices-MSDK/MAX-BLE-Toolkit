"""
Main Application for DTM Testsing
"""

import sys

import ble_hci
from ble_hci.constants import PhyOption, PayloadOption
from ble_hci.packet_codes import StatusCode
import BLE_util
import hci_util
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

TX_PACKET_TYPES = {
    "PRBS9": 0,
    "11110000": 1,
    "10101010": 2,
    "PRBS15": 3,
    "11111111": 4,
    "00000000": 5,
    "00001111": 6,
    "01010101": 7,
}

TX_PHY_TYPES = {"1M": 1, "2M": 2, "S8": 3, "S2": 4}


class MainWindow(QMainWindow):
    """
    App Main Window
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.win = Ui_MainWindow()
        self.win.setupUi(self)

        self.refresh_port_select()
        self.win.baud_rate_select.setValue(hci_util.DEFAULT_BAUDRATE)

        self.win.phy_select.insertItems(0, BLE_util.AVAILABLE_PHYS)
        self.win.packet_type_select.insertItems(0, BLE_util.TX_PACKET_TYPE_OPTIONS)
        self.win.power_select.insertItems(0, BLE_util.AVAILABLE_TX_POWERS)
        self.win.power_select.setCurrentIndex(len(BLE_util.AVAILABLE_TX_POWERS) - 1)

        self.win.channel_select.valueChanged.connect(self.slider_value_changed)
        self.win.packet_len_select.valueChanged.connect(self.slider_value_changed)
        self.win.start_stop_btn.clicked.connect(self.dtm_btn_click)

        self.set_channel_label(0)
        self.set_packet_len_label(0)

        self.dtm_test_started = False

    def refresh_port_select(self):
        """
        Refreshes available ports in port selector
        """
        self.win.port_select.clear()
        self.win.port_select.insertItems(0, hci_util.serial_ports())

    def set_channel_label(self, channel):
        """
        Sets the label to show the channel
        """
        self.win.channel_label.setText(f"Channel {channel}")

    def set_packet_len_label(self, packet_len):
        """
        Sets the label to show the packet length
        """
        self.win.packet_len_label.setText(f"Packet Length {packet_len}")

    def slider_value_changed(self):
        """
        Updates Labels whenever slider values are moved
        """
        self.set_channel_label(self.win.channel_select.value())
        self.set_packet_len_label(self.win.packet_len_select.value())

    def dtm_btn_click(self):
        """
        Starts or Stops DTM test
        """
        port = self.win.port_select.currentText()
        baud_rate = self.win.baud_rate_select.value()

        hci = ble_hci.BleHci(port_id=port, baud=baud_rate)

        try:
            hci.reset()
        except:
            self.show_basic_msg_box(f"Failed to reset devices!")

        if not self.dtm_test_started:
            tx_power = int(self.win.power_select.currentText().split("dbm")[0])
            channel = int(self.win.channel_select.value())
            payload = TX_PACKET_TYPES[self.win.packet_type_select.currentText()]
            phy = TX_PHY_TYPES[self.win.phy_select.currentText()]
            packet_len = self.win.packet_len_select.value()

            try:
                hci.set_adv_tx_power(tx_power)
                hci.tx_test(
                    channel=channel, phy=phy, payload=payload, packet_len=packet_len
                )
                self.disable_inputs()
                self.win.start_stop_btn.setText("STOP")
                self.dtm_test_started = True
            except:
                self.show_basic_msg_box("Failed to start test")

        else:
            self.enable_inputs()
            self.dtm_test_started = False
            self.win.start_stop_btn.setText("START")
            try:
                hci.end_test()
            except:
                self.show_basic_msg_box("Failed to end test!")

    def show_basic_msg_box(self, msg):
        """
        Display a basic message box with a given message
        """
        msg_box = QMessageBox()
        msg_box.setText(msg)
        msg_box.exec()

    def disable_inputs(self):
        """
        Disable all inputs used for DTM testing
        to prevent alterations before stopping the test
        """
        self.win.input_frame.setDisabled(True)

    def enable_inputs(self):
        """
        Enable all DTM inputs
        """
        self.win.input_frame.setDisabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
