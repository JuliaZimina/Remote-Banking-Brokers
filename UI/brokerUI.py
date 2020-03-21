from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QFileDialog
from PyQt5.QtCore import  Qt
from pandas.tests.io.excel.test_xlrd import xlwt

from UI.resultWinUI import *
from algorithm import *
from UI.mainWinUI import *


class BrokerWin(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(1100, 540)
        self.fizButton.clicked.connect(self.sendInputFiz)
        self.bizButton.clicked.connect(self.sendInputBiz)
        self.selectAll.clicked.connect(self.selectAllFiz)
        self.selectAll_2.clicked.connect(self.selectAllBiz)

    def sendInputFiz(self):
        banks.clear()
        black_list.clear()
        optional_fiz['Осуществление автоплатежей'] = self.autoPayments.isChecked()
        optional_fiz['Перевод за рубеж'] = self.foreignTransfer.isChecked()
        optional_fiz['Создание автоперевода'] = self.createAutoPayments.isChecked()
        optional_fiz['Новости системы банка онлайн'] = self.news.isChecked()
        optional_fiz['Автострахование'] = self.insuranceAuto.isChecked()
        optional_fiz['Страхование недвижимости'] = self.insuranceEstate.isChecked()
        optional_fiz['Страхование путешественников'] = self.insuranceTravellers.isChecked()
        optional_fiz['Страхование пассажиров'] = self.insurancePassangers.isChecked()
        optional_fiz['Наличие мобильного приложения'] = self.mobileApp.isChecked()
        optional_fiz['Открытие брокерского счета'] = self.brokerAccount.isChecked()
        ranked_fiz['Переводы на карту'] = self.transferToClient_fiz_SpinBox.value()
        ranked_fiz['Минимальная сумма вклада'] = self.depositSum_fiz_SpinBox.value()
        ranked_fiz['Процент по вкладу '] = self.persentDepozit_fiz_SpinBox.value()
        ranked_fiz['Сумма кредита'] = self.creditSum_fiz_SpinBox.value()
        ranked_fiz['Ставка кредита'] = self.percentCredit_fiz_SpinBox.value()
        ranked_fiz['Переводы на карты по номеру телефона'] = self.transferNumber_fiz_SpinBox.value()

        choose_necessary('fiz')
        choose_ranked('fiz')
        kind_of_sort = self.sort_fiz.currentText()
        # self.close()
        if kind_of_sort == "Пользовательскому рейтингу":
            self.Open = ResultWin("По рейтингу")
        elif kind_of_sort == "Кредитным условиям":
            self.Open = ResultWin("по кредиту")
        elif kind_of_sort == "Условиям по вкладам":
            self.Open = ResultWin("по вкладу")
        self.Open.show()

        # print(special_sort('По рейтингу'))


    def sendInputBiz(self):
        banks.clear()
        black_list.clear()
        optional_biz['Мобильное приложение'] = self.mobileApp_biz.isChecked()
        optional_biz['Торговый эквайринг'] = self.trade_biz.isChecked()
        optional_biz['Мобильный эквайринг'] = self.mobileTrade_biz.isChecked()
        optional_biz['Онлайн-бухгалтерия'] = self.onlineAccounting_biz.isChecked()
        optional_biz['Проверка контрагентов'] = self.checkAgents_biz.isChecked()
        optional_biz['Управление корпоративными картами'] = self.cards_biz.isChecked()
        optional_biz['Финансовая аналитика'] = self.analitics_biz.isChecked()
        optional_biz['Техподдержка клиентов 24/7'] = self.clientSupport_biz.isChecked()
        optional_biz['Персональный менеджер'] = self.personalManager_biz.isChecked()
        ranked_biz['Стоимость обслуживания'] = self.mounthPayment_biz_SpinBox.value()
        ranked_biz['% за снятие наличных'] = self.cashComission_biz_SpinBox.value()
        ranked_biz['% за внесение наличных'] = self.cashInputComission_biz_SpinBox.value()
        ranked_biz['Лимит перевода на карту физ.лица'] = self.transfer_biz_SpinBox.value()

        choose_necessary('biz')
        choose_ranked('biz')
        kind_of_sort = self.sort_biz.currentText()
        # self.close()
        if kind_of_sort == "Пользовательскому рейтингу":
            self.Open = ResultWin("По рейтингу")
        elif kind_of_sort == "Стоимости обслуживания":
            self.Open = ResultWin("По обслуживанию в месяц")
        self.Open.show()

    def selectAllFiz(self):
        self.autoPayments.setChecked(True)
        self.foreignTransfer.setChecked(True)
        self.createAutoPayments.setChecked(True)
        self.news.setChecked(True)
        self.insuranceAuto.setChecked(True)
        self.insuranceEstate.setChecked(True)
        self.insuranceTravellers.setChecked(True)
        self.insurancePassangers.setChecked(True)
        self.mobileApp.setChecked(True)
        self.brokerAccount.setChecked(True)

    def selectAllBiz(self):
        self.mobileApp_biz.setChecked(True)
        self.trade_biz.setChecked(True)
        self.mobileTrade_biz.setChecked(True)
        self.onlineAccounting_biz.setChecked(True)
        self.checkAgents_biz.setChecked(True)
        self.cards_biz.setChecked(True)
        self.analitics_biz.setChecked(True)
        self.clientSupport_biz.setChecked(True)
        self.personalManager_biz.setChecked(True)


class ResultWin(Ui_ResultWindow, QtWidgets.QMainWindow):

    def __init__(self, type_of_sort, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(930, 900)
        self.type_of_sort = type_of_sort
        self.showResult()
    def showResult(self):
        result = special_sort(self.type_of_sort)
        i = 0
        self.sites=[]
        information = pd.read_csv("files/banks_info.csv", encoding="cp1251", sep=";")
        for key in result.keys():
            for bank in result[key]:
                self.tableWidget.insertRow(i)
                label = QLabel()
                item = QTableWidgetItem(str(key))
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(i, 0, item)
                self.tableWidget.setItem(i, 1, QTableWidgetItem(bank))
                self.sites.append(information[bank][0])
                label.setText('<a href="'+information[bank][0]+'">'+information[bank][0]+'</a>')
                label.setOpenExternalLinks(True)
                self.tableWidget.setCellWidget(i, 2, label)
                self.tableWidget.setItem(i, 3, QTableWidgetItem(information[bank][1]))
                item=QTableWidgetItem(information[bank][2])
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(i, 4, item)
                item = QTableWidgetItem(information[bank][3])
                item.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(i, 5, item)
                i += 1
        self.tableWidget.resizeColumnsToContents()
        self.importButton.clicked.connect(self.savefile)
        style = "::section {""background-color: #ffc02b; font:10pt; }"
        self.tableWidget.horizontalHeader().setStyleSheet(style)

    def savefile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        style = xlwt.XFStyle()

        model = self.tableWidget.model()
        for c in range(model.columnCount()):
            text = model.headerData(c, QtCore.Qt.Horizontal)
            sheet.write(0, c , text, style=style)

        for c in range(model.columnCount()):
            for r in range(model.rowCount()):
                text = model.data(model.index(r, c))
                sheet.write(r + 1, c, text)
        for r in range(model.rowCount()):
            text = self.sites[r]
            sheet.write(r + 1, 2, text)

        wbk.save(filename)
