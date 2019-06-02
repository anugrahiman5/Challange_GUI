import sys

from FormPendaftaran import *

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi1()

    def setupUi1(self):
        self.setWindowTitle('Kuis Pemrograman GUI')
        self.setFixedSize(225,125)
        self.move(300,300)

        self.username = QLabel('Username')
        self.password = QLabel('Password')

        self.userText = QLineEdit()
        self.passText = QLineEdit()
        self.passText.setEchoMode(QLineEdit.Password)

        self.blogin = QPushButton('Login')
        self.bclear = QPushButton('Clear')

        self.layout = QGridLayout()
        self.layout.addWidget(self.username, 0, 0, 1, 1)
        self.layout.addWidget(self.password, 1, 0, 1, 1)
        self.layout.addWidget(self.userText, 0, 1, 1, 2)
        self.layout.addWidget(self.passText, 1, 1, 1, 2)
        self.layout.addWidget(self.blogin, 2, 1, 1, 1)
        self.layout.addWidget(self.bclear, 2, 2, 1, 1)
        self.setLayout(self.layout)

        self.blogin.clicked.connect(self.loginClicked)
        self.bclear.clicked.connect(self.clearClicked)

    def loginClicked(self):
        user = self.userText.text()
        pw = self.passText.text()

        if not user or not pw:
            QMessageBox.information(self, 'Perhatian', 'Username atau password tidak boleh kosong')
        else:
            if user == '17104022' and pw == '12345':
                self.form = Pendaftaran()
                self.form.show()
                self.close()
            else:
                QMessageBox.information(self, 'Perhatian', 'Username atau password Salah')

    def clearClicked(self):
        self.userText.clear()
        self.passText.clear()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = Login()
    form.show()
    a.exec_()