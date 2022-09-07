import time
from json import dumps

from httplib2 import Http
from colorama import Fore, Back, Style
from PyQt5 import QtCore, QtGui, QtWidgets
# -*- coding: utf-8 -*-

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 306)
        self.run = QtWidgets.QDialogButtonBox(Dialog)
        self.run.setGeometry(QtCore.QRect(410, 260, 171, 32))
        self.run.setAccessibleName("")
        self.run.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run.setOrientation(QtCore.Qt.Horizontal)
        self.run.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.run.setObjectName("run")
        self.message = QtWidgets.QTextEdit(Dialog)
        self.message.setGeometry(QtCore.QRect(20, 120, 561, 61))
        self.message.setObjectName("message")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 240, 561, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.text = QtWidgets.QLabel(Dialog)
        self.text.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.text.setObjectName("text")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 210, 561, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.URL = QtWidgets.QLabel(Dialog)
        self.URL.setGeometry(QtCore.QRect(20, 190, 151, 16))
        self.URL.setObjectName("URL")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 551, 71))
        self.label.setObjectName("label")
        self.runfinal = QtWidgets.QPushButton(Dialog)
        self.runfinal.setGeometry(QtCore.QRect(20, 260, 113, 32))
        self.runfinal.setObjectName("runfinal")
        self.runfinal.clicked.connect(lambda: self.showLine())
        self.retranslateUi(Dialog)
        self.run.accepted.connect(Dialog.accept) # type: ignore
        self.run.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def showLine(self):
        print(Fore.YELLOW + "Message to send:" + self.message.toPlainText())
        self.progressBar.setValue(14)
        url = self.textEdit_2.toPlainText()
        print(f"{Fore.GREEN}Webhook URL: {url}")
        message = self.message.toPlainText()
        message = {'text': message}
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.progressBar.setValue(36)
        http_obj = Http()
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=headers,
            body=dumps(message),
        )
        self.progressBar.setValue(100)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text.setText(_translate("Dialog", "Message to Send:"))
        self.URL.setText(_translate("Dialog", "Webhook URL:"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img "
                                                "src=\"title.png\"/></p></body></html>"))
        self.runfinal.setText(_translate("Dialog", "Run"))





title = Fore.RED + """
  _  _                         _       __      __   _    _             _   
 | || |__ _ _ _  __ _ ___ _  _| |_ ___ \ \    / /__| |__| |_  ___  ___| |__
 | __ / _` | ' \/ _` / _ \ || |  _(_-<  \ \/\/ / -_) '_ \ ' \/ _ \/ _ \ / /
 |_||_\__,_|_||_\__, \___/\_,_|\__/__/   \_/\_/\___|_.__/_||_\___/\___/_\_\ """ + Fore.RESET
print(title)
def withoutGUI():
    url = input(Fore.RED + "Hangouts Webhook URL:")
    message = str(input(f"{Fore.GREEN}Message to send:"))
    message = {'text': message}
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=headers,
        body=dumps(message),
    )


if __name__ == '__main__':
    while 1:
        i = input(Fore.BLUE + "(1)Minimal or (2)Full version: ")
        if i == "1" or i == "minimal":
            withoutGUI()
            break
        elif i == "2" or i == "full" or i == "full version":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            sys.exit(app.exec_())
            break
        else:
            print(Back.RED + Fore.WHITE + f"{i} is not a valid option, please try again! \n" + Back.RESET)

