# coding=utf-8
import os.path
import sys


sys.path.append(os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "."))  # 配置项目路径变量

import IO
import time
from PyQt5 import QtWidgets

from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


import ui_welcome
import ui_LoginInterface

#////////////////

#import welcome
import ui_LoginInterface
from CreateUsers import CreateUsers
import configparser

# push test

def close_welcome(thread1, thread2, wnd):  # 等待准备工作完成然后关闭欢迎窗口
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    wnd.close()


if __name__ == '__main__':
    # 准备工作，启动线程
    t1 = time.time()
    import threading

    th1 = threading.Thread(target=IO.ReadFromFile, args=())
    th2 = threading.Thread(target=CreateUsers, args=())

    app = QtWidgets.QApplication(sys.argv)
    widget_wel = QtWidgets.QWidget()

    th3 = threading.Thread(target=close_welcome, args=(th1, th2, widget_wel))

    welcome_wnd = ui_welcome.Ui_Welcome()
    welcome_wnd.setupUi(widget_wel)
    widget_wel.show()

    th3.start()
    app.exec_()  # 为欢迎页启动消息循环

    t2 = time.time()
    print('程序准备时间：%s ms' % ((t2 - t1) * 1000))

    #  进入主界面
    widget = QtWidgets.QWidget()
    loginInterface = ui_LoginInterface.Ui_LoginInterface()
    loginInterface.setupUi(widget)
    widget.show()

    exit_code = app.exec_()

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('../Setting.ini')
    if int(config['AutoSave']['default']) == 1:
        print('开始写文件')
        IO.SaveToFile()
        print('程序退出')
    sys.exit(exit_code)  # 为主界面启动消息循环
