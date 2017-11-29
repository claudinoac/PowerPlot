# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/CalibracaoT.ui'
#
# Created: Wed Nov 29 17:01:02 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from InterfaceTimer import InterfaceTimer

class Ui_MainWindow(InterfaceTimer):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 695)
        MainWindow.setMinimumSize(QtCore.QSize(817, 0))
        MainWindow.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"color: rgb(255,255,255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")
        self.CentralGraph = QtWidgets.QGraphicsView(self.centralWidget)
        self.CentralGraph.setGeometry(QtCore.QRect(420, 10, 931, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CentralGraph.sizePolicy().hasHeightForWidth())
        self.CentralGraph.setSizePolicy(sizePolicy)
        self.CentralGraph.setObjectName("CentralGraph")
        self.scaleBox = QtWidgets.QGroupBox(self.centralWidget)
        self.scaleBox.setGeometry(QtCore.QRect(10, 10, 401, 231))
        self.scaleBox.setToolTip("")
        self.scaleBox.setStatusTip("")
        self.scaleBox.setWhatsThis("")
        self.scaleBox.setAutoFillBackground(False)
        self.scaleBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(194, 8, 6);\n"
"color: rgb(255, 255, 255);")
        self.scaleBox.setFlat(False)
        self.scaleBox.setCheckable(False)
        self.scaleBox.setObjectName("scaleBox")
        self.tempBox = QtWidgets.QGroupBox(self.scaleBox)
        self.tempBox.setGeometry(QtCore.QRect(10, 30, 181, 91))
        self.tempBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.tempBox.setObjectName("tempBox")
        self.temp_max = QtWidgets.QLineEdit(self.tempBox)
        self.temp_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.temp_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.temp_max.setObjectName("temp_max")
        self.temp_max_label = QtWidgets.QLabel(self.tempBox)
        self.temp_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.temp_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.temp_max_label.setObjectName("temp_max_label")
        self.temp_min_label = QtWidgets.QLabel(self.tempBox)
        self.temp_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.temp_min_label.setStyleSheet("border:rgb(255,255,255)")
        self.temp_min_label.setObjectName("temp_min_label")
        self.temp_min = QtWidgets.QLineEdit(self.tempBox)
        self.temp_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.temp_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.temp_min.setObjectName("temp_min")
        self.powerBox = QtWidgets.QGroupBox(self.scaleBox)
        self.powerBox.setGeometry(QtCore.QRect(210, 30, 181, 91))
        self.powerBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.powerBox.setObjectName("powerBox")
        self.p_max = QtWidgets.QLineEdit(self.powerBox)
        self.p_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.p_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.p_max.setObjectName("p_max")
        self.p_max_label = QtWidgets.QLabel(self.powerBox)
        self.p_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.p_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_max_label.setObjectName("p_max_label")
        self.p_min_label = QtWidgets.QLabel(self.powerBox)
        self.p_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.p_min_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_min_label.setObjectName("p_min_label")
        self.p_min = QtWidgets.QLineEdit(self.powerBox)
        self.p_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.p_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.p_min.setObjectName("p_min")
        self.timeGBox = QtWidgets.QGroupBox(self.scaleBox)
        self.timeGBox.setGeometry(QtCore.QRect(10, 130, 181, 91))
        self.timeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.timeGBox.setObjectName("timeGBox")
        self.t_max = QtWidgets.QLineEdit(self.timeGBox)
        self.t_max.setGeometry(QtCore.QRect(90, 40, 61, 21))
        self.t_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.t_max.setObjectName("t_max")
        self.t_max_label = QtWidgets.QLabel(self.timeGBox)
        self.t_max_label.setGeometry(QtCore.QRect(30, 40, 51, 21))
        self.t_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.t_max_label.setObjectName("t_max_label")
        self.forceBox = QtWidgets.QGroupBox(self.scaleBox)
        self.forceBox.setGeometry(QtCore.QRect(210, 130, 181, 91))
        self.forceBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceBox.setObjectName("forceBox")
        self.f_max = QtWidgets.QLineEdit(self.forceBox)
        self.f_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.f_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.f_max.setObjectName("f_max")
        self.f_max_label = QtWidgets.QLabel(self.forceBox)
        self.f_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.f_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.f_max_label.setObjectName("f_max_label")
        self.f_min_label = QtWidgets.QLabel(self.forceBox)
        self.f_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.f_min_label.setStyleSheet("border: rgb(255,255,255)")
        self.f_min_label.setObjectName("f_min_label")
        self.f_min = QtWidgets.QLineEdit(self.forceBox)
        self.f_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.f_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.f_min.setObjectName("f_min")
        self.samplingBox = QtWidgets.QGroupBox(self.centralWidget)
        self.samplingBox.setGeometry(QtCore.QRect(150, 250, 121, 71))
        self.samplingBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(255, 83, 0);\n"
