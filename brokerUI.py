from PyQt5 import QtWidgets

from дбо import *
from main import *


class BrokerWin(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(1000, 500)
        self.fizButton.clicked.connect(self.sendInputFiz)
        self.bizButton.clicked.connect(self.sendInputBiz)

    def sendInputFiz(self):
        optional_fiz['Осуществление автоплатежей']=self.autoPayments.isChecked()
        optional_fiz['Перевод за рубеж']=self.foreignTransfer.isChecked()
        optional_fiz['Создание автоперевода']=self.createAutoPayments.isChecked()
        optional_fiz['Новости системы банка онлайн']=self.news.isChecked()
        optional_fiz['Автострахование']= self.insuranceAuto.isChecked()
        optional_fiz['Страхование недвижимости']=self.insuranceEstate.isChecked(),
        optional_fiz['Страхование путешественников']= self.insuranceTravellers.isChecked()
        optional_fiz['Страхование пассажиров']=self.insurancePassangers.isChecked()
        optional_fiz['Наличие мобильного приложения']=self.mobileApp.isChecked()
        #optional_fiz['Ведение и планирование личного бюджета']=self.personalBudget.isChecked()
        optional_fiz['Открытие брокерского счета']=self.brokerAccount.isChecked()
        ranked_fiz['Переводы на карту']=self.transferToClient_fiz_SpinBox.value()
        ranked_fiz['Минимальная сумма вклада']= self.depositSum_fiz_SpinBox.value()
        ranked_fiz['Процент по вкладу ']= self.percentCredit_fiz_SpinBox.value()
        ranked_fiz['Сумма кредита']=self.creditSum_fiz_SpinBox.value()
        ranked_fiz['Ставка кредита']= self.percentCredit_fiz_SpinBox.value()
        ranked_fiz['Переводы на карты по номеру телефона']= self.transferNumber_fiz_SpinBox.value()

        choose_necessary('fiz')
        choose_ranked('fiz')

        print(special_sort('По рейтингу'))



    def sendInputBiz(self):
        optional_biz['Мобильное приложение']=self.mobileApp_biz
        optional_biz['Торговый эквайринг']=self.trade_biz
        optional_biz['Мобильный эквайринг']= self.mobileTrade_biz
        optional_biz['Онлайн-бухгалтерия']=self.onlineAccounting_biz
        optional_biz['Проверка контрагентов']=self.checkAgents_biz
        optional_biz['Управление корпоративными картами']=self.cards_biz
        optional_biz['Финансовая аналитика']=self.analitics_biz
        optional_biz['Техподдержка клиентов 24/7']=self.clientSupport_biz
        optional_biz['Персональный менеджер']=self.personalManager_biz
        ranked_biz['Стоимость обслуживания']=self.mounthPayment_biz_SpinBox
        ranked_biz['% за снятие наличных']=self.cashComission_biz_SpinBox
        ranked_biz['% за внесение наличных']=self.cashInputComission_biz_SpinBox
        ranked_biz['Лимит перевода на карту физ.лица']=self.transfer_biz_SpinBox




