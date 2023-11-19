from main_app import *

def set_theme(main_window):
        # set custom font for application
        font_id = QFontDatabase.addApplicationFont("../../common/assets/themes/Ubuntu-Medium.ttf")
        if font_id == -1:
            print("Failed to load font")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        main_window.setFont(QFont(font_family, 24))
        #set theme
        if app_settings.THEME == "light":
            str = open(main_window.light_themefile, 'r').read()
           
        else:
            str = open(main_window.dark_themefile, 'r').read()
        main_window.setStyleSheet(str)

        #top left logo icon
        pixmap = QPixmap("../../common/assets/images/analog.png")
        main_window.ui.topLeftLogoLabel.setPixmap(pixmap)
        main_window.ui.topLeftLogoLabel.setScaledContents(True)

        set_console_log_theme(main_window)
        set_adv_data_table_theme(main_window)

def set_theme_button_icon(main_window):
    icon = QIcon()
    icon.addPixmap(QPixmap("../../common/assets/images/icons/theme_mode.png"), QIcon.Normal, QIcon.On)
    # set button width and height
    main_window.ui.btn_theme.setFixedWidth(35)
    main_window.ui.btn_theme.setFixedHeight(35)
    main_window.ui.btn_theme.setIcon(icon)
    main_window.ui.btn_theme.setIconSize(QSize(30, 30))
    main_window.ui.btn_theme.setText("")
    #custome stylesheet
    main_window.ui.btn_theme.setStyleSheet('''
    QPushButton {background-color: transparent; border: none;}
    QPushButton:hover{
    color: rgb(255, 255, 255);
    background-color: #464E69;
    /* add padding */
    padding-left: 3px;
    padding-right: 3px;
    padding-top: 3px;
    padding-bottom: 3px;

    }''')

def set_menu_button_icon(main_window):
    icon = QIcon()
    icon.addPixmap(QPixmap("../../common/assets/images/icons/icon_settings.png"), QIcon.Normal, QIcon.On)
    # set button width and height
    main_window.ui.btn_menu.setFixedWidth(35)
    main_window.ui.btn_menu.setFixedHeight(35)
    main_window.ui.btn_menu.setIcon(icon)
    main_window.ui.btn_menu.setIconSize(QSize(30, 30))
    main_window.ui.btn_menu.setText("")
    #custome stylesheet
    main_window.ui.btn_menu.setStyleSheet('''
    QPushButton {background-color: transparent; border: none;}
    QPushButton:hover{
    color: rgb(255, 255, 255);
    background-color: #464E69;
    /* add padding */
    padding-left: 3px;
    padding-right: 3px;
    padding-top: 3px;
    padding-bottom: 3px;

    }''')

def set_console_log_theme(main_window):
    #set transparent background
    # fore color to light gray
    main_window.ui.console.setStyleSheet('''
    QTextEdit {background-color: transparent; border: none;}
    QTextEdit {color: rgb(222, 221, 218);}''')

def set_adv_data_table_theme(main_window):
    #set transparent background
    # fore color to light gray
    if app_settings.THEME == "light":
        main_window.ui.table_adv_data.setStyleSheet('''
        QTextEdit {background-color: transparent; border: none;}
        QTextEdit {color: rgb(0, 0, 0);}''')
    else:
        main_window.ui.table_adv_data.setStyleSheet('''
        QTextEdit {background-color: transparent; border: none;}
        QTextEdit {color: rgb(222, 221, 218);}''') 