"color: rgb(255,255,255);")
        self.samplingBox.setObjectName("samplingBox")
        self.samplingCBox = QtWidgets.QComboBox(self.samplingBox)
        self.samplingCBox.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.samplingCBox.setMouseTracking(False)
        self.samplingCBox.setAutoFillBackground(False)
        self.samplingCBox.setStyleSheet("background-color:rgb(53, 53, 53)\n"
"")
        self.samplingCBox.setObjectName("samplingCBox")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.cronometroBox = QtWidgets.QGroupBox(self.centralWidget)
        self.cronometroBox.setGeometry(QtCore.QRect(10, 330, 401, 201))
        self.cronometroBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(123, 0, 129);")
        self.cronometroBox.setObjectName("cronometroBox")
        self.timerGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.timerGBox.setGeometry(QtCore.QRect(10, 30, 211, 71))
        self.timerGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.timerGBox.setObjectName("timerGBox")
        self.timerLabel = QtWidgets.QLabel(self.timerGBox)
        self.timerLabel.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.timerLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"border: 1px solid rgb(44, 0, 47);\n"
"font: 75 12pt \"Noto Serif\";")
        self.timerLabel.setObjectName("timerLabel")
        self.startTimerButton = QtWidgets.QPushButton(self.timerGBox)
        self.startTimerButton.setGeometry(QtCore.QRect(130, 10, 51, 21))
        self.startTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(44, 0, 47);")
        self.startTimerButton.setObjectName("startTimerButton")
        self.stopTimerButton = QtWidgets.QPushButton(self.timerGBox)
        self.stopTimerButton.setGeometry(QtCore.QRect(130, 40, 51, 21))
        self.stopTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(44, 0, 47);")
        self.stopTimerButton.setObjectName("stopTimerButton")
        self.startTimeGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.startTimeGBox.setGeometry(QtCore.QRect(240, 30, 151, 71))
        self.startTimeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.startTimeGBox.setObjectName("startTimeGBox")
        self.startTimeLabel = QtWidgets.QLabel(self.startTimeGBox)
        self.startTimeLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.startTimeLabel.setStyleSheet("background-color:rgb(80, 80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.currentTimeGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.currentTimeGBox.setGeometry(QtCore.QRect(240, 120, 151, 71))
        self.currentTimeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.currentTimeGBox.setObjectName("currentTimeGBox")
        self.currentTimeLabel = QtWidgets.QLabel(self.currentTimeGBox)
        self.currentTimeLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.currentTimeLabel.setStyleSheet("background-color:rgb(80, 80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.regTimerGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.regTimerGBox.setGeometry(QtCore.QRect(10, 120, 211, 71))
        self.regTimerGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.regTimerGBox.setObjectName("regTimerGBox")
        self.regTimerLabel = QtWidgets.QLineEdit(self.regTimerGBox)
        self.regTimerLabel.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.regTimerLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"border: 1px solid rgb(255,255,255);\n"
"color:rgb(255,255,255);\n"
"font: 75 12pt \"Noto Serif\";")
        self.regTimerLabel.setObjectName("regTimerLabel")
        self.startRegTimerButton = QtWidgets.QPushButton(self.regTimerGBox)
        self.startRegTimerButton.setGeometry(QtCore.QRect(130, 10, 51, 21))
        self.startRegTimerButton.setStyleSheet("border: 1px solid rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.startRegTimerButton.setObjectName("startRegTimerButton")
        self.stopRegTimerButton = QtWidgets.QPushButton(self.cronometroBox)
        self.stopRegTimerButton.setGeometry(QtCore.QRect(140, 160, 51, 21))
        self.stopRegTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(255,255,255);")
        self.stopRegTimerButton.setObjectName("stopRegTimerButton")
        self.prensaNameGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.prensaNameGBox.setGeometry(QtCore.QRect(10, 250, 121, 71))
        self.prensaNameGBox.setStyleSheet("\n"
"border: 1px solid rgb(27, 144, 0);\n"
"background-color: rgb(86, 86, 86);")
        self.prensaNameGBox.setObjectName("prensaNameGBox")
        self.prensaName = QtWidgets.QLineEdit(self.prensaNameGBox)
        self.prensaName.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.prensaName.setStyleSheet("font: 11pt \"Noto Serif\";\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.prensaName.setObjectName("prensaName")
        self.arquivoSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arquivoSalvoLabel.setGeometry(QtCore.QRect(420, 630, 111, 16))
        self.arquivoSalvoLabel.setObjectName("arquivoSalvoLabel")
        self.arqSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arqSalvoLabel.setGeometry(QtCore.QRect(530, 630, 241, 16))
        self.arqSalvoLabel.setObjectName("arqSalvoLabel")
        self.ambientTempGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.ambientTempGBox.setGeometry(QtCore.QRect(290, 250, 121, 71))
        self.ambientTempGBox.setStyleSheet("\n"
"border: 1px solid rgb(255, 243, 0);\n"
"background-color: rgb(86, 86, 86);")
        self.ambientTempGBox.setObjectName("ambientTempGBox")
        self.ambientTempLabel = QtWidgets.QLineEdit(self.ambientTempGBox)
        self.ambientTempLabel.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.ambientTempLabel.setStyleSheet("font: 14pt \"Noto Serif\";\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.ambientTempLabel.setObjectName("ambientTempLabel")
        self.absolValGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.absolValGBox.setGeometry(QtCore.QRect(10, 540, 401, 101))
        self.absolValGBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border: 1px solid rgb(26, 149, 172)")
        self.absolValGBox.setObjectName("absolValGBox")
        self.tempGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.tempGBox.setGeometry(QtCore.QRect(10, 30, 121, 61))
        self.tempGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.tempGBox.setObjectName("tempGBox")
        self.tempLabel = QtWidgets.QLabel(self.tempGBox)
        self.tempLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.tempLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.tempLabel.setObjectName("tempLabel")
        self.powGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.powGBox.setGeometry(QtCore.QRect(270, 30, 121, 61))
        self.powGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.powGBox.setObjectName("powGBox")
        self.powLabel = QtWidgets.QLabel(self.powGBox)
        self.powLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.powLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.powLabel.setObjectName("powLabel")
        self.forceGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.forceGBox.setGeometry(QtCore.QRect(140, 30, 121, 61))
        self.forceGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceGBox.setObjectName("forceGBox")
        self.forceLabel = QtWidgets.QLabel(self.forceGBox)
        self.forceLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.forceLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.forceLabel.setObjectName("forceLabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.menuStatusBar.setObjectName("menuStatusBar")
        MainWindow.setStatusBar(self.menuStatusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.stageMenu = QtWidgets.QMenu(self.menuBar)
        self.stageMenu.setObjectName("stageMenu")
        self.serialMenu = QtWidgets.QMenu(self.menuBar)
        self.serialMenu.setObjectName("serialMenu")
        self.playPauseButton = QtWidgets.QMenu(self.menuBar)
        self.playPauseButton.setObjectName("playPauseButton")
        self.ThermocoupleMenu = QtWidgets.QMenu(self.menuBar)
        self.ThermocoupleMenu.setObjectName("ThermocoupleMenu")
        self.finalizeButton = QtWidgets.QMenu(self.menuBar)
        self.finalizeButton.setObjectName("finalizeButton")
        MainWindow.setMenuBar(self.menuBar)
        self.alternaCalibraP = QtWidgets.QAction(MainWindow)
        self.alternaCalibraP.setObjectName("alternaCalibraP")
        self.alternaCalibraT = QtWidgets.QAction(MainWindow)
        self.alternaCalibraT.setObjectName("alternaCalibraT")
        self.alternaProc = QtWidgets.QAction(MainWindow)
        self.alternaProc.setObjectName("alternaProc")
        self.openButton = QtWidgets.QAction(MainWindow)
        self.openButton.setEnabled(False)
        self.openButton.setIconVisibleInMenu(True)
        self.openButton.setObjectName("openButton")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_Como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Como.setObjectName("actionSalvar_Como")
        self.saveButton = QtWidgets.QAction(MainWindow)
        self.saveButton.setObjectName("saveButton")
        self.saveAsButton = QtWidgets.QAction(MainWindow)
        self.saveAsButton.setObjectName("saveAsButton")
        self.selectPortaUSB = QtWidgets.QAction(MainWindow)
        self.selectPortaUSB.setObjectName("selectPortaUSB")
        self.fileMenu.addAction(self.openButton)
        self.fileMenu.addAction(self.saveButton)
        self.fileMenu.addAction(self.saveAsButton)
        self.stageMenu.addAction(self.alternaCalibraP)
        self.stageMenu.addAction(self.alternaCalibraT)
        self.stageMenu.addAction(self.alternaProc)
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.stageMenu.menuAction())
        self.menuBar.addAction(self.serialMenu.menuAction())
        self.menuBar.addAction(self.ThermocoupleMenu.menuAction())
        self.menuBar.addAction(self.playPauseButton.menuAction())
        self.menuBar.addAction(self.finalizeButton.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADAMAP - Análise de Dados: Etapa 1 - Calibração de Pressão"))
        self.scaleBox.setTitle(_translate("MainWindow", "Escalas de Visualização (Range)"))
        self.tempBox.setTitle(_translate("MainWindow", "Temperatura (ºC)"))
        self.temp_max.setText(_translate("MainWindow", "1000"))
        self.temp_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.temp_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.temp_min.setText(_translate("MainWindow", "100"))
        self.powerBox.setTitle(_translate("MainWindow", "Potência (kW)"))
        self.p_max.setText(_translate("MainWindow", "100"))
        self.p_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.p_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.p_min.setText(_translate("MainWindow", "10"))
        self.timeGBox.setTitle(_translate("MainWindow", "Tempo (s)"))
        self.t_max.setText(_translate("MainWindow", "50"))
        self.t_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.forceBox.setTitle(_translate("MainWindow", "Força (kN)"))
        self.f_max.setText(_translate("MainWindow", "1000"))
        self.f_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.f_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.f_min.setText(_translate("MainWindow", "20"))
        self.samplingBox.setTitle(_translate("MainWindow", "Amostragem"))
        self.samplingCBox.setItemText(0, _translate("MainWindow", "100 mseg"))
        self.samplingCBox.setItemText(1, _translate("MainWindow", "200 mseg"))
        self.samplingCBox.setItemText(2, _translate("MainWindow", "500 mseg"))
        self.samplingCBox.setItemText(3, _translate("MainWindow", "1 seg"))
        self.samplingCBox.setItemText(4, _translate("MainWindow", "1.5 seg"))
        self.samplingCBox.setItemText(5, _translate("MainWindow", "2 seg"))
        self.samplingCBox.setItemText(6, _translate("MainWindow", "2.5 seg"))
        self.samplingCBox.setItemText(7, _translate("MainWindow", "5 seg"))
        self.samplingCBox.setItemText(8, _translate("MainWindow", "10 seg"))
        self.cronometroBox.setTitle(_translate("MainWindow", "Timer"))
        self.timerGBox.setTitle(_translate("MainWindow", "Cronômetro"))
        self.timerLabel.setText(_translate("MainWindow", "0.00 s"))
        self.startTimerButton.setText(_translate("MainWindow", "Iniciar"))
        self.stopTimerButton.setText(_translate("MainWindow", "Parar"))
        self.startTimeGBox.setTitle(_translate("MainWindow", "Horário de Início"))
        self.startTimeLabel.setText(_translate("MainWindow", "16:30:15"))
        self.currentTimeGBox.setTitle(_translate("MainWindow", "Horário Atual"))
        self.currentTimeLabel.setText(_translate("MainWindow", "17:05:56"))
        self.regTimerGBox.setTitle(_translate("MainWindow", "Cont. Regressivo"))
        self.regTimerLabel.setText(_translate("MainWindow", "0.00 s"))
        self.startRegTimerButton.setText(_translate("MainWindow", "Iniciar"))
        self.stopRegTimerButton.setText(_translate("MainWindow", "Parar"))
        self.prensaNameGBox.setTitle(_translate("MainWindow", "Prensa"))
        self.prensaName.setText(_translate("MainWindow", "Pr 400 Tonf"))
        self.arquivoSalvoLabel.setText(_translate("MainWindow", "Arquivo Salvo em:"))
        self.arqSalvoLabel.setText(_translate("MainWindow", "/home/LAPMA/Pressao/1025565.temp"))
        self.ambientTempGBox.setTitle(_translate("MainWindow", "Temp. Ambiente"))
        self.ambientTempLabel.setText(_translate("MainWindow", "    26 ºC"))
        self.absolValGBox.setTitle(_translate("MainWindow", "Valores Absolutos"))
        self.tempGBox.setTitle(_translate("MainWindow", "Temperatura"))
        self.tempLabel.setText(_translate("MainWindow", "42.679 ºC"))
        self.powGBox.setTitle(_translate("MainWindow", "Potência"))
        self.powLabel.setText(_translate("MainWindow", "23.567 kW"))
        self.forceGBox.setTitle(_translate("MainWindow", "Força"))
        self.forceLabel.setText(_translate("MainWindow", "340.34 kN"))
        self.fileMenu.setTitle(_translate("MainWindow", "Arquivo"))
        self.stageMenu.setTitle(_translate("MainWindow", "Etapa"))
        self.serialMenu.setTitle(_translate("MainWindow", "Porta"))
        self.playPauseButton.setTitle(_translate("MainWindow", "Iniciar/Pausar"))
        self.ThermocoupleMenu.setTitle(_translate("MainWindow", "Termopar"))
        self.finalizeButton.setTitle(_translate("MainWindow", "Finalizar"))
        self.alternaCalibraP.setText(_translate("MainWindow", "Calibração P"))
        self.alternaCalibraT.setText(_translate("MainWindow", "Calibração T"))
        self.alternaProc.setText(_translate("MainWindow", "Processamento"))
        self.openButton.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como"))
        self.saveButton.setText(_translate("MainWindow", "Salvar"))
        self.saveAsButton.setText(_translate("MainWindow", "Salvar Como"))
        self.selectPortaUSB.setText(_translate("MainWindow", "Selecionar porta USB"))

