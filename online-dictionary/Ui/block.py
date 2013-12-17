# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block.ui'
#
# Created: Tue Dec 17 14:02:37 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parrent=None):
        super(Ui_Form, self).__init__(parrent)
        Form=self
        #Form.setObjectName("Form")
        #Form.resize(400, 300)
        self.webView = QtWebKitWidgets.QWebView(Form)
        self.webView.setGeometry(QtCore.QRect(-21, -31, 481, 421))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webView.setHtml(
        '''
            <html>
            <body>
            <h1>My First Heading</h1>
            <p>My first paragraph.</p>
            </body>
            </html>
        '''
        )
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from PyQt5 import QtWebKitWidgets
