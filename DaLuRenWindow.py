import datetime
from functools import wraps
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
from shipan.shipan import ShiPan, MinGPan

from common import GetShiChen, GetLi, DiZHiList
from help import HelpDialog
from shensha.ShenShaDialog import ShenShaDialog


def checkValue(func):
    @wraps(func)
    def wrapper(self):
        year = int("0{}".format(self.yearInput.text()))
        month = int("0{}".format(self.monthInput.text()))
        day = int("0{}".format(self.dayInput.text()))
        hour = int("0{}".format(self.hourInput.text()))
        minutes = int("0{}".format(self.minutesInput.text()))
        second = int("0{}".format(self.secondInput.text()))
        shengNian = int("0{}".format(self.shengNianInput.text()))
        if year < 1 or year > 2100 or \
                shengNian < 1920 or shengNian > 2100 or \
                month < 1 or month > 12 or \
                day < 1 or day > 31 or \
                hour < 0 or hour > 23 or \
                minutes < 0 or minutes > 59 or \
                second < 0 or second > 59:
            QtWidgets.QMessageBox.information(None, "OK", "输入时间不正确",
                                              QtWidgets.QMessageBox.Ok,
                                              QtWidgets.QMessageBox.Ok)
            return
        timeString = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(
            year, month, day, hour, minutes, second)
        try:
            datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            QtWidgets.QMessageBox.information(None,
                                              "OK", "输入时间{}不正确".format(
                                                  timeString),
                                              QtWidgets.QMessageBox.Ok,
                                              QtWidgets.QMessageBox.Ok)
            return
        return func(self)
    return wrapper


class DaLuRenWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.shiPan = None
        self.setWindowTitle("大六壬")

        # Create mainold layout
        layout = QtWidgets.QHBoxLayout()

        mainWidget = QtWidgets.QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        self.textBrowser = QWebEngineView()
        layout.addWidget(self.textBrowser)

        # 设置右则面板
        rightWidget = QtWidgets.QWidget()
        rightWidget.setFixedWidth(100)
#         layout.addWidget(rightWidget)
        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setFixedWidth(120)
        scrollArea.setWidgetResizable(True)

#         scroll_bar = scrollArea.verticalScrollBar()
        scrollArea.setWidget(rightWidget)
        layout.addWidget(scrollArea)

        # 为右则面板使用水平布局
        rightVBoxLayout = QtWidgets.QVBoxLayout()
        rightWidget.setLayout(rightVBoxLayout)
#
        self.yearInput = QtWidgets.QLineEdit()
        self.yearInput.setPlaceholderText("年 1920-2050")
        self.yearInput.setValidator(QtGui.QIntValidator(1920, 2050,
                                                        self.yearInput))
        rightVBoxLayout.addWidget(self.yearInput)

        self.monthInput = QtWidgets.QLineEdit()
        self.monthInput.setPlaceholderText("月")
        self.monthInput.setValidator(QtGui.QIntValidator(1, 12,
                                                         self.monthInput))
        rightVBoxLayout.addWidget(self.monthInput)

        self.dayInput = QtWidgets.QLineEdit()
        self.dayInput.setPlaceholderText("日")
        self.dayInput.setValidator(QtGui.QIntValidator(1, 31, self.dayInput))
        rightVBoxLayout.addWidget(self.dayInput)

        self.hourInput = QtWidgets.QLineEdit()
        self.hourInput.setPlaceholderText("时")
        self.hourInput.setValidator(QtGui.QIntValidator(0, 23, self.hourInput))
        rightVBoxLayout.addWidget(self.hourInput)

        self.minutesInput = QtWidgets.QLineEdit()
        self.minutesInput.setPlaceholderText("分")
        self.minutesInput.setValidator(QtGui.QIntValidator(0, 59,
                                                           self.minutesInput))
        rightVBoxLayout.addWidget(self.minutesInput)

        self.secondInput = QtWidgets.QLineEdit()
        self.secondInput.setPlaceholderText("秒")
        self.secondInput.setValidator(QtGui.QIntValidator(0, 59,
                                                          self.minutesInput))
        rightVBoxLayout.addWidget(self.secondInput)

        timeNowButton = QtWidgets.QPushButton("当前时间")
        rightVBoxLayout.addWidget(timeNowButton)

        self.yueJiang = QtWidgets.QComboBox()
        self.yueJiang.addItems(DiZHiList)

        yueJiangHBoxLayout = QtWidgets.QHBoxLayout()
        yueJiangHBoxLayout.addWidget(QtWidgets.QLabel("月将"))
        yueJiangbutton = QtWidgets.QPushButton("计算")
        yueJiangHBoxLayout.addWidget(yueJiangbutton)
        rightVBoxLayout.addLayout(yueJiangHBoxLayout)
        rightVBoxLayout.addWidget(self.yueJiang)

        self.zhanShi = QtWidgets.QComboBox()
        self.zhanShi.addItems(DiZHiList)
        rightVBoxLayout.addWidget(QtWidgets.QLabel("占时"))
        rightVBoxLayout.addWidget(self.zhanShi)

        self.zhouZhan = QtWidgets.QComboBox()
        self.zhouZhan.addItems(["是", "否"])
        rightVBoxLayout.addWidget(QtWidgets.QLabel("昼占/昼生人"))
        rightVBoxLayout.addWidget(self.zhouZhan)

        self.mingJu = QtWidgets.QComboBox()
        self.mingJu.addItems(["否", "是"])
        rightVBoxLayout.addWidget(QtWidgets.QLabel("命局"))
        rightVBoxLayout.addWidget(self.mingJu)

        man = QtWidgets.QRadioButton("男")
        male = QtWidgets.QRadioButton("女")
        man.setChecked(True)
        self.sex = QtWidgets.QButtonGroup()
        self.sex.addButton(man, 0)
        self.sex.addButton(male, 1)
        sexLayout = QtWidgets.QHBoxLayout()
        sexLayout.addWidget(man)
        sexLayout.addWidget(male)
        rightVBoxLayout.addLayout(sexLayout)

        self.shengNianInput = QtWidgets.QLineEdit()
        self.shengNianInput.setPlaceholderText("生年")
        self.shengNianInput.setValidator(
            QtGui.QIntValidator(1920, 2050, self.shengNianInput))
        rightVBoxLayout.addWidget(self.shengNianInput)

        rightVBoxLayout.addWidget(QtWidgets.QLabel("占测之事"))
        self.占测的事Input = QtWidgets.QLineEdit()
        rightVBoxLayout.addWidget(self.占测的事Input)

        button = QtWidgets.QPushButton("起六壬局")
        rightVBoxLayout.addWidget(button)

        shenShaButton = QtWidgets.QPushButton("神煞查询")
        rightVBoxLayout.addWidget(shenShaButton)

        helpButton = QtWidgets.QPushButton("帮助")
        rightVBoxLayout.addWidget(helpButton)
        rightVBoxLayout.addStretch()

        # 设置默认时间
        self.timeNow()

        月将 = GetLi(int(self.yearInput.text()), int(self.monthInput.text()),
                   int(self.dayInput.text()), int(self.hourInput.text()),
                   int(self.minutesInput.text()),
                   int(self.secondInput.text()))[4]
        self.yueJiang.setCurrentIndex(月将.num - 1)
        button.clicked.connect(self.onclick)
        helpButton.clicked.connect(self.helpOnclick)
        yueJiangbutton.clicked.connect(self.yueJiangOnClick)
        shenShaButton.clicked.connect(self.shenShaOnclick)
        timeNowButton.clicked.connect(self.timeNowOnClick)
