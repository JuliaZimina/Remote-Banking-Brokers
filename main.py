from UI.brokerUI import *

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myapp = BrokerWin()
    myapp.show()
    sys.exit(app.exec_())