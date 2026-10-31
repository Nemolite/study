import sys
import sqlite3
from asyncio import QueueEmpty

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget, \
    QGridLayout, QFormLayout, QCheckBox, QComboBox, QSpinBox


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowTitle("Работа с БД")
        # self.button_db = QPushButton("Создать таблицу БД", self)
        # self.button_db.clicked.connect(self.myfunc)
        # self.button_db.setGeometry(30,30,150,50)
        #
        # self.input1 = QLineEdit(self)
        # self.input1.setPlaceholderText("Введит name")  # Подсказка внутри поля
        # self.input1.setGeometry(30,80,150,50)
        #
        # self.input2 = QLineEdit(self)
        # self.input2.setPlaceholderText("Введит age")
        # self.input2.setGeometry(30,120,150,50)
        #
        # self.checkbox = QCheckBox('Я согласен', self)
        # self.checkbox.setGeometry(30, 180, 150, 50)
        # self.checkbox.stateChanged.connect(self.changed)
        #
        # self.button = QPushButton("Нажми", self)
        # self.button.setGeometry(30, 210, 150, 50)
        # self.button.setEnabled(False)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # form_layout = QFormLayout(central_widget)
        # self.setLayout(form_layout)

        self.layout = QFormLayout(central_widget)
        self.setLayout(self.layout)

        self.layout.addRow('Name:', QLineEdit(self))
        self.layout.addRow('Email:', QLineEdit(self))
        self.layout.addRow('Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        self.layout.addRow('Confirm Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        self.layout.addRow('Phone:', QLineEdit(self))


        self.checkbox = QCheckBox('Я согласен', self)
        # self.checkbox.setGeometry(30, 180, 150, 50)
        self.checkbox.stateChanged.connect(self.changed)
        self.layout.addRow(self.checkbox)

        self.button = QPushButton("Нажми", self)
        # self.button.setGeometry(30, 210, 150, 50)
        self.button.resize(200,200)
        self.button.setEnabled(False)

        self.layout.addRow(self.button)



    def myfunc(self):
          con = sqlite3.connect("basa.db")
          cursor = con.cursor()
          cursor.execute("""CREATE TABLE IF NOT EXISTS people
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                             age INTEGER)
                          """)

    def changed(self,value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.button.setEnabled(True)
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            self.button.setEnabled(False)
            print('Unchecked')

app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(200,200,600,600)

window.show()

app.exec()

#########

import sys
import sqlite3
from asyncio import QueueEmpty

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget, \
    QGridLayout, QFormLayout, QCheckBox, QComboBox, QSpinBox, QRadioButton


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowTitle("Работа с БД")
        # self.button_db = QPushButton("Создать таблицу БД", self)
        # self.button_db.clicked.connect(self.myfunc)
        # self.button_db.setGeometry(30,30,150,50)
        #
        # self.input1 = QLineEdit(self)
        # self.input1.setPlaceholderText("Введит name")  # Подсказка внутри поля
        # self.input1.setGeometry(30,80,150,50)
        #
        # self.input2 = QLineEdit(self)
        # self.input2.setPlaceholderText("Введит age")
        # self.input2.setGeometry(30,120,150,50)
        #
        # self.checkbox = QCheckBox('Я согласен', self)
        # self.checkbox.setGeometry(30, 180, 150, 50)
        # self.checkbox.stateChanged.connect(self.changed)
        #
        # self.button = QPushButton("Нажми", self)
        # self.button.setGeometry(30, 210, 150, 50)
        # self.button.setEnabled(False)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # form_layout = QFormLayout(central_widget)
        # self.setLayout(form_layout)

        self.layout = QFormLayout(central_widget)
        self.setLayout(self.layout)

        self.layout.addRow('Name:', QLineEdit(self))
        self.layout.addRow('Email:', QLineEdit(self))
        self.layout.addRow('Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        self.layout.addRow('Confirm Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        self.layout.addRow('Phone:', QLineEdit(self))


        self.checkbox = QCheckBox('Я согласен', self)
        # self.checkbox.setGeometry(30, 180, 150, 50)
        self.checkbox.stateChanged.connect(self.changed)
        self.layout.addRow(self.checkbox)

        self.button = QPushButton("Нажми", self)
        # self.button.setGeometry(30, 210, 150, 50)
        self.button.resize(200,200)
        self.button.setEnabled(False)

        self.layout.addRow(self.button)

        # radio

        self.rb_android = QRadioButton('Android', self)
        self.rb_android.toggled.connect(self.update)
        self.layout.addRow(self.rb_android)

        self.rb_ios = QRadioButton('iOS', self)
        self.rb_ios.toggled.connect(self.update)
        self.layout.addRow(self.rb_ios)

        self.rb_windows = QRadioButton('Windows', self)
        self.rb_windows.toggled.connect(self.update)
        self.layout.addRow(self.rb_windows)
    def update(self):
        rb = self.sender()
        print(rb)
        print(type(rb))
        print(rb.text())


    def myfunc(self):
          con = sqlite3.connect("basa.db")
          cursor = con.cursor()
          cursor.execute("""CREATE TABLE IF NOT EXISTS people
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                             age INTEGER)
                          """)

    def changed(self,value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.button.setEnabled(True)
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            self.button.setEnabled(False)
            print('Unchecked')

app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(200,200,600,600)

window.show()

app.exec()
