from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QPushButton, QVBoxLayout
from PyQt5.QtCore import QSize, Qt, pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.scene = None
        self.table = None
        self.dump = None

        self.show_scene('Команды', 8, ["Команда", "Дивизион", "Формат", "Тренер",
                                       "Дата", "Стадион", "Время", "Доп. Время"], self.enter2)

    def show_scene(self, title, cols, headers, func):
        self.setWindowTitle(title)
        self.setMinimumSize(QSize(1080, 800))
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        self.table = QTableWidget(self)
        self.table.setColumnCount(cols)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(headers)

        button_enter = QPushButton('Ввод', self)
        button_enter.clicked.connect(func)

        button_clear = QPushButton('Добавить команду', self)
        button_clear.clicked.connect(self.insert)

        grid_layout.addWidget(self.table, 0, 0)
        inner_grid = QGridLayout(self)
        grid_layout.addLayout(inner_grid, 0, 1)
        inner_grid.addWidget(button_clear, 0, 0)
        inner_grid.addWidget(button_enter, 1, 0)

    @pyqtSlot()
    def insert(self):
        self.table.setRowCount(self.table.rowCount() + 1)

    @pyqtSlot()
    def enter1(self):
        # self.read()
        self.show_scene('Команды', 8, ["Команда", "Дивизион", "Формат", "Тренер",
                                       "Дата", "Стадион", "Время", "Доп. Время"], self.enter2)
        #self.close()

    @pyqtSlot()
    def enter2(self):
        self.read()
        self.show_scene('Данные по туру', 7, ["Формат", "Дата", "Стадион", "Поле",
                                              "Время", "Время игры", "Количество игр"], self.enter3)
        #self.close()

    @pyqtSlot()
    def enter3(self):
        pass

    def read(self):
        dump = []
        for i in range(0, self.table.rowCount()):
            dump.append([])
            for j in range(0, self.table.columnCount()):
                item = self.table.item(i, j)
                dump[i].append(item.text())
        print(dump)
        self.dump = dump


if __name__ == "__main__":
    app = QApplication(argv)
    mw = MainWindow()
    mw.showMaximized()
    exit(app.exec())
