import sys
from pathlib import Path
from modules import *
# Adding the 'src' directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent / "src"))
# Now you can use absolute imports
from modules import *

import sys
class MainWindow(QMainWindow):
    def __init__(self):
        # instantiate the QMainWindow
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_theme()

        self.show()
        #register button callbacks
        btn_callbacks.register_button_callbacks(self)

        # connect signals and slots

        # other stuff

    def set_theme(self):
        # set custom font for application
        font_id = QFontDatabase.addApplicationFont("../../common/assets/themes/Ubuntu-Medium.ttf")
        if font_id == -1:
            print("Failed to load font")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.setFont(QFont(font_family, 24))
        #set theme
        light_themefile = "../local_assets/themes/light_theme.qss"
        dark_themefile = "../local_assets/themes/dark_theme.qss"
        if app_settings.THEME == "light":
            str = open(light_themefile, 'r').read()
        else:
            str = open(dark_themefile, 'r').read()
        self.setStyleSheet(str)

        #top left logo icon
        pixmap = QPixmap("../../common/assets/images/analog.png")
        self.ui.topLeftLogoLabel.setPixmap(pixmap)
        self.ui.topLeftLogoLabel.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
