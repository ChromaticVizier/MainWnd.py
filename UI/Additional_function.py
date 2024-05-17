from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel

from GlobalVariable import global_obj

user_list = global_obj.GlobalUserList  # 全局用户表
video_list = global_obj.GlobalVideoList  # 全局视频表

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(310, 10, 581, 441))
        self.listView.setObjectName("listView")


        self.user_cluster = QtWidgets.QPushButton(self.centralwidget)
        self.user_cluster.setGeometry(QtCore.QRect(10, 60, 291, 91))
        self.user_cluster.setStyleSheet("<p>text</p>")
        self.user_cluster.setObjectName("pushButton")


        self.video_cluster = QtWidgets.QPushButton(self.centralwidget)
        self.video_cluster.setGeometry(QtCore.QRect(10, 160, 291, 91))
        self.video_cluster.setObjectName("pushButton_2")


        self.video_predict = QtWidgets.QPushButton(self.centralwidget)
        self.video_predict.setGeometry(QtCore.QRect(10, 260, 291, 91))
        self.video_predict.setObjectName("pushButton_3")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 9, 291, 41))
        self.lineEdit.setObjectName("lineEdit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.user_cluster.clicked.connect(self.user_clu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_cluster.setText(_translate("MainWindow", "用户聚类"))
        self.video_cluster.setText(_translate("MainWindow", "视频聚类"))
        self.video_predict.setText(_translate("MainWindow", "热度推测"))

    def user_clu(self):
        for user in user_list:
            for video_class in user.video_list:
                sum_screen_time = 0
                for video in video_class.video_list:
                    sum_screen_time += video[1]
                user.prefer_list.append(sum_screen_time)

            favourite = max(user.prefer_list)
            global_obj.user_cluster_list[favourite].append(user.uid)

        slm = QStringListModel()
        slm.setStringList(global_obj.user_cluster_list)
        self.listView.setModel(slm)



