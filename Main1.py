from PyQt5 import QtWidgets
import sys

from brokerUI import *

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myapp = BrokerWin()
    myapp.show()
    sys.exit(app.exec_())