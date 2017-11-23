# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/CalibracaoP.ui'
#
# Created: Thu Nov 23 09:19:47 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time


class Ui_MainWindow(object):
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
        self.CentralGraph.setGeometry(QtCore.QRect(420, 10, 931, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CentralGraph.sizePolicy().hasHeightForWidth())
        self.CentralGraph.setSizePolicy(sizePolicy)
        self.CentralGraph.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CentralGraph.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CentralGraph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CentralGraph.setAlignment(QtCore.Qt.AlignCenter)
        self.CentralGraph.setObjectName("CentralGraph")
        self.scaleBox = QtWidgets.QGroupBox(self.centralWidget)
        self.scaleBox.setGeometry(QtCore.QRect(20, 10, 391, 231))
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
        self.forceBox = QtWidgets.QGroupBox(self.scaleBox)
        self.forceBox.setGeometry(QtCore.QRect(10, 30, 181, 101))
        self.forceBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceBox.setObjectName("forceBox")
        self.f_max = QtWidgets.QLineEdit(self.forceBox)
        self.f_max.setGeometry(QtCore.QRect(80, 30, 61, 21))
        self.f_max.setStyleSheet("background-color: rgb(80,80,80);\n"
                                 "color:rgb(255,255,255);")
        self.f_max.setObjectName("f_max")
        self.f_max_label = QtWidgets.QLabel(self.forceBox)
        self.f_max_label.setGeometry(QtCore.QRect(20, 30, 57, 21))
        self.f_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.f_max_label.setObjectName("f_max_label")
        self.f_min_label = QtWidgets.QLabel(self.forceBox)
        self.f_min_label.setGeometry(QtCore.QRect(20, 60, 57, 21))
        self.f_min_label.setStyleSheet("border:rgb(255,255,255)")
        self.f_min_label.setObjectName("f_min_label")
        self.f_min = QtWidgets.QLineEdit(self.forceBox)
        self.f_min.setGeometry(QtCore.QRect(80, 60, 61, 21))
        self.f_min.setStyleSheet("background-color: rgb(80,80,80);\n"
                                 "color:rgb(255,255,255);")
        self.f_min.setObjectName("f_min")
        self.pressureBox = QtWidgets.QGroupBox(self.scaleBox)
        self.pressureBox.setGeometry(QtCore.QRect(200, 30, 181, 101))
        self.pressureBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.pressureBox.setObjectName("pressureBox")
        self.p_max = QtWidgets.QLineEdit(self.pressureBox)
        self.p_max.setGeometry(QtCore.QRect(80, 30, 61, 21))
        self.p_max.setStyleSheet("background-color: rgb(80,80,80);\n"
                                 "color:rgb(255,255,255);")
        self.p_max.setObjectName("p_max")
        self.p_max_label = QtWidgets.QLabel(self.pressureBox)
        self.p_max_label.setGeometry(QtCore.QRect(20, 30, 57, 21))
        self.p_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_max_label.setObjectName("p_max_label")
        self.p_min_label = QtWidgets.QLabel(self.pressureBox)
        self.p_min_label.setGeometry(QtCore.QRect(20, 60, 57, 21))
        self.p_min_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_min_label.setObjectName("p_min_label")
        self.p_min = QtWidgets.QLineEdit(self.pressureBox)
        self.p_min.setGeometry(QtCore.QRect(80, 60, 61, 21))
        self.p_min.setStyleSheet("background-color: rgb(80,80,80);\n"
                                 "color:rgb(255,255,255);")
        self.p_min.setObjectName("p_min")
        self.timeGBox = QtWidgets.QGroupBox(self.scaleBox)
        self.timeGBox.setGeometry(QtCore.QRect(90, 140, 211, 81))
        self.timeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.timeGBox.setObjectName("timeGBox")
        self.t_max = QtWidgets.QLineEdit(self.timeGBox)
        self.t_max.setGeometry(QtCore.QRect(140, 30, 61, 21))
        self.t_max.setStyleSheet("background-color: rgb(80,80,80);\n"
                                 "color:rgb(255,255,255);")
        self.t_max.setObjectName("t_max")
        self.t_max_label = QtWidgets.QLabel(self.timeGBox)
        self.t_max_label.setGeometry(QtCore.QRect(10, 30, 131, 21))
        self.t_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.t_max_label.setObjectName("t_max_label")
        self.samplingBox = QtWidgets.QGroupBox(self.centralWidget)
        self.samplingBox.setGeometry(QtCore.QRect(20, 250, 181, 71))
        self.samplingBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
                                       "border: 1px solid rgb(255, 75, 0);\n"
                                       "color: rgb(255, 255, 255);")
        self.samplingBox.setObjectName("samplingBox")
        self.samplingCBox = QtWidgets.QComboBox(self.samplingBox)
        self.samplingCBox.setGeometry(QtCore.QRect(40, 30, 101, 27))
        self.samplingCBox.setStyleSheet("background-color:rgb(53, 53, 53)")
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
        self.currentTimeBox = QtWidgets.QGroupBox(self.centralWidget)
        self.currentTimeBox.setGeometry(QtCore.QRect(20, 330, 391, 171))
        self.currentTimeBox.setStyleSheet("border:1px solid rgb(123, 0, 129);\n"
                                          "background-color: rgb(86, 86, 86);")
        self.currentTimeBox.setObjectName("currentTimeBox")
        self.startTimerButton = QtWidgets.QPushButton(self.currentTimeBox)
        self.startTimerButton.setGeometry(QtCore.QRect(150, 20, 61, 31))
        self.startTimerButton.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.startTimerButton.setObjectName("startTimerButton")
        self.screenTimerGBox = QtWidgets.QGroupBox(self.currentTimeBox)
        self.screenTimerGBox.setGeometry(QtCore.QRect(10, 30, 120, 131))
        self.screenTimerGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.screenTimerGBox.setObjectName("screenTimerGBox")
        self.screenTimerLabel = QtWidgets.QLabel(self.screenTimerGBox)
        self.screenTimerLabel.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.screenTimerLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
                                            "color:rgb(255,255,255);\n"
                                            "font: 75 12pt \"Noto Serif\";")
        self.screenTimerLabel.setObjectName("screenTimerLabel")
        self.startTimeGBox = QtWidgets.QGroupBox(self.currentTimeBox)
        self.startTimeGBox.setGeometry(QtCore.QRect(230, 10, 151, 71))
        self.startTimeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.startTimeGBox.setObjectName("startTimeGBox")
        self.startTimeLabel = QtWidgets.QLabel(self.startTimeGBox)
        self.startTimeLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.startTimeLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
                                          "color:rgb(255,255,255);\n"
                                          "font: 14pt \"Noto Serif\";")
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.currentTimeGBox = QtWidgets.QGroupBox(self.currentTimeBox)
        self.currentTimeGBox.setGeometry(QtCore.QRect(230, 90, 151, 71))
        self.currentTimeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.currentTimeGBox.setObjectName("currentTimeGBox")
        self.currentTimeLabel = QtWidgets.QLabel(self.currentTimeGBox)
        self.currentTimeLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.currentTimeLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
                                            "color:rgb(255,255,255);\n"
                                            "font: 14pt \"Noto Serif\";")
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.stopTimerButton = QtWidgets.QPushButton(self.currentTimeBox)
        self.stopTimerButton.setGeometry(QtCore.QRect(150, 120, 61, 31))
        self.stopTimerButton.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.stopTimerButton.setObjectName("stopTimerButton")
        self.pauseTimerButton = QtWidgets.QPushButton(self.currentTimeBox)
        self.pauseTimerButton.setGeometry(QtCore.QRect(150, 70, 61, 31))
        self.pauseTimerButton.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.pauseTimerButton.setObjectName("pauseTimerButton")
        self.pressNameGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.pressNameGBox.setGeometry(QtCore.QRect(220, 250, 191, 71))
        self.pressNameGBox.setStyleSheet("border: 1px solid rgb(27, 144, 0);\n"
                                         "background-color: rgb(86, 86, 86);")
        self.pressNameGBox.setObjectName("pressNameGBox")
        self.pressName = QtWidgets.QLineEdit(self.pressNameGBox)
        self.pressName.setGeometry(QtCore.QRect(50, 20, 111, 41))
        self.pressName.setStyleSheet("font: 12pt \"Noto Serif\";\n"
                                     "background-color:rgb(53, 53, 53);\n"
                                     "color:rgb(255,255,255);")
        self.pressName.setObjectName("pressName")
        self.absValGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.absValGBox.setGeometry(QtCore.QRect(20, 510, 391, 111))
        self.absValGBox.setStyleSheet("border: 1px solid rgb(26, 149, 172);\n"
                                      "background-color: rgb(86, 86, 86);")
        self.absValGBox.setObjectName("absValGBox")
        self.forceGBox = QtWidgets.QGroupBox(self.absValGBox)
        self.forceGBox.setGeometry(QtCore.QRect(20, 30, 161, 71))
        self.forceGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceGBox.setObjectName("forceGBox")
        self.forceLabel = QtWidgets.QLabel(self.forceGBox)
        self.forceLabel.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.forceLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
                                      "color:rgb(255,255,255);\n"
                                      "font: 14pt \"Noto Serif\";")
        self.forceLabel.setObjectName("forceLabel")
        self.calibratorGBox = QtWidgets.QGroupBox(self.absValGBox)
        self.calibratorGBox.setGeometry(QtCore.QRect(220, 30, 161, 71))
        self.calibratorGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.calibratorGBox.setObjectName("calibratorGBox")
        self.calibratorLabel = QtWidgets.QLabel(self.calibratorGBox)
        self.calibratorLabel.setGeometry(QtCore.QRect(20, 30, 131, 31))
        self.calibratorLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
                                           "color:rgb(255,255,255);\n"
                                           "font: 14pt \"Noto Serif\";")
        self.calibratorLabel.setObjectName("calibratorLabel")
        self.arquivoSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arquivoSalvoLabel.setGeometry(QtCore.QRect(20, 630, 111, 16))
        self.arquivoSalvoLabel.setObjectName("arquivoSalvoLabel")
        self.arqSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arqSalvoLabel.setGeometry(QtCore.QRect(140, 630, 241, 16))
        self.arqSalvoLabel.setObjectName("arqSalvoLabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuEtapa = QtWidgets.QMenu(self.menuBar)
        self.menuEtapa.setObjectName("menuEtapa")
        self.menuPorta = QtWidgets.QMenu(self.menuBar)
        self.menuPorta.setObjectName("menuPorta")
        MainWindow.setMenuBar(self.menuBar)
        self.menuStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.menuStatusBar.setObjectName("menuStatusBar")
        MainWindow.setStatusBar(self.menuStatusBar)
        self.alternaCalibraP = QtWidgets.QAction(MainWindow)
        self.alternaCalibraP.setObjectName("alternaCalibraP")
        self.alternaCalibraT = QtWidgets.QAction(MainWindow)
        self.alternaCalibraT.setObjectName("alternaCalibraT")
        self.alternaProc = QtWidgets.QAction(MainWindow)
        self.alternaProc.setObjectName("alternaProc")
        self.botaoAbrir = QtWidgets.QAction(MainWindow)
        self.botaoAbrir.setIconVisibleInMenu(True)
        self.botaoAbrir.setObjectName("botaoAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_Como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Como.setObjectName("actionSalvar_Como")
        self.botaoSalvar = QtWidgets.QAction(MainWindow)
        self.botaoSalvar.setObjectName("botaoSalvar")
        self.botaoSalvarComo = QtWidgets.QAction(MainWindow)
        self.botaoSalvarComo.setObjectName("botaoSalvarComo")
        self.selectPortaUSB = QtWidgets.QAction(MainWindow)
        self.selectPortaUSB.setObjectName("selectPortaUSB")
        self.menuArquivo.addAction(self.botaoAbrir)
        self.menuArquivo.addAction(self.botaoSalvar)
        self.menuArquivo.addAction(self.botaoSalvarComo)
        self.menuEtapa.addAction(self.alternaCalibraP)
        self.menuEtapa.addAction(self.alternaCalibraT)
        self.menuEtapa.addAction(self.alternaProc)
        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuBar.addAction(self.menuEtapa.menuAction())
        self.menuBar.addAction(self.menuPorta.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuPlay_Pause = QtWidgets.QAction(MainWindow)
        self.menuPlay_Pause.setText("Play")
        self.menuPlay_Pause.setObjectName("menuPlay_Pause")
        self.menuBar.addAction(self.menuPlay_Pause)
        self.menuPlay_Pause.setCheckable(True)

        self.menuPlay_Pause.toggled.connect(self.playPauseButtonAnimation)

        self.pauseTimerButton.setText("Iniciar")
        self.screenTimerFlag = False
        self.startTimerButton.pressed.connect(self.startScreenTimer)
        self.stopTimerButton.pressed.connect(self.stopScreenTimer)
        self.pauseTimerButton.pressed.connect(self.playPauseScreenTimer)
        self.currentTimer = QtCore.QTimer()
        self.currentTimer.timeout.connect(self.updateCurrentTime)
        self.currentTimer.start(500)

        self.screenTimerFlag = False
        self.retranslateUi(MainWindow)

    def sceneSelector(self, scene):
        self.CentralGraph.setScene(scene)
        self.CentralGraph.setBackgroundBrush(QtCore.Qt.black)
        self.CentralGraph.setInteractive(False)

    def serialListPanel(self, seriaList):
        self.usb = []
        for i in range(0, len(seriaList)):
            self.usb.append(QtWidgets.QAction(self.MainWindow))
            self.usb[i].setText(seriaList[i].device)
            self.usb[i].setCheckable(True)
            self.menuPorta.addAction(self.usb[i])

    def playPauseButtonAnimation(self):
        if (self.menuPlay_Pause.text() == "Play"):
            self.menuPlay_Pause.setText("Pause")
            self.startTimeLabel.setText(self.currentTimeLabel.text())
        else:
            self.menuPlay_Pause.setText("Play")

    def startScreenTimer(self):
        self.timeValue = 0
        self.screenTimer = QtCore.QTimer()
        self.screenTimer.timeout.connect(self.updateScreenTimer)
        self.screenTimer.start(100)
        self.startTimerButton.setText("Reiniciar")
        self.pauseTimerButton.setText("Pausar")
        self.screenTimerFlag = True

    def playPauseScreenTimer(self):
        self.startTimerButton.setText("Reiniciar")
        if (self.pauseTimerButton == "Iniciar"):
            self.startScreenTimer()
        if (self.screenTimerFlag == True):
            self.screenTimer.stop()
            self.screenTimerFlag = False
            self.pauseTimerButton.setText("Continuar")
        else:
            try:
                self.screenTimer.start(100)
                self.screenTimerFlag = True
                self.pauseTimerButton.setText("Pausar")
            except:
                self.startScreenTimer()

    def stopScreenTimer(self):
        self.screenTimer.stop()
        self.screenTimerLabel.setText("0.00 seg")
        self.timeValue = 0
        self.screenTimerFlag = False
        self.startTimerButton.setText("Iniciar")
        self.pauseTimerButton.setText("Iniciar")

    def updateScreenTimer(self):
        self.timeValue += 0.1
        self.screenTimerLabel.setText("%.1f seg" % self.timeValue)

    def updateCurrentTime(self):
        self.currentTime = (str(datetime.now().time()))
        self.currentTime = self.currentTime.split(":", 4)
        self.currentTime[2] = self.currentTime[2].split(".", 3)
        self.currentTimeLabel.setText("%s:%s:%s" % (self.currentTime[0], self.currentTime[1], self.currentTime[2][0]))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "SADAMAP - Análise de Dados: Etapa 1 - Calibração de Pressão"))
        self.scaleBox.setTitle(_translate("MainWindow", "Escalas de Visualização (Range)"))
        self.forceBox.setTitle(_translate("MainWindow", "Força"))
        self.f_max.setText(_translate("MainWindow", "32700"))
        self.f_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.f_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.f_min.setText(_translate("MainWindow", "0"))
        self.pressureBox.setTitle(_translate("MainWindow", "Tensão no Calibrante"))
        self.p_max.setText(_translate("MainWindow", "32700"))
        self.p_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.p_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.p_min.setText(_translate("MainWindow", "0"))
        self.timeGBox.setTitle(_translate("MainWindow", "Tempo"))
        self.t_max.setText(_translate("MainWindow", "100"))
        self.t_max_label.setText(_translate("MainWindow", "Intervalo (amostras):"))
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
        self.currentTimeBox.setTitle(_translate("MainWindow", "Timer"))
        self.startTimerButton.setText(_translate("MainWindow", "Iniciar"))
        self.screenTimerGBox.setTitle(_translate("MainWindow", "Cronômetro"))
        self.screenTimerLabel.setText(_translate("MainWindow", "0 seg"))
        self.startTimeGBox.setTitle(_translate("MainWindow", "Horário de Início"))
        self.startTimeLabel.setText(_translate("MainWindow", "00:00:00"))
        self.currentTimeGBox.setTitle(_translate("MainWindow", "Horário Atual"))
        self.currentTimeLabel.setText(_translate("MainWindow", "00:00:00"))
        self.stopTimerButton.setText(_translate("MainWindow", "Parar"))
        self.pauseTimerButton.setText(_translate("MainWindow", "Pausar"))
        self.pressNameGBox.setTitle(_translate("MainWindow", "Prensa"))
        self.pressName.setText(_translate("MainWindow", "Pr 400 Tonf"))
        self.absValGBox.setTitle(_translate("MainWindow", "Valores Absolutos"))
        self.forceGBox.setTitle(_translate("MainWindow", "Força"))
        self.forceLabel.setText(_translate("MainWindow", "0 Tonf"))
        self.calibratorGBox.setTitle(_translate("MainWindow", "Tensão no Calibrante"))
        self.calibratorLabel.setText(_translate("MainWindow", "0 mV"))
        self.arquivoSalvoLabel.setText(_translate("MainWindow", "Arquivo Salvo em:"))
        self.arqSalvoLabel.setText(_translate("MainWindow", "/home/LAPMA/Pressao/1025565.pre"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuEtapa.setTitle(_translate("MainWindow", "Etapa"))
        self.menuPorta.setTitle(_translate("MainWindow", "Porta"))
        self.alternaCalibraP.setText(_translate("MainWindow", "Calibração P"))
        self.alternaCalibraT.setText(_translate("MainWindow", "Calibração T"))
        self.alternaProc.setText(_translate("MainWindow", "Processamento"))
        self.botaoAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaoSalvarComo.setText(_translate("MainWindow", "Salvar Como"))
        self.selectPortaUSB.setText(_translate("MainWindow", "Selecionar porta USB"))
