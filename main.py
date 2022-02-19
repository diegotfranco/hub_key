import sys
from datetime import datetime
from ui_main import *
from ui_dialog import Ui_Dialog, Ui_Dialog_2

class Overlay(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Window, Qt.transparent)
        self.setPalette(palette)
              
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(0, 0, 0, 127)))
        painter.end()


class Dialog(QDialog):
    def __init__(self, parent) -> None:
        super(Dialog, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        

class Dialog2(QDialog):
    def __init__(self, parent) -> None:
        super(Dialog2, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self)
       

class MainWindow(QMainWindow):

    timer = QTimer()

    '''emprestimos = [[302,'Tatiane', '12:55'], [302,'Tatiane', '12:55'], [302,'Tatiane', '12:55'],
                    [307,'Enilda', '12:55'], [307,'Enilda', '12:55'], [307,'Enilda', '12:55']]'''

    emprestimos = []
    codigos = {'0264':'Diego', '2130':'Anderson', '9329':'Mariana', '1428':'Tatiana', '4287':'Enilda'}
    chaves = ['301', '302', '303', '304', '305', '306', '307', '310', '311']

    codigo = None

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.popup = Overlay(self)
        self.popup.setMinimumWidth(1920)
        self.popup.setMinimumHeight(1080)
        self.popup.hide()

        self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableEmprestimo.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.carregaEmprestimo()

        self.showMaximized()
        self.show()

        #SINAIS DE CONTROLE
        self.ui.lineEdit_codigo.editingFinished.connect(self.salvaUsuario)
        #---------------------------------------------------------------#
        self.ui.lineEdit_chave.editingFinished.connect(self.fazEmprestimo)
        #---------------------------------------------------------------#
        self.timer.timeout.connect(self.deslogar)

        #BOTÃO BUSCA
        self.ui.toolButton.clicked.connect(self.carregaEmprestimo)

    def deslogar(self):
        self.codigo = None
        self.timer.stop()

        self.ui.label.setText('Bem vindo,')
        self.ui.label_2.setText('Entre com seu código.')

        self.ui.lineEdit_chave.blockSignals(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_codigo)

        msg = Dialog2(self)
        msg.ui.label.setText('Usuário Deslogado!')
        self.popup.show()
        msg.exec()
        self.popup.hide()

    def devolveChave(self, pos):
        msg = Dialog(self)
        msg.ui.label.setText(f'{self.codigos[self.codigo]}, deseja devolver a chave {self.emprestimos[pos][0]}')

        msg2 = Dialog2(self)
        self.popup.show()
        if msg.exec():
            msg2.ui.label.setText(f'Chave devolvida com sucesso.')
            self.emprestimos.pop(pos)
            self.ui.tableEmprestimo.removeRow(pos)
        else:
            msg2.ui.label.setText(f'Operação cancelada!')
        msg2.exec()
        self.popup.hide()

    def carregaEmprestimo(self):
        txt = self.ui.lineEdit_2.text().lower()

        if txt == '':
            emprestimos = self.emprestimos
        else:
            emprestimos = [i for i in self.emprestimos if i[0].lower() == txt or i[1].lower() == txt]
        
        self.ui.tableEmprestimo.setRowCount(len(emprestimos))

        for row, emprestimo in enumerate(emprestimos):
            for col, dado in enumerate(emprestimo):
                self.ui.tableEmprestimo.setItem(row, col, QTableWidgetItem(str(dado)))
                self.ui.tableEmprestimo.item(row, col).setTextAlignment(Qt.AlignCenter)
            
        #self.ui.tableEmprestimo.setColumnHidden(0, True)
    
    def salvaUsuario(self):
        self.ui.lineEdit_codigo.blockSignals(True)
        self.codigo = self.ui.lineEdit_codigo.text()
        self.ui.lineEdit_codigo.setText('')

        if self.codigo not in self.codigos.keys():
            msg = Dialog2(self)
            msg.ui.label.setText('Código não encontrado!')
            self.popup.show()
            msg.exec()
            self.popup.hide()
            #QTimer.singleShot(3000, lambda : self.fechaMsg)
            self.ui.lineEdit_codigo.blockSignals(False)
            return

        self.ui.label.setText(f'Olá {self.codigos[self.codigo]},')
        self.ui.label_2.setText(f'Entre com o código da chave.')

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_chave)
        self.ui.lineEdit_codigo.blockSignals(False)
        self.timer.start(25000)

    def fazEmprestimo(self):
        self.ui.lineEdit_chave.blockSignals(True)
        chave = self.ui.lineEdit_chave.text()
        self.ui.lineEdit_chave.setText('')

        for pos, emprestimo in enumerate(self.emprestimos):
            if emprestimo[0] == chave:
                self.devolveChave(pos)
                self.ui.lineEdit_chave.blockSignals(False)
                return        

        if chave  not in self.chaves:
            msg = Dialog2(self)
            msg.ui.label.setText('Chave não encontrada!')
            self.popup.show()
            msg.exec()
            self.popup.hide()
            #QTimer.singleShot(3000, lambda : self.fechaMsg)
            self.ui.lineEdit_chave.blockSignals(False)
            return

        msg = Dialog(self)
        msg.ui.label.setText(f'{self.codigos[self.codigo]}, deseja retirar a chave {chave}')

        msg2 = Dialog2(self)
        self.popup.show()
        if msg.exec():
            msg2.ui.label.setText(f'Chave retirada com sucesso.')
            self.emprestimos.append([str(chave), self.codigos[self.codigo], str(datetime.now().time())[:5]])
            self.carregaEmprestimo()
        else:
            msg2.ui.label.setText(f'Operação cancelada!')
        msg2.exec()
        self.popup.hide()
        #QTimer.singleShot(3000, lambda : self.fechaMsg)
        
        self.ui.lineEdit_chave.blockSignals(False)


if __name__ == '__main__':

	#myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	app = QApplication(sys.argv)
	#app.setWindowIcon(QIcon('icons\church_black_48dp.svg'))

	window = MainWindow()
	sys.exit(app.exec())
	