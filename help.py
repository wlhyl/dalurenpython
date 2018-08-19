from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # QtWidgets.QDialog(self,parent)
        self.setWindowTitle("帮助")
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint)
        self.resize(700, 500)
        guaTiLayout = QtWidgets.QVBoxLayout()
        # self.layout=helpLayout
        self.setLayout(guaTiLayout)
        self.guaTiTextBrowser = QtWidgets.QTextBrowser()
        guaTiLayout.addWidget(self.guaTiTextBrowser)
        with open('help/help.html', 'r') as f:
            helpStrings = f.read()
        guaTiFont = QtGui.QFont()
        guaTiFont.setPixelSize(18)
        self.guaTiTextBrowser.setFont(guaTiFont)
        self.guaTiTextBrowser.setHtml(helpStrings)