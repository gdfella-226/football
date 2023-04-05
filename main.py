from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, \
    QPushButton, QComboBox, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QSize, Qt, pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.scene = None
        self.table = None
        self.dump1 = None
        self.dump2 = None
        self.dump3 = None
        self.show_scene('Команды', 8, ["Команда", "Дивизион", "Формат", "Тренер",
                                        "Дата", "Стадион", "Время", "Желаемое Время"], self.enter2)
        #self.scene3()

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
        for i in range(cols):
            self.table.setItem(0, i, QTableWidgetItem(''))

        button_enter = QPushButton('Ввод', self)
        button_enter.clicked.connect(func)

        button_clear = QPushButton('Добавить команду', self)
        button_clear.clicked.connect(self.insert)

        grid_layout.addWidget(self.table, 0, 0)
        inner_grid = QGridLayout(self)
        grid_layout.addLayout(inner_grid, 0, 1)
        inner_grid.addWidget(button_clear, 0, 0)
        inner_grid.addWidget(button_enter, 1, 0)

    def scene3(self):
        self.setWindowTitle("Предыдущие игры")
        self.setMinimumSize(QSize(1080, 800))
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        self.cb = QComboBox()
        self.data = {
              "division1": ["team1", "team2", "team3"],
              "division2": ["team4", "team5", "team6"],
              "division3": ["team7", "team8", "team9"]
            }
        for i in list(self.data.keys()):
            self.cb.addItem(i)

        self.cb.currentIndexChanged.connect(self.selection_change)
        self.table = QTableWidget(self)

        button_enter = QPushButton('Ввод', self)
        button_enter.clicked.connect(self.prev_games)

        grid_layout.addWidget(self.table, 0, 0)
        inner_grid = QGridLayout(self)
        grid_layout.addLayout(inner_grid, 0, 1)
        inner_grid.addWidget(self.cb, 0, 0)
        inner_grid.addWidget(button_enter, 1, 0)

    def selection_change(self):
        try:
            self.get_games()
        except:
            pass
        key = self.cb.currentText()
        commands = self.data[key]
        commands *= (len(commands))
        tmp = []
        for i, j in zip(commands, sorted(commands)):
            tmp.append([i, j])
        res = sorted(set([tuple(sorted(i)) for i in tmp if i[0] != i[1]]))
        self.table.setRowCount(len(res))
        self.table.setColumnCount(3)
        for i in res:
            self.table.setItem(res.index(i), 2, QTableWidgetItem('-'))
            self.table.setItem(res.index(i), 1, QTableWidgetItem(i[1]))
            self.table.setItem(res.index(i), 0, QTableWidgetItem(i[0]))

    def get_games(self):
        res = []
        for i in range(0, self.table.rowCount()):
            res.append([])
            for j in range(0, self.table.columnCount()):
                res[i].append(self.table.item(i, j).text())
        self.dump3 += res

    def read(self, flag):
        dump = []
        while not dump:
            for i in range(0, self.table.rowCount()):
                dump.append([])
                for j in range(0, self.table.columnCount()):
                    item = self.table.item(i, j)
                    if flag == 1 and j == 7 and item.text() == '':
                        dump[i].append('00:00-24:00')
                    else:
                        dump[i].append(item.text())
            print(dump)
            for i in dump:
                if '' in i:
                    QMessageBox.warning(self, "ВНИМАНИЕ!", "Заполните таблицу, перед тем как продолжить работу")
                    dump = []
                    break

        if flag == 1:
            self.dump1 = dump
        elif flag == 2:
            self.dump2 = dump

    @pyqtSlot()
    def insert(self):
        self.table.setRowCount(self.table.rowCount() + 1)
        self.table.setItem(0, self.table.rowCount(), QTableWidgetItem(''))

    @pyqtSlot()
    def enter1(self):
        self.show_scene('Команды', 8, ["Команда", "Дивизион", "Формат", "Тренер",
                                       "Дата", "Стадион", "Время", "Доп. Время"], self.enter2)

    @pyqtSlot()
    def enter2(self):
        self.read(1)
        self.show_scene('Данные по туру', 7, ["Формат", "Дата", "Стадион", "Поле",
                                              "Время", "Время игры", "Количество игр"], self.enter3)

    @pyqtSlot()
    def enter3(self):
        self.read(2)
        self.scene3()

    @pyqtSlot()
    def prev_games(self):
        try:
            self.get_games()
        except:
            pass
        for i in self.dump1:
            print(i)
        print('--------------------------------')
        for i in self.dump2:
            print(i)
        print('--------------------------------')
        for i in self.dump3:
            print(i)


if __name__ == "__main__":
    app = QApplication(argv)
    mw = MainWindow()
    mw.showMaximized()
    exit(app.exec())
