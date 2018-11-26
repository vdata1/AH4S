
from PyQt4 import QtCore, QtGui
from Embedding import *
from Extracting import *
import time
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AH4S(object):

    def __init__(self):
        object.__init__(self)

       # self.setupUi(AH4S)
    def setupUi(self, AH4S):
        AH4S.setObjectName(_fromUtf8("AH4S"))
        AH4S.resize(802, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AH4S.setWindowIcon(icon)

        self.centralwidget = QtGui.QWidget(AH4S)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #Done

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 761, 491))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        #Done

        self.Embedding_tab = QtGui.QWidget()
        self.Embedding_tab.setObjectName(_fromUtf8("Embedding_tab"))
        #Done

        self.Clear_btn = QtGui.QPushButton(self.Embedding_tab)
        self.Clear_btn.setGeometry(QtCore.QRect(40, 400, 93, 29))
        self.Clear_btn.setObjectName(_fromUtf8("Clear_btn"))
        self.Clear_btn.clicked.connect(self.ClearEmbeddingTab)
        #Done


        self.OpenFile_btn = QtGui.QPushButton(self.Embedding_tab)
        self.OpenFile_btn.setGeometry(QtCore.QRect(140, 400, 93, 29))
        self.OpenFile_btn.setObjectName(_fromUtf8("OpenFile_btn"))
        self.OpenFile_btn.clicked.connect(self.OpenSecMsgFile)
        #Done

        self.Save_bin = QtGui.QPushButton(self.Embedding_tab)
        self.Save_bin.setGeometry(QtCore.QRect(240, 400, 93, 29))
        self.Save_bin.setObjectName(_fromUtf8("Save_bin"))
        self.Save_bin.clicked.connect(self.SaveCoverMsg)
        #Done

        self.Embedding_btn = QtGui.QPushButton(self.Embedding_tab)
        self.Embedding_btn.setGeometry(QtCore.QRect(340, 400, 93, 29))
        self.Embedding_btn.setObjectName(_fromUtf8("Embedding_btn"))
        self.Embedding_btn.clicked.connect(self.DoEmbedding)
        #Done

        self.groupBox = QtGui.QGroupBox(self.Embedding_tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 341))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        #Done

        self.ESecretMsg_box = QtGui.QPlainTextEdit(self.groupBox)
        self.ESecretMsg_box.setGeometry(QtCore.QRect(10, 30, 311, 301))
        self.ESecretMsg_box.setObjectName(_fromUtf8("ESecretMsg_box"))
        #Done

        self.groupBox_2 = QtGui.QGroupBox(self.Embedding_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 20, 351, 341))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        #Done

        self.ECoverMsg_box = QtGui.QPlainTextEdit(self.groupBox_2)
        self.ECoverMsg_box.setGeometry(QtCore.QRect(10, 20, 311, 301))
        self.ECoverMsg_box.setObjectName(_fromUtf8("ECoverMsg_box"))
        #Done

        self.groupBox_3 = QtGui.QGroupBox(self.Embedding_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(470, 370, 251, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        #Done

        self.ETimerVal_LineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.ETimerVal_LineEdit.setGeometry(QtCore.QRect(20, 30, 191, 31))
        self.ETimerVal_LineEdit.setObjectName(_fromUtf8("ETimerVal_LineEdit"))
        #Done

        self.tabWidget.addTab(self.Embedding_tab, _fromUtf8(""))
        self.Extracting_tab = QtGui.QWidget()
        self.Extracting_tab.setObjectName(_fromUtf8("Extracting_tab"))
        #Done

        self.groupBox_4 = QtGui.QGroupBox(self.Extracting_tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 341, 331))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        #Done

        self.XCoverMessage_box = QtGui.QPlainTextEdit(self.groupBox_4)
        self.XCoverMessage_box.setGeometry(QtCore.QRect(10, 20, 321, 301))
        self.XCoverMessage_box.setObjectName(_fromUtf8("XCoverMessage_box"))
        #Done

        self.groupBox_5 = QtGui.QGroupBox(self.Extracting_tab)
        self.groupBox_5.setGeometry(QtCore.QRect(370, 10, 341, 331))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        #Done


        self.XSecretMessage_box = QtGui.QPlainTextEdit(self.groupBox_5)
        self.XSecretMessage_box.setGeometry(QtCore.QRect(10, 20, 321, 301))
        self.XSecretMessage_box.setObjectName(_fromUtf8("XSecretMessage_box"))
        #Done


        self.groupBox_6 = QtGui.QGroupBox(self.Extracting_tab)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 360, 211, 71))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        #Done


        self.XTimeVal_LineEdit = QtGui.QLineEdit(self.groupBox_6)
        self.XTimeVal_LineEdit.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.XTimeVal_LineEdit.setObjectName(_fromUtf8("XTimeVal_LineEdit"))
        #Done


        self.XClear_btn = QtGui.QPushButton(self.Extracting_tab)
        self.XClear_btn.setGeometry(QtCore.QRect(20, 390, 93, 29))
        self.XClear_btn.setObjectName(_fromUtf8("XClear_btn"))
        self.XClear_btn.clicked.connect(self.ClearExtractingTab)
        #Done

        self.XOpenFile_btn = QtGui.QPushButton(self.Extracting_tab)
        self.XOpenFile_btn.setGeometry(QtCore.QRect(120, 390, 93, 29))
        self.XOpenFile_btn.setObjectName(_fromUtf8("XOpenFile_btn"))
        self.XOpenFile_btn.clicked.connect(self.OpenCoverMsgFile)
        #Done

        self.XSave_btn = QtGui.QPushButton(self.Extracting_tab)
        self.XSave_btn.setGeometry(QtCore.QRect(220, 390, 93, 29))
        self.XSave_btn.setObjectName(_fromUtf8("XSave_btn"))
        self.XSave_btn.clicked.connect(self.SaveSecMsg)
        #Done


        self.Extracting_btn = QtGui.QPushButton(self.Extracting_tab)
        self.Extracting_btn.setGeometry(QtCore.QRect(320, 390, 93, 29))
        self.Extracting_btn.setObjectName(_fromUtf8("Extracting_btn"))
        self.Extracting_btn.clicked.connect(self.DoExtracting)


        self.tabWidget.addTab(self.Extracting_tab, _fromUtf8(""))
        AH4S.setCentralWidget(self.centralwidget)
        #Done


        self.retranslateUi(AH4S)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AH4S)
        #Done


    def retranslateUi(self, AH4S):
        AH4S.setWindowTitle(_translate("AH4S", "AH4S", None))
        self.Clear_btn.setText(_translate("AH4S", "Clear", None))
        self.OpenFile_btn.setText(_translate("AH4S", "Open File", None))
        self.Save_bin.setText(_translate("AH4S", "Save", None))
        self.Embedding_btn.setText(_translate("AH4S", "Embeed", None))
        self.groupBox.setTitle(_translate("AH4S", "Secret Message", None))
        self.groupBox_2.setTitle(_translate("AH4S", "Final Cover Message ", None))
        self.groupBox_3.setTitle(_translate("AH4S", "Exec. Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Embedding_tab), _translate("AH4S", "Embedding", None))
        self.groupBox_4.setTitle(_translate("AH4S", "Cover Message", None))
        self.groupBox_5.setTitle(_translate("AH4S", "Secret Message", None))
        self.groupBox_6.setTitle(_translate("AH4S", "Exec. Timer", None))
        self.XClear_btn.setText(_translate("AH4S", "Clear", None))
        self.XOpenFile_btn.setText(_translate("AH4S", "Open", None))
        self.XSave_btn.setText(_translate("AH4S", "Save", None))
        self.Extracting_btn.setText(_translate("AH4S", "Extracting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Extracting_tab), _translate("AH4S", "Extracting", None))
    def ClearEmbeddingTab(self):
        self.ETimerVal_LineEdit.clear()
        self.ECoverMsg_box.clear()
        self.ESecretMsg_box.clear()
        self.SecMessage = ""
        self.EmbededMsg = ""
    def OpenSecMsgFile(self):
        FileName = QtGui.QFileDialog.getOpenFileName()
        File = open(FileName, 'r')
        self.ESecretMsg_box.clear()
        SecSTR = ""
        with File:
            SecSTR = File.read()
            self.ESecretMsg_box.appendPlainText(SecSTR)
        File.close()
    def SaveCoverMsg(self):
        FileName = QtGui.QFileDialog.getSaveFileName()
        File = open(FileName, "w")
        text = self.ECoverMsg_box.toPlainText()
        File.write(text)
        File.close()
    def DoEmbedding(self):

        EM = Embedding()
        self.EmbededMsg = ""
        self.SecMessage = ""
        SecMessageSTR = ""

        self.ECoverMsg_box.clear()
        self.ETimerVal_LineEdit.clear()

        self.SecMessage = self.ESecretMsg_box.toPlainText()

        SecMessageSTR = str(self.SecMessage)

        Timer_init = time.time()
        self.EmbededMsg = EM.Embed(SecMessageSTR)
        self.ETimerVal_LineEdit.setText(str(time.time() - Timer_init))

        self.ECoverMsg_box.setPlainText(self.EmbededMsg)
        SecMessageSTR  = ""
        self.EmbededMsg = ""
        self.SecMessage = ""
    def ClearExtractingTab(self):
        self.XTimeVal_LineEdit.clear()
        self.XCoverMessage_box.clear()
        self.XSecretMessage_box.clear()
    def OpenCoverMsgFile(self):
        FileName = QtGui.QFileDialog.getOpenFileName()
        File = open(FileName, 'r')
        self.XCoverMessage_box.clear()
        SecSTR = ""
        with File:
              SecSTR = File.read()
              self.XCoverMessage_box.appendPlainText(SecSTR)
              File.close()
    def SaveSecMsg(self):
        FileName = QtGui.QFileDialog.getSaveFileName()
        File = open(FileName, "w")
        text = self.XSecretMessage_box.toPlainText()
        File.write(text)
        File.close()
    def DoExtracting(self):
        self.XTimeVal_LineEdit.clear()
        self.XSecretMessage_box.clear()

        EX = Extracting()

        CoverMsg = str(self.ECoverMsg_box.toPlainText())
        Timer = time.time()
        SecMsg = EX.ExtractSecMsg(CoverMsg)
        self.XTimeVal_LineEdit.setText(str(time.time() - Timer))
        self.XSecretMessage_box.appendPlainText(str(SecMsg))









if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AH4S = QtGui.QMainWindow()
    ui = Ui_AH4S()
    ui.setupUi(AH4S)
    AH4S.show()
    sys.exit(app.exec_())
