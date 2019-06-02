from PyQt5.QtWidgets import *

class Pendaftaran(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi2()

    def setupUi2(self):
        self.setWindowTitle('Form Pendaftaran')
        self.setFixedSize(350, 350)
        self.move(300,300)

        self.judul = QLabel('<b>Pendaftaran Calon Anggota Avengers</b>')

        self.nama = QLabel('Nama')
        self.nameEdit = QLineEdit()

        self.JK = QLabel('Jenis Kelamin')
        self.laki = QRadioButton('Laki-laki')
        self.laki.setChecked(True)
        self.perempuan = QRadioButton('Perempuan')

        self.Tgl = QLabel('Tanggal Lahir')
        self.tanggal = QDateEdit()
        self.tanggal.setDisplayFormat('dd/MM/yyyy')

        self.hobi = QLabel('Hobi')
        self.hobiBox = QComboBox()
        self.hobiBox.addItem('--Pilih Hobi--')
        self.hobiBox.addItem('basket')
        self.hobiBox.addItem('sepak bola')
        self.hobiBox.addItem('voli')
        self.hobiBox.addItem('catur')
        self.hobiBox.addItem('lainnya')

        self.alamat = QLabel('Alamat')
        self.alamatEdit = QTextEdit()

        self.submit = QPushButton('Submit')
        self.cancel = QPushButton('Cancel')

        self.layout = QGridLayout()
        self.layout.addWidget(self.judul, 0, 1, 1, 2)
        self.layout.addWidget(self.nama, 1, 0, 1, 1)
        self.layout.addWidget(self.nameEdit, 1, 1, 1, 2)
        self.layout.addWidget(self.JK, 2, 0, 1, 1)
        self.layout.addWidget(self.laki, 2, 1, 1, 2)
        self.layout.addWidget(self.perempuan, 3, 1, 1, 2)
        self.layout.addWidget(self.Tgl, 4, 0, 1, 1)
        self.layout.addWidget(self.tanggal, 4, 1, 1, 2)
        self.layout.addWidget(self.hobi, 5, 0, 1, 1)
        self.layout.addWidget(self.hobiBox, 5, 1, 1, 2)
        self.layout.addWidget(self.alamat, 6, 0, 1, 1)
        self.layout.addWidget(self.alamatEdit, 6, 1, 1, 2)
        self.layout.addWidget(self.submit, 7, 1, 1, 1)
        self.layout.addWidget(self.cancel, 7, 2, 1, 1)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.submitClicked)
        self.cancel.clicked.connect(self.cancelClicked)

    def submitClicked(self):
        nama = str(self.nameEdit.text())
        tgl = str(self.tanggal.date().toString())
        hobi = str(self.hobiBox.currentText())
        alamat = str(self.alamatEdit.toPlainText())

        if self.laki.isChecked():
            QMessageBox.information(self, 'Pendaftaran Berhasil',
                                    'Nama : ' + nama  +
                                    '\nJenis Kelamin : Laki-Laki' +
                                    '\nTanggal Lahir : ' + tgl +
                                    '\nHobi : ' + hobi +
                                    '\nAlamat : ' + alamat + '\n')
        else:
            QMessageBox.information(self, 'Pendaftaran Berhasil',
                                    'Nama : ' + nama +
                                    '\nJenis Kelamin : Perempuan' +
                                    '\nTanggal Lahir : ' + tgl +
                                    '\nHobi : ' + hobi +
                                    '\nAlamat : ' + alamat + '\n')
    def cancelClicked(self):
        self.close()

