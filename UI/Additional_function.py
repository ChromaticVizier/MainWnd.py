from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
#。。。
from GlobalVariable import global_obj

user_list = global_obj.GlobalUserList  # 全局用户表
video_list = global_obj.GlobalVideoList  # 全局视频表

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #大的文本框
        self.listView = QtWidgets.QTextEdit(self.centralwidget)
        self.listView.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                    "font: 18pt \"Adobe Heiti Std\";")

        self.listView.setGeometry(QtCore.QRect(310, 10, 581, 441))
        self.listView.setObjectName("listView")


        #下面是三个按钮
        self.user_cluster = QtWidgets.QPushButton(MainWindow)
        self.user_cluster.setGeometry(QtCore.QRect(10, 60, 291, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.user_cluster.setFont(font)
        self.user_cluster.setStyleSheet("<p>text</p>")
        self.user_cluster.setObjectName("pushButton")


        self.video_cluster = QtWidgets.QPushButton(MainWindow)
        self.video_cluster.setGeometry(QtCore.QRect(10, 160, 291, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.video_cluster.setFont(font)
        self.video_cluster.setObjectName("pushButton_2")


        self.video_predict = QtWidgets.QPushButton(self.centralwidget)
        self.video_predict.setGeometry(QtCore.QRect(10, 260, 291, 91))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.video_predict.setFont(font)
        self.video_predict.setObjectName("pushButton_3")


        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(10, 9, 291, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                    "font: 18pt \"Adobe Heiti Std\";")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graphicsView = QtWidgets.QGraphicsView(MainWindow)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 903, 499))
        self.graphicsView.setStyleSheet("border-image: url(:/imagees/background3.png);")
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView.raise_()
        self.centralwidget.raise_()
        self.listView.raise_()
        self.lineEdit.raise_()
        self.user_cluster.raise_()
        self.video_cluster.raise_()
        self.video_predict.raise_()

        self.retranslateUi(MainWindow)
        self.user_cluster.clicked.connect(self.user_clu)
        self.video_cluster.clicked.connect(self.video_clu)

        self.video_predict.clicked.connect(self.video_pre)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_cluster.setText(_translate("MainWindow", "用户聚类"))
        self.video_cluster.setText(_translate("MainWindow", "视频聚类"))
        self.video_predict.setText(_translate("MainWindow", "热度推测"))

    def user_clu(self):#对于列表中每个用户观看过的视频，video_class是某一类视频的集合（如电视），其中每个视频的
        for user in user_list:
            for video_class in user.video_list:
                sum_screen_time = 0
                for video in video_class:
                    sum_screen_time += video[1]
                user.prefer_list.append(sum_screen_time)

            user.favourite = user.prefer_list.index(max(user.prefer_list))

        query_uid = int(self.lineEdit.text())
        same_hobby_list = []

        for user in user_list:
            # if user.favourite == user_list[query_uid].favourite:
            if user.favourite == user_list[query_uid].favourite and user.favourite != 0:
                same_hobby_list.append(user)

        self.listView.setPlainText(str(same_hobby_list))

    def video_clu(self): #视频聚类，把喜欢看这个视频的用户ID列出来
        video_uid = int(self.lineEdit.text())
        print(video_uid)
        video = video_list[video_uid - 1]
        self.listView.setPlainText(str(video.user_list))




    def video_pre(self):
        video_uid = int(self.lineEdit.text())
        print(video_uid)
        video = video_list[video_uid - 1]
        if video.hot == 1 and len(video.user_list) >= 5:
            # 之后会火
            self.listView.setPlainText("该视频是热点且观看人数较多，之后很可能会火")
        else:
            #可能过时
            self.listView.setPlainText("该视频不是热点或观看人数稀少，之后可能过时")



