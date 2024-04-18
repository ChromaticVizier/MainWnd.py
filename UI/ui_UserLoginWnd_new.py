# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserLoginWnd_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel

class Ui_UserLoginWnd(object):
    def setupUi(self, UserLoginWnd):
        UserLoginWnd.setObjectName("UserLoginWnd")
        UserLoginWnd.resize(900, 800)
        UserLoginWnd.setMinimumSize(QtCore.QSize(900, 800))
        self.listToPlay = QtWidgets.QListWidget(UserLoginWnd)
        self.listToPlay.setGeometry(QtCore.QRect(10, 350, 381, 331))
        self.listToPlay.setMinimumSize(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listToPlay.setFont(font)
        self.listToPlay.setObjectName("listToPlay")
        self.label = QtWidgets.QLabel(UserLoginWnd)
        self.label.setGeometry(QtCore.QRect(480, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 9pt \"黑体\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(UserLoginWnd)
        self.textEdit.setGeometry(QtCore.QRect(580, 20, 221, 61))
        self.textEdit.setStyleSheet("font: 18pt \"Adobe Heiti Std\";")
        self.textEdit.setObjectName("textEdit")
        self.listHistory = QtWidgets.QListView(UserLoginWnd)
        self.listHistory.setGeometry(QtCore.QRect(470, 130, 381, 551))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.listHistory.setFont(font)
        self.listHistory.setObjectName("listHistory")
        self.label_2 = QtWidgets.QLabel(UserLoginWnd)
        self.label_2.setGeometry(QtCore.QRect(600, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 15pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UserLoginWnd)
        self.label_3.setGeometry(QtCore.QRect(110, 310, 151, 51))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Query = QtWidgets.QPushButton(UserLoginWnd)
        self.Query.setGeometry(QtCore.QRect(810, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Query.setFont(font)
        self.Query.setStyleSheet("border-image: url(:/imagees/pic4.png);")
        self.Query.setText("")
        self.Query.setObjectName("Query")
        self.Share = QtWidgets.QPushButton(UserLoginWnd)
        self.Share.setGeometry(QtCore.QRect(400, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Share.setFont(font)
        self.Share.setStyleSheet("border-image: url(:/imagees/pic8.png);")
        self.Share.setText("")
        self.Share.setObjectName("Share")
        self.Comment = QtWidgets.QPushButton(UserLoginWnd)
        self.Comment.setGeometry(QtCore.QRect(400, 90, 61, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Comment.setFont(font)
        self.Comment.setStyleSheet("border-image: url(:/imagees/pic6.png);")
        self.Comment.setText("")
        self.Comment.setObjectName("Comment")
        self.Praise = QtWidgets.QPushButton(UserLoginWnd)
        self.Praise.setGeometry(QtCore.QRect(400, 20, 61, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Praise.setFont(font)
        self.Praise.setStyleSheet("border-image: url(:/imagees/pic5.png);")
        self.Praise.setText("")
        self.Praise.setObjectName("Praise")
        self.Coin = QtWidgets.QPushButton(UserLoginWnd)
        self.Coin.setGeometry(QtCore.QRect(400, 170, 61, 61))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(20)
        self.Coin.setFont(font)
        self.Coin.setStyleSheet("border-image: url(:/imagees/pic7.png);")
        self.Coin.setText("")
        self.Coin.setObjectName("Coin")
        self.graphicsView = QtWidgets.QGraphicsView(UserLoginWnd)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 1, 971, 791))
        self.graphicsView.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(UserLoginWnd)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 20, 381, 281))
        self.graphicsView_2.setStyleSheet("border-image: url(:/imagees/pic9.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(UserLoginWnd)
        self.graphicsView_3.setGeometry(QtCore.QRect(470, 61, 381, 191))
        self.graphicsView_3.setStyleSheet("background-image: url(:/imagees/background4.png);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView.raise_()
        self.textEdit.raise_()
        self.graphicsView_3.raise_()
        self.listToPlay.raise_()
        self.label.raise_()
        self.listHistory.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.Query.raise_()
        self.Share.raise_()
        self.Comment.raise_()
        self.Praise.raise_()
        self.Coin.raise_()
        self.graphicsView_2.raise_()

        self.retranslateUi(UserLoginWnd)
        self.Query.clicked.connect(self.OnQuery)  # type: ignore
        self.Praise.clicked.connect(self.OnPraise)  # type: ignore
        self.Comment.clicked.connect(self.OnComment)  # type: ignore
        self.Share.clicked.connect(self.OnShare)  # type: ignore
        self.Coin.clicked.connect(self.OnCoin)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(UserLoginWnd)

        self.listToPlay.clicked.connect(self.checkPlayItem)
        self.listHistory.clicked.connect(self.checkHistoryItem)

        self.model_play = QStringListModel()
        self.model_history = QStringListModel()

    def retranslateUi(self, UserLoginWnd):
        _translate = QtCore.QCoreApplication.translate
        UserLoginWnd.setWindowTitle(_translate("UserLoginWnd", "用户测试"))
        self.label.setText(_translate("UserLoginWnd", "<html><head/><body><p><span style=\" font-size:18pt; color:#b0b0b0;\">用户ID：</span></p></body></html>"))
        self.label_2.setText(_translate("UserLoginWnd", "<html><head/><body><p><span style=\" color:#ce9738;\">播放历史</span></p></body></html>"))
        self.label_3.setText(_translate("UserLoginWnd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'隶书\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; color:#cea847;\">待播放列表</span></p></body></html>"))
    def OnQuery(self):
        from GlobalVariable import global_obj

        self.query_uid = int(self.textEdit.toPlainText())
        self.cur_user = global_obj.GlobalUserList[self.query_uid]

        self.cur_user.HelpRefreshWeight()
        self.cur_user.RefreshWeight()

        self.playItems = []  # 先清空
        self.HistoryItems = []  # 先清空

        for i, video in enumerate(self.cur_user.to_play_list):
            self.playItems.extend([str(video[0]) + ' ' + str(global_obj.GlobalVideoList[video[0] - 1].name)])
        self.model_play.setStringList(self.playItems)
        self.listToPlay.setModel(self.model_play)

        # 重构历史视频列表
        for video_uid in self.cur_user.history_list:
            self.HistoryItems.extend([str(video_uid) + ' ' + str(global_obj.GlobalVideoList[video_uid - 1].name)])

        self.model_history.setStringList(self.HistoryItems)
        self.listHistory.setModel(self.model_history)

    def checkPlayItem(self, index):
        # 点击项目表示观看
        video_uid = self.cur_user.to_play_list[index.row()][0]
        from GlobalVariable import global_obj
        video = global_obj.GlobalVideoList[video_uid - 1]
        self.cur_video = video  # 保存起来，用于点赞等操作
        video.watch += 1
        video.user_list.append(self.cur_user.uid)  # 存储已观看用户,不去重
        print('%s 观看数 %d ' % (video.name, video.watch))
        self.HistoryItems.extend([str(video.uid) + ' ' + str(video.name)])  # 临时更改
        self.model_history.setStringList(self.HistoryItems)
        self.cur_user.history_list.append(video_uid)  # 更新数据到用户对象，永久更改

        # 更新权重
        self.cur_user.HelpUpdateInitWeight(video.category)

    def checkHistoryItem(self, index):
        print('选择历史: ', index.row())

    def OnPraise(self):
        video = self.cur_video
        video.like += 1
        print('%s 点赞数： %d' % (video.name, video.like))

    def OnComment(self):
        video = self.cur_video
        video.comment += 1
        print('%s 评论数： %d' % (video.name, video.comment))

    def OnShare(self):
        video = self.cur_video
        video.share += 1
        print('%s 分享数： %d' % (video.name, video.share))

    def OnCoin(self):
        video = self.cur_video
        video.coin += 1
        print('%s 投币数： %d' % (video.name, video.coin))

import pic_rc