#         self.show()

    # Connect event for button
    @checkValue
    def onclick(self):
        year = int("0{}".format(self.yearInput.text()))
        month = int("0{}".format(self.monthInput.text()))
        day = int("0{}".format(self.dayInput.text()))
        hour = int("0{}".format(self.hourInput.text()))
        minutes = int("0{}".format(self.minutesInput.text()))
        second = int("0{}".format(self.secondInput.text()))
        shengNian = int("0{}".format(self.shengNianInput.text()))
        月将=DiZHiList[self.yueJiang.currentIndex()]
        占时=DiZHiList[self.zhanShi.currentIndex()]
        昼占=True
        __占测的事 = self.占测的事Input.text()
        if self.zhouZhan.currentIndex() == 1:
            昼占=False
        命局=False
        if self.mingJu.currentIndex() == 1:
            命局 = True
        性别 = self.sex.checkedId()
        if 命局:
            s = MinGPan(year, month, day, hour, minutes, second, 月将, 占时, 昼占,
                        __占测的事, 性别, shengNian)
        else:
            s = ShiPan(year, month, day, hour, minutes, second, 月将, 占时, 昼占,
                       __占测的事, 性别, shengNian)
        self.textBrowser.setHtml(s.toHml)
        self.shiPan = s

    @checkValue
    def yueJiangOnClick(self):
        year = int("0{}".format(self.yearInput.text()))
        month = int("0{}".format(self.monthInput.text()))
        day = int("0{}".format(self.dayInput.text()))
        hour = int("0{}".format(self.hourInput.text()))
        minutes = int("0{}".format(self.minutesInput.text()))
        second = int("0{}".format(self.secondInput.text()))
        __月将 = GetLi(year, month, day, hour, minutes, second)[4]
        self.yueJiang.setCurrentIndex(__月将.num - 1)
        __占时 = GetShiChen(int(self.hourInput.text()))
        self.zhanShi.setCurrentIndex(__占时.num - 1)

    def helpOnclick(self):
        # return
        helpDialog = HelpDialog(self)
        # helpDialog.setWindowTitle("帮助")
        # helpDialog.exec_()
        helpDialog.show()

    def shenShaOnclick(self):
        # return
        shenShaDialog = ShenShaDialog(self, self.shiPan)
        shenShaDialog.show()

    def timeNowOnClick(self):
        self.timeNow()

    def timeNow(self):
        nowDateTime = datetime.datetime.today()
        self.yearInput.setText("{}".format(nowDateTime.year))
        self.monthInput.setText("{}".format(nowDateTime.month))
        self.dayInput.setText("{}".format(nowDateTime.day))
        self.hourInput.setText("{}".format(nowDateTime.hour))
        self.minutesInput.setText("{}".format(nowDateTime.minute))
        self.secondInput.setText("{}".format(nowDateTime.second))
        self.shengNianInput.setText("{}".format(nowDateTime.year))
        __占时 = GetShiChen(nowDateTime.hour)
#         self.zhanShi.setCurrentIndex(GetShiChen(int(self.hourInput.text())).num
#                              - 1)
        self.zhanShi.setCurrentIndex(__占时.num - 1)
