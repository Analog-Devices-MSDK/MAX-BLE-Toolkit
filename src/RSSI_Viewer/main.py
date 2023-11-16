import random
import sys
import time
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QCategoryAxis,
    QChart,
    QChartView,
)
from PySide6.QtCore import Qt,  QThread, Signal, QObject, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

# from ..common import hci_util
BLE_CHANNELS = 40
class RssiWorker(QObject):
    finished = Signal()
    data_ready = Signal(list)
    early_exit = False
    @Slot()
    def process_data(self):

        data_list = [self.get_rssi(x) for x in range(BLE_CHANNELS)]
        self.data_ready.emit(data_list)

    def get_rssi(self,channel):
        return random.randint(-120, 8) + 120

class RssiWorkerThread(QThread):
    early_exit = False
    def __init__(self):
        super().__init__()

        # Create a worker object
        self.worker = RssiWorker()

        # Connect signals and slots
        self.worker.finished.connect(self.finished)
        self.worker.data_ready.connect(self.data_ready)

        

    def run(self):
        # Start the data processing in the worker thread
        while True:
            self.worker.process_data()
            time.sleep(0.1)
            if self.early_exit: 
                return 

    def data_ready(self, data):
        # This method is called when data is ready from the worker thread
        pass

class MainWindow(QMainWindow):
    

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.channel_labels = [str(channel) for channel in range(BLE_CHANNELS)]

        self.rssi_set = QBarSet("RSSIs")
        self.rssi_set.append([random.randint(0, 128) for x in range(BLE_CHANNELS)])

        self._bar_series = QBarSeries()
        self._bar_series.append(self.rssi_set)

        self.chart = QChart()
        self.chart.addSeries(self._bar_series)
        self.chart.setTitle("Channel RSSIS")

        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.channel_labels)
        self.chart.addAxis(self._axis_x, Qt.AlignBottom)

        self._bar_series.attachAxis(self._axis_x)

        self._axis_y = QCategoryAxis()

        for i in range(-120, 30, 5):
            self._axis_y.append(str(i), 120 + i)

        self.chart.addAxis(self._axis_y, Qt.AlignLeft)
        self._bar_series.attachAxis(self._axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.gridLayout.addWidget(self._chart_view)

        self.rssi_capture = RssiWorkerThread()
        self.rssi_capture.worker.data_ready.connect(self.update_rssis)
        self.rssi_capture.start()
        
    def _make_channel_set(self, rssis):
        channel_sets = []
        for i, channel in enumerate(range(BLE_CHANNELS)):
            channel_sets.append(QBarSet(f"{channel}"))
            print(rssis[i])
            channel_sets[i].append([rssis[i]])
        return channel_sets

    def update_rssis(self, data):
        for channel, rssi in enumerate(data):
            self.rssi_set.replace(channel, rssi)

    def closeEvent(self, event) -> None:
        self.rssi_capture.early_exit = True
        self.rssi_capture.quit()
        self.rssi_capture.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
