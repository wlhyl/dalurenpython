from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from shensha import shensha


class ShenShaDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, shiPan=None):
        super().__init__(parent)
        self.setWindowTitle("神煞")
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint)
        self.resize(700, 500)
        guaTiLayout = QtWidgets.QVBoxLayout()
        # self.layout=helpLayout
        self.setLayout(guaTiLayout)
        self.guaTiTextBrowser = QtWidgets.QTextBrowser()
        guaTiLayout.addWidget(self.guaTiTextBrowser)
        guaTiFont = QtGui.QFont()
        guaTiFont.setPixelSize(18)
        self.guaTiTextBrowser.setFont(guaTiFont)

        if shiPan is None:
            self.guaTiTextBrowser.setHtml("查询神煞，请先排盘")
            return

        shenShaJson = {"年": {}, "月": {}, "日": {}}
        shenShaModules = shensha
        shenShaFuns = []
        for attr in (a for a in dir(shenShaModules) if a.startswith('do_')):
            callback = getattr(shenShaModules, attr)
            shenShaFuns.append(callback)
        for fun in shenShaFuns:
            fun(shiPan, shenShaJson)
        guaTiStrings = ""
        for key in shenShaJson:
            s0 = None
            count = 0
            for sh in shenShaJson[key]:
                if s0 is None:
                    s0 = '<span>{}: {}</span>'.format(sh, shenShaJson[key][sh])
                else:
                    if count % 8 == 0:
                        s0 = '{}<br/><span>{}: {}</span>'.format(s0, sh, shenShaJson[key][sh])
                    else:
                        s0 = '{}&nbsp;&nbsp;&nbsp;&nbsp;<span>{}: {}</span>'.format(s0, sh, shenShaJson[key][sh])
#                 if count == 7:
#                     s0 = "{}<br/>".format(s0)
                count = count + 1
            guaTiStrings = "{}<div>{}</div><div>{}</div>".format(guaTiStrings, key, s0)
        self.guaTiTextBrowser.setText(guaTiStrings)