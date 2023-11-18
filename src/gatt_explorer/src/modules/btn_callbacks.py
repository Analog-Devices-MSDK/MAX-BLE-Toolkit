from main_app import *

def btn_callback(main_window):
    print("Button 1 clicked")
    main_window.ui.pushButton.setText("Button 1 clicked")
    #change themes
    main_window.set_theme(main_window.dark_themefile, True)

def btn_callback_2(main_window):
    print("Button 2 clicked")
    main_window.ui.pushButton_2.setText("Button 2 clicked")
    #change themes
    main_window.set_theme(main_window.light_themefile, True)

def register_button_callbacks(main_window):
    pass
    # try:
    #     main_window.ui.pushButton.clicked.connect(lambda: btn_callback(main_window))
    #     main_window.ui.pushButton_2.clicked.connect(lambda: btn_callback_2(main_window))
    # except Exception as e:
    #     print(e)
    