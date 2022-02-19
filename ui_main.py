# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSguWUM.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        font = QFont()
        font.setFamilies([u"Aldrich"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.planodefundo1 = QFrame(self.centralwidget)
        self.planodefundo1.setObjectName(u"planodefundo1")
        self.planodefundo1.setMaximumSize(QSize(16777215, 16777215))
        self.planodefundo1.setStyleSheet(u"QFrame#planodefundo1{background-color:#064A80}")
        self.planodefundo1.setFrameShape(QFrame.StyledPanel)
        self.planodefundo1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.planodefundo1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.planodefundo1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 385))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(450, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_15)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(650, 200))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 130, 521, 55))
        font1 = QFont()
        font1.setFamilies([u"Aldrich"])
        font1.setPointSize(26)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:#fff")
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 79, 361, 55))
        font2 = QFont()
        font2.setFamilies([u"Aldrich"])
        font2.setPointSize(30)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:#fff")

        self.verticalLayout_2.addWidget(self.frame_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_14)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_14)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{background-color: #064A80}")
        self.page_codigo = QWidget()
        self.page_codigo.setObjectName(u"page_codigo")
        self.lineEdit_codigo = QLineEdit(self.page_codigo)
        self.lineEdit_codigo.setObjectName(u"lineEdit_codigo")
        self.lineEdit_codigo.setGeometry(QRect(130, 50, 200, 40))
        self.lineEdit_codigo.setFont(font)
        self.lineEdit_codigo.setStyleSheet(u"padding-left:14px ;border-radius: 20px")
        self.label_codigo = QLabel(self.page_codigo)
        self.label_codigo.setObjectName(u"label_codigo")
        self.label_codigo.setGeometry(QRect(158, 26, 61, 21))
        font3 = QFont()
        font3.setFamilies([u"Aldrich"])
        font3.setPointSize(12)
        self.label_codigo.setFont(font3)
        self.label_codigo.setStyleSheet(u"color: #fff")
        self.stackedWidget.addWidget(self.page_codigo)
        self.page_chave = QWidget()
        self.page_chave.setObjectName(u"page_chave")
        self.label_chave = QLabel(self.page_chave)
        self.label_chave.setObjectName(u"label_chave")
        self.label_chave.setGeometry(QRect(158, 26, 61, 21))
        self.label_chave.setFont(font3)
        self.label_chave.setStyleSheet(u"color: #fff")
        self.lineEdit_chave = QLineEdit(self.page_chave)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")
        self.lineEdit_chave.setGeometry(QRect(130, 50, 200, 40))
        self.lineEdit_chave.setFont(font)
        self.lineEdit_chave.setStyleSheet(u"padding-left:14px ;border-radius: 20px")
        self.stackedWidget.addWidget(self.page_chave)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.frame_14)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 3)

        self.horizontalLayout_2.addWidget(self.frame_15)

        self.horizontalSpacer_2 = QSpacerItem(111, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_12 = QFrame(self.planodefundo1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 300))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(180, 120, 60, 60))
        self.frame_7.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame_12)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 180, 60, 60))
        self.frame_2.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(180, 240, 60, 60))
        self.frame_4.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(60, 0, 60, 60))
        self.frame_10.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_12)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(60, 120, 60, 60))
        self.frame_6.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 240, 60, 60))
        self.frame_3.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_12)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 60, 60, 60))
        self.frame_8.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_12)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 240, 60, 60))
        self.frame.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(120, 180, 60, 60))
        self.frame_5.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(120, 60, 60, 60))
        self.frame_9.setStyleSheet(u"background-color:#fff\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_12)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.planodefundo1)

        self.planodefundo2 = QFrame(self.centralwidget)
        self.planodefundo2.setObjectName(u"planodefundo2")
        self.planodefundo2.setStyleSheet(u"QFrame#planodefundo2{background-color: #F8FCFF}")
        self.planodefundo2.setFrameShape(QFrame.StyledPanel)
        self.planodefundo2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.planodefundo2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.planodefundo2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 210))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_18)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 90, 0, 0)
        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:#064A80")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 16, 0)
        self.horizontalSpacer_3 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.search_box = QFrame(self.frame_17)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setMinimumSize(QSize(200, 0))
        self.search_box.setMaximumSize(QSize(16777215, 32))
        self.search_box.setStyleSheet(u"QFrame#search_box {border: 1px solid #c4c4c4; background-color: #FFF; border-radius: 16px}\n"
"QLineEdit{border-radius: 15px}")
        self.search_box.setFrameShape(QFrame.StyledPanel)
        self.search_box.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.search_box)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1, 1, 165, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"	border-right:1px solid #c4c4c4;\n"
"	padding-left: 14px\n"
"}\n"
"")
        self.toolButton = QToolButton(self.search_box)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(170, 5, 22, 22))
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(u"QToolButton{background-color:#fff; border:hidden}")
        icon = QIcon()
        icon.addFile(u"icons/search_black_18dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(18, 18))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)

        self.horizontalLayout_3.addWidget(self.search_box)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.planodefundo2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_16)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(128, 32, 128, 32)
        self.tableEmprestimo = QTableWidget(self.frame_16)
        if (self.tableEmprestimo.columnCount() < 3):
            self.tableEmprestimo.setColumnCount(3)

        font4 = QFont()
        font4.setPointSize(18)
        font4.setUnderline(True)

        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setForeground(QColor('#064A80'))
        self.tableEmprestimo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableEmprestimo.setObjectName(u"tableEmprestimo")
        
        p = self.tableEmprestimo.palette()
        p.setColor(QPalette.Base, '#F8FCFF')
        p.setColor(QPalette.AlternateBase, '#EFF4FB')
        p.setColor(QPalette.Highlight, '#D2E4FF')
        p.setColor(QPalette.HighlightedText, '#000000')
        self.tableEmprestimo.setPalette(p)
        
        self.tableEmprestimo.horizontalHeader().setStyleSheet(u"QHeaderView::Section{height:70px; background-color: #F8FCFF; border:hidden}")
        self.tableEmprestimo.setStyleSheet(u"QTableView{border: hidden}")
        self.tableEmprestimo.verticalHeader().setVisible(False)
        self.tableEmprestimo.horizontalHeader().setHighlightSections(False)
        self.tableEmprestimo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableEmprestimo.setFocusPolicy(Qt.NoFocus)
        self.tableEmprestimo.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableEmprestimo.setAlternatingRowColors(True)
        self.tableEmprestimo.setShowGrid(False)
        self.tableEmprestimo.setSortingEnabled(False)
        self.tableEmprestimo.setFont(font3)

        self.verticalLayout_4.addWidget(self.tableEmprestimo)


        self.verticalLayout_5.addWidget(self.frame_16)


        self.horizontalLayout.addWidget(self.planodefundo2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Entre com seu c\u00f3digo.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bem vindo,", None))
        self.label_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.label_chave.setText(QCoreApplication.translate("MainWindow", u"Chave:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimos", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.toolButton.setText("")
        ___qtablewidgetitem = self.tableEmprestimo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tableEmprestimo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Colaborador", None));
        ___qtablewidgetitem2 = self.tableEmprestimo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Retirada", None));
    # retranslateUi

