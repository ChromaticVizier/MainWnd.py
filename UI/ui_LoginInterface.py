# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWnd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ui_UserLogin


import ui_VideoLogin
import ui_Analysis

import Additional_function

class Ui_LoginInterface(object):
    def setupUi(self, LoginInterface):
        LoginInterface.setObjectName("MainWnd")
        LoginInterface.resize(591, 591)
        self.graphicsView = QtWidgets.QGraphicsView(LoginInterface)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 591, 591))
        self.graphicsView.setStyleSheet("border-image: url(:/imagees/background3.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginInterface)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 560, 291))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(180, 180))
        self.pushButton.setStyleSheet("border-image: url(:/imagees/pic2.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.UL = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.UL.setFont(font)
        self.UL.setObjectName("UL")
        self.verticalLayout_5.addWidget(self.UL)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(180, 180))
        self.pushButton_2.setStyleSheet("border-image: url(:/imagees/pic1.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.VL = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.VL.setFont(font)
        self.VL.setObjectName("VL")
        self.verticalLayout_4.addWidget(self.VL)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(180, 180))
        self.pushButton_3.setStyleSheet("border-image: url(:/imagees/pic3.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.Analysis = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.Analysis.setFont(font)
        self.Analysis.setObjectName("Analysis")
        self.verticalLayout_2.addWidget(self.Analysis)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(LoginInterface)
        self.UL.clicked.connect(self.UserLogin) # type: ignore
        self.VL.clicked.connect(self.VideoLogin) # type: ignore
        self.Analysis.clicked.connect(self.AnalysisFun) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginInterface)

    def retranslateUi(self, MainWnd):
        _translate = QtCore.QCoreApplication.translate
        MainWnd.setWindowTitle(_translate("MainWnd", "短视频推荐系统_登录"))
        self.UL.setText(_translate("MainWnd", "用户登录"))
        self.VL.setText(_translate("MainWnd", "视频登录"))
        self.Analysis.setText(_translate("MainWnd", "统计分析"))

    def UserLogin(self):
        self.widget_user = QtWidgets.QWidget()
        self.user_login = ui_UserLogin.Ui_UserLogin()
        self.user_login.setupUi(self.widget_user)
        self.widget_user.show()

    def VideoLogin(self):
        self.widget_video = QtWidgets.QWidget()
        self.video_login = ui_VideoLogin.Ui_VideoLogin()
        self.video_login.setupUi(self.widget_video)
        self.widget_video.show()

    def AnalysisFun(self):
        self.widget_analysis = QtWidgets.QWidget()
        self.analysis = ui_Analysis.Ui_Analysis()
        self.analysis.setupUi(self.widget_analysis)
        self.widget_analysis.show()

        self.widget_additional = QtWidgets.QMainWindow()
        self.additional = Additional_function.Ui_MainWindow()
        self.additional.setupUi(self.widget_additional)
        self.widget_additional.show()

import pic_rc

