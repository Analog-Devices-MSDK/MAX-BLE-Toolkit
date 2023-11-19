import sys
from pathlib import Path
from modules import *
# Adding the 'src' directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent / "src"))

import sys
class MainWindow(QMainWindow):
    light_themefile = "../assets/themes/light_theme.qss"
    dark_themefile = "../assets/themes/dark_theme.qss"
    ble_scanner = None
    logger = None
    def __init__(self):
        # instantiate the QMainWindow
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ui_methods.set_theme(self)
        self.show()
        #register button callbacks
        btn_callbacks.register_button_callbacks(self)

        # Theme stuff
        ui_methods.set_theme_button_icon(self)
        ui_methods.set_menu_button_icon(self)
        ui_methods.set_console_log_theme(self)

        #config logging
        console_log.init_logging(self)
        self.logger = logging.getLogger("gattLogger")
        self.logger.info("Application started")

        #BLE scanner
        self.ble_scanner = ble.BleScanner(self)
        
        # Slots
        slots.init_signals_and_slots(self)
        
    def logToTextbox(self, data):
        self.ui.console.append(data)
    def closeEvent(self, event):
        self.stop_scanner()

    def stop_scanner(self):
        self.ui.btn_scan.setText("Scan")
        self.ble_scanner.is_scanning = False
        self.ble_scanner.quit()
        self.ble_scanner.wait()
        #self.stop_graphing()

if __name__ == "__main__":
    light_themefile = "../assets/themes/light_theme.qss"
    str = open(light_themefile, 'r').read()
    app = QApplication(sys.argv)
    app.setStyleSheet(str)
    window = MainWindow()
    sys.exit(app.exec())
