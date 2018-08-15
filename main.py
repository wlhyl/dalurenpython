import sys
from PyQt5 import QtWidgets
from DaLuRenWindow import DaLuRenWindow

# Create application
app = QtWidgets.QApplication(sys.argv)
window = DaLuRenWindow()
window.show()
app.exec()
