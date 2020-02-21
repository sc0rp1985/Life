# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 238)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vboxlayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(1)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.sbWorldSize = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbWorldSize.setMaximum(1000)
        self.sbWorldSize.setDisplayIntegerBase(10)
        self.sbWorldSize.setObjectName("sbWorldSize")
        self.vboxlayout.addWidget(self.sbWorldSize)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)
        self.cbOutType = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbOutType.setObjectName("cbOutType")
        self.cbOutType.addItem("")
        self.cbOutType.addItem("")
        self.vboxlayout.addWidget(self.cbOutType)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.vboxlayout.addWidget(self.label_3)
        self.sbWindowSize = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sbWindowSize.setEnabled(True)
        self.sbWindowSize.setMaximum(10000)
        self.sbWindowSize.setDisplayIntegerBase(10)
        self.sbWindowSize.setObjectName("sbWindowSize")
        self.vboxlayout.addWidget(self.sbWindowSize)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.vboxlayout.addWidget(self.label_4)
        self.dsbDelay = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.dsbDelay.setObjectName("dsbDelay")
        self.vboxlayout.addWidget(self.dsbDelay)
        self.cbRandomInit = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbRandomInit.setChecked(True)
        self.cbRandomInit.setObjectName("cbRandomInit")
        self.vboxlayout.addWidget(self.cbRandomInit)
        self.cbCheckRepeat = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbCheckRepeat.setObjectName("cbCheckRepeat")
        self.vboxlayout.addWidget(self.cbCheckRepeat)
        self.pbRun = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbRun.setObjectName("pbRun")
        self.vboxlayout.addWidget(self.pbRun)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Размер мира"))
        self.label_2.setText(_translate("MainWindow", "Визуализация"))
        self.cbOutType.setItemText(0, _translate("MainWindow", "Консоль"))
        self.cbOutType.setItemText(1, _translate("MainWindow", "Черепаха"))
        self.label_3.setText(_translate("MainWindow", "Размер окна"))
        self.label_4.setText(_translate("MainWindow", "Интервал между поколениями"))
        self.cbRandomInit.setText(_translate("MainWindow", "Рандомная инициализация"))
        self.cbCheckRepeat.setText(_translate("MainWindow", "Проверять поколение на повтор"))
        self.pbRun.setText(_translate("MainWindow", "RUN"))
