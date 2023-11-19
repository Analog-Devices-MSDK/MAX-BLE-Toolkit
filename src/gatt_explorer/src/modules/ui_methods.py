from main_app import *

def set_theme(main_window):
        # set custom font for application
        font_id = QFontDatabase.addApplicationFont("../../common/assets/themes/Ubuntu-Medium.ttf")
        font_family =  None
        if font_id == -1:
            print("Failed to load font")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        if font_family:
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
        # remove horizontal header from table_adv_data
        main_window.ui.table_adv_data.horizontalHeader().setVisible(False)
    

        

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

#************| Animation stuff |-------------------
def toggleRightBox(main_window):
        # GET WIDTH
        width = main_window.ui.frame_main_right.width()
        widthLeftBox = main_window.ui.frame_main_left.width()
        maxExtend = app_settings.RIGHT_BOX_WIDTH
       # color = Settings.BTN_RIGHT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
       # style = main_window.ui.settingsTopBtn.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
          #  main_window.ui.settingsTopBtn.setStyleSheet(style + color)
            # if widthLeftBox != 0:
            #     style = main_window.ui.toggleLeftBox.styleSheet()
            #     main_window.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
          #  main_window.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

        start_box_animation(main_window, widthLeftBox, width, "right")

def start_box_animation(main_window, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # # ANIMATION LEFT BOX        
        main_window.left_box = QPropertyAnimation(main_window.ui.frame_main_left, b"minimumWidth")
        main_window.left_box.setDuration(app_settings.TIME_ANIMATION)
        main_window.left_box.setStartValue(left_box_width)
        main_window.left_box.setEndValue(left_width)
        main_window.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        main_window.right_box = QPropertyAnimation(main_window.ui.frame_main_right, b"minimumWidth")
        main_window.right_box.setDuration(app_settings.TIME_ANIMATION)
        main_window.right_box.setStartValue(right_box_width)
        main_window.right_box.setEndValue(right_width)
        main_window.right_box.setEasingCurve(QEasingCurve.InOutQuart)
        print("right box width: ", right_box_width)
        print("right width: ", right_width)
        print(app_settings.TIME_ANIMATION)
        print(app_settings.RIGHT_BOX_WIDTH)



        # GROUP ANIMATION
        main_window.group = QParallelAnimationGroup()
        main_window.group.addAnimation(main_window.left_box)
        main_window.group.addAnimation(main_window.right_box)
        main_window.group.start()