from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1080, 800))  # Set sizes
        self.setWindowTitle("Работа с QTableWidget")  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        table = QTableWidget(self)  # Create a table
        table.setColumnCount(7)  # Set three columns
        table.setRowCount(370)  # and one row

        # Set the table headers
        table.setHorizontalHeaderLabels(["Команда", "Дивизион", "Формат",
                                         "Тренер", "Дата", "Стадион", "Время"])


        button_enter = QPushButton('Ввод', self)
        button_clear = QPushButton('Сброс', self)

        grid_layout.addWidget(table, 0, 0)
        inner_grid = QGridLayout(self)
        grid_layout.addLayout(inner_grid, 0, 1)
        inner_grid.addWidget(button_clear, 0, 0)
        inner_grid.addWidget(button_enter, 1, 0)
        #button_clear.move(1000, 100)
        #button_enter.move(0, 130)
        self.showMaximized()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())