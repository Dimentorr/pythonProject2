import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QComboBox, QMessageBox


class LastWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        cur = self.con.cursor()

        self.setGeometry(300, 300, 370, 220)
        self.setWindowTitle('Итог поиска')
        #
        self.OutData = QTextBrowser(self)
        self.OutData.setGeometry(10, 10, 350, 200)
        tmp = ex.ForLastIteration
        answer = cur.execute("""Select * from List_com
        where Name_command=?""", (tmp,)).fetchall()
        self.OutData.setText(f'{answer[0][1]} - {answer[0][-1]}')


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur2 = self.con.cursor()

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Команды')
        #
        self.btn = QPushButton('Показать', self)
        self.btn.setGeometry(240, 28, 100, 50)
        self.btn.clicked.connect(self.Find)
        #
        self.slider = QComboBox(self)
        self.slider.setGeometry(10, 10, 200, 20)
        #
        tmp = ex.data[0]
        result = tmp
        for i in range(len(result)):
            self.slider.insertItem(i, result[i])

    def Find(self):
        ex.ForLastIteration = self.slider.currentText()
        self.w3 = LastWindow()
        self.w3.show()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ForLastIteration = ''

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur = self.con.cursor()

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Справочник')
        #
        self.btn = QPushButton('Искать', self)
        self.btn.setGeometry(240, 28, 100, 50)
        self.btn.clicked.connect(self.Find)
        #
        self.slider = QComboBox(self)
        self.slider.setGeometry(10, 10, 200, 20)
        #
        result = self.cur.execute("""SELECT * FROM tags""").fetchall()
        for i in range(len(result)):
            self.slider.insertItem(i, result[i][1])

    def Find(self):
        tmp = self.slider.currentText()
        self.data = self.cur.execute("""Select Name_command from List_com where tags=(
        Select id from tags where tag=?)""", (tmp,)).fetchall()
        if self.data:
            self.w2 = SecondWindow()
            self.w2.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Совпадений не найдено")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())