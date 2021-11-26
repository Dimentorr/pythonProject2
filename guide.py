import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QComboBox, QMessageBox,\
    QLineEdit, QLabel, QTextEdit, QInputDialog


class LastWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur = self.con.cursor()

        self.setGeometry(650, 260, 370, 220)
        self.setWindowTitle('Итог поиска')
        #
        self.OutData = QTextEdit(self)
        self.OutData.setGeometry(10, 10, 300, 200)

        self.btn = QPushButton(self)
        self.btn.setGeometry(310, 10, 58, 90)
        self.btn.setText('Удалить')
        self.btn.clicked.connect(self.delComponent)

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(310, 120, 58, 90)
        self.btn1.setText('Изменить')
        self.btn1.clicked.connect(self.addData)

        tmp = ex.ForLastIteration
        self.answer = self.cur.execute("""Select * from List_com
        where Name_command=?""", (tmp,)).fetchall()
        self.OutData.setText(f'{self.answer[0][1]} - {self.answer[0][-1]}')

    def addData(self):
        valid = QMessageBox.question(
            self, '', "Вы уверены, что хотите изменить этот элемент?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            tmp = self.OutData.toPlainText().split(' - ')
            tmp = tmp[1:]
            self.cur.execute("""Update List_com set Valuess=? where id=?""", (' - '.join(tmp), self.answer[0][0]))
            self.con.commit()
        self.close()

    def delComponent(self):
        valid = QMessageBox.question(
            self, '', "Вы действительно хотите удалить этот элемент?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.cur.execute("""Delete from List_com where id=?""", (self.answer[0][0],))
            self.con.commit()
        self.close()


class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur = self.con.cursor()
        #
        self.setGeometry(650, 260, 400, 220)
        self.setWindowTitle('Добавление команды')
        #
        self.btn = QPushButton(self)
        self.btn.setGeometry(15, 100, 60, 60)
        self.btn.setText('Добавить')
        self.btn.clicked.connect(self.add_component)
        #
        self.text0 = QLabel(self)
        self.text0.move(10, 10)
        self.text0.setText('Тег команды')
        #
        self.text1 = QLabel(self)
        self.text1.move(10, 30)
        self.text1.setText('Команда')
        #
        self.text2 = QLabel(self)
        self.text2.move(10, 50)
        self.text2.setText('Описание')
        #
        self.textTag = QLineEdit(self)
        self.textTag.move(100, 10)
        #
        self.textCom = QLineEdit(self)
        self.textCom.move(100, 30)
        #
        self.textVal = QTextEdit(self)
        self.textVal.setGeometry(100, 50, 270, 150)

    def add_component(self):
        if (self.textTag.text() != '') and (self.textCom.text() != '' and (self.textVal.toPlainText() != '')):
            result = self.cur.execute("""Select id from tags 
            where tag = ?""", (self.textTag.text(), )).fetchall()

            if result:
                print(f'''---{result[0][0]}---''')
                print(f'''---{type(self.textVal.toPlainText())}---''')
                self.cur.execute("""Insert into List_com(Name_command, tags, Valuess) Values(?, ?, ?)""",
                                 (str(self.textCom.text()), int(result[0][0]), str(self.textVal.toPlainText())))
                self.con.commit()
                self.close()
            else:
                print(1)
                self.cur.execute("""Insert into tags(tag) Values(?)""", (str(self.textTag.text()),))
                self.con.commit()
                result = self.cur.execute("""Select id from tags 
                            where tag = ?""", (self.textTag.text(),)).fetchall()
                print(f'''---{result[0][0]}---''')
                print(f'''---{self.textVal.toPlainText()}---''')
                self.cur.execute("""Insert into List_com(Name_command, tags, Valuess) Values(?, ?, ?)""",
                                 (str(self.textCom.text()), result[0][0], str(self.textVal.toPlainText())))
                self.con.commit()
                self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Заполните все поля")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur2 = self.con.cursor()

        self.setGeometry(350, 350, 350, 100)
        self.setWindowTitle('Команды')
        #
        self.btn = QPushButton('Показать', self)
        self.btn.setGeometry(240, 28, 100, 50)
        self.btn.clicked.connect(self.Find)
        #
        self.slider = QComboBox(self)
        self.slider.setGeometry(10, 10, 200, 20)
        #
        tmp = ex.data
        result = tmp
        for i in range(len(result)):
            self.slider.insertItem(i, result[i][0])

    def Find(self):
        try:
            ex.ForLastIteration = self.slider.currentText()
            self.w3 = LastWindow()
            self.w3.show()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Что-топошло не так...")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ForLastIteration = ''

    def initUI(self):
        self.con = sqlite3.connect('БД/list_command_bd.db')
        self.cur = self.con.cursor()

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Справочник')
        #
        self.btn = QPushButton('Искать', self)
        self.btn.setGeometry(240, 5, 100, 40)
        self.btn.clicked.connect(self.Find)
        #
        self.btn1 = QPushButton('Добавить', self)
        self.btn1.setGeometry(240, 50, 100, 40)
        self.btn1.clicked.connect(self.AddWind)
        #
        self.btn1 = QPushButton('Обновить', self)
        self.btn1.setGeometry(240, 95, 100, 40)
        self.btn1.clicked.connect(self.reset)
        #
        self.slider = QComboBox(self)
        self.slider.setGeometry(10, 10, 200, 20)
        #
        result = self.cur.execute("""SELECT * FROM tags""").fetchall()
        for i in range(len(result)):
            self.slider.insertItem(i, result[i][1])

    def reset(self):
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

    def AddWind(self):
        self.wAdd = AddWindow()
        self.wAdd.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())