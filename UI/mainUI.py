# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Remote-Banking-Brokers\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 362)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:#f0f0f0;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QCheckBox {\n"
"    padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"      background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color:rgb(246, 134, 86);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #ffffff;\n"
"    color: rgb(81,72,65);\n"
"    selection-color:rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color:rgb(81,72,65);    \n"
"    background: #ffffff;\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color:  #1e1d23;    \n"
"    background: #ffffff;\n"
"}\n"
"QDateTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDateEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QFontComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QLabel {\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255,255,255);\n"
"    selection-background-color:rgb(236,116,64);\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QMenuBar {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top:4px;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    padding-top:2px;\n"
"    padding-left:2px;\n"
"    padding-right:2px;\n"
"    border-top-width:2px;\n"
"    border-left-width:2px;\n"
"    border-right-width:2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-style:solid;\n"
"    background-color:rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-style: inset;\n"
"    border-color: rgb(150,150,150);\n"
"    background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style: solid;\n"
"    border-radius:8px;\n"
"    border-width:1px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QPushButton{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    color:rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"     background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"      background: rgb(246, 134, 86);\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-color: rgb(255,150,60);\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"      border-bottom-left-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-bottom-right-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"     height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-bottom-left-radius: 3px;\n"
"      border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color:rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    padding-bottom:2px;\n"
"    padding-top:2px;\n"
"    color:rgb(81,72,65);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(247,246,246);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 270, 306))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.selectAll = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.selectAll.setObjectName("selectAll")
        self.verticalLayout_4.addWidget(self.selectAll)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.insurancePassangers = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.insurancePassangers.setObjectName("insurancePassangers")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.insurancePassangers)
        self.insuranceTravellers = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.insuranceTravellers.setObjectName("insuranceTravellers")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.insuranceTravellers)
        self.insuranceEstate = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.insuranceEstate.setObjectName("insuranceEstate")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.insuranceEstate)
        self.insuranceAuto = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.insuranceAuto.setObjectName("insuranceAuto")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.insuranceAuto)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.autoPayments = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.autoPayments.setObjectName("autoPayments")
        self.verticalLayout_4.addWidget(self.autoPayments)
        self.createAutoPayments = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.createAutoPayments.setObjectName("createAutoPayments")
        self.verticalLayout_4.addWidget(self.createAutoPayments)
        self.foreignTransfer = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.foreignTransfer.setObjectName("foreignTransfer")
        self.verticalLayout_4.addWidget(self.foreignTransfer)
        self.mobileApp = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.mobileApp.setObjectName("mobileApp")
        self.verticalLayout_4.addWidget(self.mobileApp)
        self.brokerAccount = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.brokerAccount.setObjectName("brokerAccount")
        self.verticalLayout_4.addWidget(self.brokerAccount)
        self.news = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.news.setObjectName("news")
        self.verticalLayout_4.addWidget(self.news)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 385, 232))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.percentCredit_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.percentCredit_fiz_SpinBox.setMaximum(100)
        self.percentCredit_fiz_SpinBox.setProperty("value", 100)
        self.percentCredit_fiz_SpinBox.setObjectName("percentCredit_fiz_SpinBox")
        self.gridLayout.addWidget(self.percentCredit_fiz_SpinBox, 13, 1, 1, 1)
        self.depositSum_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.depositSum_fiz_SpinBox.setMaximum(10000000)
        self.depositSum_fiz_SpinBox.setProperty("value", 70000)
        self.depositSum_fiz_SpinBox.setObjectName("depositSum_fiz_SpinBox")
        self.gridLayout.addWidget(self.depositSum_fiz_SpinBox, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setStyleSheet("font: italic 9pt \"Arial\";\n"
"\n"
"font: 8pt \"Arial\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.transferToClient_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.transferToClient_fiz_SpinBox.setMaximum(10000000)
        self.transferToClient_fiz_SpinBox.setObjectName("transferToClient_fiz_SpinBox")
        self.gridLayout.addWidget(self.transferToClient_fiz_SpinBox, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 13, 0, 1, 1)
        self.persentDepozit_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.persentDepozit_fiz_SpinBox.setMaximum(100)
        self.persentDepozit_fiz_SpinBox.setObjectName("persentDepozit_fiz_SpinBox")
        self.gridLayout.addWidget(self.persentDepozit_fiz_SpinBox, 5, 1, 1, 1)
        self.creditSum_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.creditSum_fiz_SpinBox.setMaximum(10000000)
        self.creditSum_fiz_SpinBox.setObjectName("creditSum_fiz_SpinBox")
        self.gridLayout.addWidget(self.creditSum_fiz_SpinBox, 11, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)
        self.transferNumber_fiz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.transferNumber_fiz_SpinBox.setMaximum(10000000)
        self.transferNumber_fiz_SpinBox.setObjectName("transferNumber_fiz_SpinBox")
        self.gridLayout.addWidget(self.transferNumber_fiz_SpinBox, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.sort_fiz = QtWidgets.QComboBox(self.tab)
        self.sort_fiz.setObjectName("sort_fiz")
        self.sort_fiz.addItem("")
        self.sort_fiz.addItem("")
        self.sort_fiz.addItem("")
        self.verticalLayout_2.addWidget(self.sort_fiz)
        self.fizButton = QtWidgets.QPushButton(self.tab)
        self.fizButton.setObjectName("fizButton")
        self.verticalLayout_2.addWidget(self.fizButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 433, 225))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.transfer_biz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.transfer_biz_SpinBox.setObjectName("transfer_biz_SpinBox")
        self.gridLayout_4.addWidget(self.transfer_biz_SpinBox, 11, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 11, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 2)
        self.mounthPayment_biz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.mounthPayment_biz_SpinBox.setMaximum(1000000)
        self.mounthPayment_biz_SpinBox.setProperty("value", 2000)
        self.mounthPayment_biz_SpinBox.setObjectName("mounthPayment_biz_SpinBox")
        self.gridLayout_4.addWidget(self.mounthPayment_biz_SpinBox, 3, 1, 1, 1)
        self.cashInputComission_biz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.cashInputComission_biz_SpinBox.setMaximum(100)
        self.cashInputComission_biz_SpinBox.setSingleStep(1)
        self.cashInputComission_biz_SpinBox.setProperty("value", 100)
        self.cashInputComission_biz_SpinBox.setObjectName("cashInputComission_biz_SpinBox")
        self.gridLayout_4.addWidget(self.cashInputComission_biz_SpinBox, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 4, 0, 1, 1)
        self.cashComission_biz_SpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_3)
        self.cashComission_biz_SpinBox.setMaximum(100)
        self.cashComission_biz_SpinBox.setSingleStep(1)
        self.cashComission_biz_SpinBox.setProperty("value", 100)
        self.cashComission_biz_SpinBox.setObjectName("cashComission_biz_SpinBox")
        self.gridLayout_4.addWidget(self.cashComission_biz_SpinBox, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.scrollArea_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(-13, 0, 235, 280))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_19.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.selectAll_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.selectAll_2.setObjectName("selectAll_2")
        self.verticalLayout_5.addWidget(self.selectAll_2)
        self.mobileTrade_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.mobileTrade_biz.setObjectName("mobileTrade_biz")
        self.verticalLayout_5.addWidget(self.mobileTrade_biz)
        self.trade_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.trade_biz.setObjectName("trade_biz")
        self.verticalLayout_5.addWidget(self.trade_biz)
        self.analitics_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.analitics_biz.setObjectName("analitics_biz")
        self.verticalLayout_5.addWidget(self.analitics_biz)
        self.onlineAccounting_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.onlineAccounting_biz.setObjectName("onlineAccounting_biz")
        self.verticalLayout_5.addWidget(self.onlineAccounting_biz)
        self.cards_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.cards_biz.setObjectName("cards_biz")
        self.verticalLayout_5.addWidget(self.cards_biz)
        self.checkAgents_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkAgents_biz.setObjectName("checkAgents_biz")
        self.verticalLayout_5.addWidget(self.checkAgents_biz)
        self.mobileApp_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.mobileApp_biz.setObjectName("mobileApp_biz")
        self.verticalLayout_5.addWidget(self.mobileApp_biz)
        self.clientSupport_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.clientSupport_biz.setObjectName("clientSupport_biz")
        self.verticalLayout_5.addWidget(self.clientSupport_biz)
        self.personalManager_biz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.personalManager_biz.setObjectName("personalManager_biz")
        self.verticalLayout_5.addWidget(self.personalManager_biz)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.scrollArea_4)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.sort_biz = QtWidgets.QComboBox(self.tab_2)
        self.sort_biz.setObjectName("sort_biz")
        self.sort_biz.addItem("")
        self.sort_biz.addItem("")
        self.gridLayout_3.addWidget(self.sort_biz, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)
        self.bizButton = QtWidgets.QPushButton(self.tab_2)
        self.bizButton.setObjectName("bizButton")
        self.gridLayout_3.addWidget(self.bizButton, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Брокер ДБО"))
        self.label.setText(_translate("MainWindow", "Выберите необходимые Вам услуги:"))
        self.selectAll.setText(_translate("MainWindow", "Выбрать все"))
        self.insurancePassangers.setText(_translate("MainWindow", "Страхование пассажиров"))
        self.insuranceTravellers.setText(_translate("MainWindow", "Страхование путешественников"))
        self.insuranceEstate.setText(_translate("MainWindow", "Страхование недвижимости"))
        self.insuranceAuto.setText(_translate("MainWindow", "Автострахование"))
        self.autoPayments.setText(_translate("MainWindow", "Подключение автоплатежей"))
        self.createAutoPayments.setText(_translate("MainWindow", "Создание автоперевода"))
        self.foreignTransfer.setText(_translate("MainWindow", "Переводы за рубеж"))
        self.mobileApp.setText(_translate("MainWindow", "Наличие мобильного приложения"))
        self.brokerAccount.setText(_translate("MainWindow", "Открытие брокерского счета "))
        self.news.setText(_translate("MainWindow", "Новости системы банка онлайн"))
        self.label_4.setText(_translate("MainWindow", "Макс. необходимый перевод клиенту банка(р.)"))
        self.label_7.setText(_translate("MainWindow", "Укажите подходящие Вам тарифы. "))
        self.label_6.setText(_translate("MainWindow", "Минимально допустимая сумма вклада(р.)"))
        self.label_9.setText(_translate("MainWindow", "Макс. необходимый перевод на карту по номеру тел.(р.)"))
        self.label_2.setText(_translate("MainWindow", "Минимальный процент по кредиту(%)"))
        self.label_3.setText(_translate("MainWindow", "Максимально необходимая сумма кредита (р.)"))
        self.label_8.setText(_translate("MainWindow", "Минимальный процент по вкладу (%)"))
        self.label_5.setText(_translate("MainWindow", "Если данный тариф Вас не интересует, оставьте поле без изменений."))
        self.label_10.setText(_translate("MainWindow", "Сортировать по:"))
        self.sort_fiz.setItemText(0, _translate("MainWindow", "Пользовательскому рейтингу"))
        self.sort_fiz.setItemText(1, _translate("MainWindow", "Кредитным условиям"))
        self.sort_fiz.setItemText(2, _translate("MainWindow", "Условиям по вкладам"))
        self.fizButton.setText(_translate("MainWindow", "Получить рекомендации"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Физические лица"))
        self.label_17.setText(_translate("MainWindow", "Макс. необходимый  перевод на карту физ.лиц(р. в д.)"))
        self.label_11.setText(_translate("MainWindow", "Макс. коммиссия за внесение наличных(%)"))
        self.label_18.setText(_translate("MainWindow", "Макс. допустимая стоимость обслуживания в мес.(р.)"))
        self.label_13.setText(_translate("MainWindow", "\n"
"Укажите подходящие Вам тарифы. "))
        self.label_14.setText(_translate("MainWindow", "Макс. коммиссия за снятие наличных(%)"))
        self.label_12.setText(_translate("MainWindow", "Если данный тариф Вас не интересует, оставьте поле без изменений. "))
        self.label_19.setText(_translate("MainWindow", "Выберите необходимые вам услуги:"))
        self.selectAll_2.setText(_translate("MainWindow", "Выбрать все"))
        self.mobileTrade_biz.setText(_translate("MainWindow", "Мобильный эквайринг"))
        self.trade_biz.setText(_translate("MainWindow", "Торговый эквайринг"))
        self.analitics_biz.setText(_translate("MainWindow", "Финансовая аналитика"))
        self.onlineAccounting_biz.setText(_translate("MainWindow", "Онлайн-бухгалтерия"))
        self.cards_biz.setText(_translate("MainWindow", "Управление корпоративными картами"))
        self.checkAgents_biz.setText(_translate("MainWindow", "Проверка контрагентов"))
        self.mobileApp_biz.setText(_translate("MainWindow", "Наличие мобильного приложения"))
        self.clientSupport_biz.setText(_translate("MainWindow", "Техподдержка клиентов 24/7"))
        self.personalManager_biz.setText(_translate("MainWindow", "Персональный менеджер"))
        self.sort_biz.setItemText(0, _translate("MainWindow", "Пользовательскому рейтингу"))
        self.sort_biz.setItemText(1, _translate("MainWindow", "Стоимости обслуживания"))
        self.label_20.setText(_translate("MainWindow", "Сортировать по:"))
        self.bizButton.setText(_translate("MainWindow", "Получить рекоммендации"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Юридические лица"))
