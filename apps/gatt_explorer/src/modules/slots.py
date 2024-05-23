from main_app import *
import  logging
#*********************| BLE scanner slots | *********************
def update_discovered_devices(main_window, device):
    device_name = str(device[0])  # Convert to string explicitly
    device_data = str(device[1])  # Convert to string without splitting by comma
    list_widget = main_window.ui.list_widget_discovered
    table_widget = main_window.ui.table_adv_data  # Access the table_adv_data

    # HELPER METHODS 
    def add_device_to_list():
        matched_items = list_widget.findItems(device_name, Qt.MatchExactly)
        if not matched_items:
            list_widget.addItem(device_name)
        else:
            # there is a match update the item
            for item in matched_items:
                item.setText(device_name)

    def add_device_to_table():
        # Add the data from device[1] into the table_adv_data
        main_window.add_adv_table_item.emit(device_data)
        
        # this method below is extremely expensive in terms of performance
        # it slows the gui down to a crawl and should only be called when needed
        # I think it is no longer needed because the table widget is being stretched
        # to match the gui window size
        #table_widget.resizeRowsToContents()
 
    def update_rssi_graph():
        pass
        # TODO possibly add a checkbox to disable graphing,
        # the checkbox could be considred here to see if we graph or not
        #main_window.update_rssi_thread.updateDeviceData(device, time.time())

    # check if the filter is empty
    if main_window.ui.txt_scan_filter.text() == "":
        add_device_to_list()
    elif main_window.ui.txt_scan_filter.text() in device_name:
        add_device_to_list()

    if main_window.ui.logAll.isChecked():
        add_device_to_table()
        update_rssi_graph()   
    elif main_window.ui.logSelection.isChecked():
        try:
            # check if the device_name is the same as the selected item in list_widget_discovered
            if device_name == main_window.ui.list_widget_discovered.currentItem().text():
                add_device_to_table()
                update_rssi_graph()
        except AttributeError:
            pass

def add_table_item(main_window, data):
        logger = logging.getLogger("gattLogger")
        # data looks like this: 
        # AdvertisementData(manufacturer_data={301: b'\x04\x00\x02\x02\xb02\x06\x02\xc2\x00\xdd\xb6\xb2\x10\x02\x003\x00\x00\x00'}, 
        # service_data={'0000fe2c-0000-1000-8000-00805f9b34fb': b'\x000\x00\x00\x00\x11\x17402G'}, 
        # service_uuids=['0000fd82-0000-1000-8000-00805f9b34fb'], tx_power=-21, rssi=-62)

        # check if the string  manufacturer_data= is in the data string
        if "manufacturer_data={" in data:
            # extract the numbers after the string "manufacturer_data={"  and before the ":" , these are manufacturer ID
            manufacturer_id = data.split("manufacturer_data={")[1].split(":")[0]
            manufacturer_id = int(manufacturer_id)
            
            # check if that manufacturer ID is in bluetooth numbers library
            try:
                companyID= ble_uuid.company[manufacturer_id]
                #replace the manufacturer ID with the company name in data string
                data = data.replace(str(manufacturer_id),str(companyID))
            except Exception as e:
                companyID = "Unknown"

        # Add the data from device[1] into the table_adv_data
        rowPosition = main_window.ui.table_adv_data.rowCount()
        main_window.ui.table_adv_data.insertRow(rowPosition)

        main_window.ui.table_adv_data.setColumnCount(1)  # Set the number of columns to 1
        main_window.ui.table_adv_data.setHorizontalHeaderItem(0, QTableWidgetItem("Advertised Data"))  # Set the column header
        # align header text to  left
        main_window.ui.table_adv_data.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        #hide horizontal header
        main_window.ui.table_adv_data.horizontalHeader().setVisible(False)
        #hide vertical header
        main_window.ui.table_adv_data.verticalHeader().setVisible(True)
        item = QTableWidgetItem(data)  # Convert data to string explicitly
        item.setTextAlignment(Qt.AlignLeft)  # Center the text
        main_window.ui.table_adv_data.setItem(rowPosition, 0, item)  # Place the data in the first column

        main_window.ui.table_adv_data.setColumnWidth(0, 700)  # Set the width to your desired value
        main_window.ui.table_adv_data.setRowHeight(rowPosition, 40)  # Set the height to your desired value
        if main_window.ui.check_scroll_to_bottom.isChecked():
            main_window.ui.table_adv_data.scrollToBottom()

def txt_scan_filter_changed(main_window):
    logger = logging.getLogger("PDexLogger")
    # filter QListwidget list_widget_discovered based on txt_scan_filter text
    # keeping in mind the list_widget_discovered is not directly iterable 
    # and you can maybe use findItems(device_name, Qt.MatchExactly)
    try:
        # get the text from txt_scan_filter
        filter_text = main_window.ui.txt_scan_filter.text()
        # get the QListWidget list_widget_discovered
        list_widget = main_window.ui.list_widget_discovered
        # get the number of items in the list_widget_discovered
        list_widget_count = list_widget.count()
        # iterate through the list_widget_discovered
        for i in range(list_widget_count):
            # get the item at index i
            item = list_widget.item(i)
            # get the text of the item
            item_text = item.text()
            # check if the filter_text is in the item_text
            if filter_text in item_text:
                # if it is, set the item to visible
                item.setHidden(False)
            else:
                # if it is not, set the item to hidden
                item.setHidden(True)
    except Exception as e:
        main_window.logger.warning(e)
        main_window.logger.warning("txt_scan_filter_changed failed")

def timed_scanning_stoped(main_window):
    main_window.stop_scanner()

def init_signals_and_slots(main_window):
    main_window.ble_scanner.discovered_devices.connect(lambda device : update_discovered_devices(main_window,device))
    main_window.ble_scanner.scanning_stoped.connect(lambda : timed_scanning_stoped(main_window))
    main_window.ui.txt_scan_filter.textChanged.connect(lambda: txt_scan_filter_changed(main_window))