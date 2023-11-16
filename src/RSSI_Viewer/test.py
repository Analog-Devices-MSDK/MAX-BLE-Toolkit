import sys
from PySide6.QtCore import Qt, QThread, Signal, QObject, Slot
from PySide6.QtWidgets import QWidget,QApplication, QMainWindow, QVBoxLayout, QPushButton, QListWidget

class Worker(QObject):
    finished = Signal()
    data_ready = Signal(list)

    @Slot()
    def process_data(self):
        # Simulate some data processing
        data_list = [1, 2, 3, 4, 5]

        # Emit the signal with the processed data
        self.data_ready.emit(data_list)

        # Notify that the task is finished
        self.finished.emit()

class WorkerThread(QThread):
    def __init__(self):
        super().__init__()

        # Create a worker object
        self.worker = Worker()

        # Connect signals and slots
        self.worker.finished.connect(self.finished)
        self.worker.data_ready.connect(self.data_ready)

    def run(self):
        # Start the data processing in the worker thread
        self.worker.process_data()

    def data_ready(self, data):
        # This method is called when data is ready from the worker thread
        print("Data ready in worker thread:", data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)

        start_button = QPushButton("Start Thread", self)
        start_button.clicked.connect(self.start_thread)
        layout.addWidget(start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a thread instance
        self.thread = WorkerThread()

        # Connect the thread's data_ready signal to a slot in the main thread
        self.thread.worker.data_ready.connect(self.update_list_widget)

    def start_thread(self):
        # Start the thread
        self.thread.start()

    def update_list_widget(self, data):
        # This method is called when data is received in the main thread
        self.list_widget.addItems([str(item) for item in data])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())