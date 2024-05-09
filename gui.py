# Form implementation generated from reading ui file 'voting_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 630)
        MainWindow.setMinimumSize(QtCore.QSize(530, 630))
        MainWindow.setMaximumSize(QtCore.QSize(530, 630))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(221, 221, 221)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -20, 530, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(530, 650))
        self.stackedWidget.setMaximumSize(QtCore.QSize(530, 650))
        self.stackedWidget.setObjectName("stackedWidget")
        self.vote_page = QtWidgets.QWidget()
        self.vote_page.setObjectName("vote_page")
        self.title_label = QtWidgets.QLabel(parent=self.vote_page)
        self.title_label.setGeometry(QtCore.QRect(195, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.id_entry = QtWidgets.QLineEdit(parent=self.vote_page)
        self.id_entry.setGeometry(QtCore.QRect(210, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_entry.setFont(font)
        self.id_entry.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-color: #000;\n"
"}")
        self.id_entry.setObjectName("id_entry")
        self.id_label = QtWidgets.QLabel(parent=self.vote_page)
        self.id_label.setGeometry(QtCore.QRect(150, 110, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.id_label.setFont(font)
        self.id_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.id_label.setObjectName("id_label")
        self.candidate_label = QtWidgets.QLabel(parent=self.vote_page)
        self.candidate_label.setGeometry(QtCore.QRect(200, 170, 141, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.candidate_label.setFont(font)
        self.candidate_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.candidate_label.setObjectName("candidate_label")
        self.tristan_vote = QtWidgets.QRadioButton(parent=self.vote_page)
        self.tristan_vote.setGeometry(QtCore.QRect(225, 220, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tristan_vote.setFont(font)
        self.tristan_vote.setObjectName("tristan_vote")
        self.corbin_vote = QtWidgets.QRadioButton(parent=self.vote_page)
        self.corbin_vote.setGeometry(QtCore.QRect(225, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.corbin_vote.setFont(font)
        self.corbin_vote.setObjectName("corbin_vote")
        self.xander_vote = QtWidgets.QRadioButton(parent=self.vote_page)
        self.xander_vote.setGeometry(QtCore.QRect(225, 300, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.xander_vote.setFont(font)
        self.xander_vote.setObjectName("xander_vote")
        self.george_vote = QtWidgets.QRadioButton(parent=self.vote_page)
        self.george_vote.setGeometry(QtCore.QRect(225, 340, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.george_vote.setFont(font)
        self.george_vote.setObjectName("george_vote")
        self.submit_button = QtWidgets.QPushButton(parent=self.vote_page)
        self.submit_button.setGeometry(QtCore.QRect(205, 400, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    background-color: rgb(193, 193, 193)\n"
"}")
        self.submit_button.setObjectName("submit_button")
        self.results_button = QtWidgets.QPushButton(parent=self.vote_page)
        self.results_button.setGeometry(QtCore.QRect(205, 450, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_button.setFont(font)
        self.results_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    background-color: rgb(193, 193, 193)\n"
"}")
        self.results_button.setObjectName("results_button")
        self.exit_button = QtWidgets.QPushButton(parent=self.vote_page)
        self.exit_button.setGeometry(QtCore.QRect(205, 500, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    background-color: rgb(193, 193, 193)\n"
"}")
        self.exit_button.setObjectName("exit_button")
        self.error_label = QtWidgets.QLabel(parent=self.vote_page)
        self.error_label.setEnabled(False)
        self.error_label.setGeometry(QtCore.QRect(100, 560, 341, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("QLabel* pLabel = new QLabel;\n"
"pLabel->setStyleSheet(\"QLabel { background-color : red; color : blue; }\");")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.label = QtWidgets.QLabel(parent=self.vote_page)
        self.label.setGeometry(QtCore.QRect(206, 130, 171, 20))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.vote_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.results_label = QtWidgets.QLabel(parent=self.result_page)
        self.results_label.setGeometry(QtCore.QRect(190, 50, 161, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        self.results_label.setFont(font)
        self.results_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.results_label.setObjectName("results_label")
        self.tristan_rslt_label = QtWidgets.QLabel(parent=self.result_page)
        self.tristan_rslt_label.setGeometry(QtCore.QRect(120, 170, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.tristan_rslt_label.setFont(font)
        self.tristan_rslt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tristan_rslt_label.setObjectName("tristan_rslt_label")
        self.corbin_rslt_label = QtWidgets.QLabel(parent=self.result_page)
        self.corbin_rslt_label.setGeometry(QtCore.QRect(120, 230, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.corbin_rslt_label.setFont(font)
        self.corbin_rslt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.corbin_rslt_label.setObjectName("corbin_rslt_label")
        self.xander_rslt_label = QtWidgets.QLabel(parent=self.result_page)
        self.xander_rslt_label.setGeometry(QtCore.QRect(120, 290, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.xander_rslt_label.setFont(font)
        self.xander_rslt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.xander_rslt_label.setObjectName("xander_rslt_label")
        self.george_rslt_label = QtWidgets.QLabel(parent=self.result_page)
        self.george_rslt_label.setGeometry(QtCore.QRect(120, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.george_rslt_label.setFont(font)
        self.george_rslt_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.george_rslt_label.setObjectName("george_rslt_label")
        self.ttl_votes_label = QtWidgets.QLabel(parent=self.result_page)
        self.ttl_votes_label.setGeometry(QtCore.QRect(120, 420, 141, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.ttl_votes_label.setFont(font)
        self.ttl_votes_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ttl_votes_label.setObjectName("ttl_votes_label")
        self.tristan_rslt_num = QtWidgets.QLabel(parent=self.result_page)
        self.tristan_rslt_num.setGeometry(QtCore.QRect(400, 170, 30, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.tristan_rslt_num.setFont(font)
        self.tristan_rslt_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tristan_rslt_num.setObjectName("tristan_rslt_num")
        self.corbin_rslt_num = QtWidgets.QLabel(parent=self.result_page)
        self.corbin_rslt_num.setGeometry(QtCore.QRect(400, 230, 30, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.corbin_rslt_num.setFont(font)
        self.corbin_rslt_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.corbin_rslt_num.setObjectName("corbin_rslt_num")
        self.xander_rslt_num = QtWidgets.QLabel(parent=self.result_page)
        self.xander_rslt_num.setGeometry(QtCore.QRect(400, 290, 30, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.xander_rslt_num.setFont(font)
        self.xander_rslt_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.xander_rslt_num.setObjectName("xander_rslt_num")
        self.george_rslt_num = QtWidgets.QLabel(parent=self.result_page)
        self.george_rslt_num.setGeometry(QtCore.QRect(400, 350, 30, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.george_rslt_num.setFont(font)
        self.george_rslt_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.george_rslt_num.setObjectName("george_rslt_num")
        self.total_rslt_num = QtWidgets.QLabel(parent=self.result_page)
        self.total_rslt_num.setGeometry(QtCore.QRect(400, 420, 30, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        self.total_rslt_num.setFont(font)
        self.total_rslt_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.total_rslt_num.setObjectName("total_rslt_num")
        self.back_button = QtWidgets.QPushButton(parent=self.result_page)
        self.back_button.setGeometry(QtCore.QRect(200, 510, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    background-color: rgb(193, 193, 193)\n"
"}")
        self.back_button.setObjectName("back_button")
        self.stackedWidget.addWidget(self.result_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Voting"))
        self.id_label.setText(_translate("MainWindow", "ID"))
        self.candidate_label.setText(_translate("MainWindow", "Candidates"))
        self.tristan_vote.setText(_translate("MainWindow", "Tristan"))
        self.corbin_vote.setText(_translate("MainWindow", "Corbin"))
        self.xander_vote.setText(_translate("MainWindow", "Xander"))
        self.george_vote.setText(_translate("MainWindow", "George"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.results_button.setText(_translate("MainWindow", "Results"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.error_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "ID must be 6 numeric digits only"))
        self.results_label.setText(_translate("MainWindow", "Results"))
        self.tristan_rslt_label.setText(_translate("MainWindow", "Tristan"))
        self.corbin_rslt_label.setText(_translate("MainWindow", "Corbin"))
        self.xander_rslt_label.setText(_translate("MainWindow", "Xander"))
        self.george_rslt_label.setText(_translate("MainWindow", "George"))
        self.ttl_votes_label.setText(_translate("MainWindow", "Total Votes"))
        self.tristan_rslt_num.setText(_translate("MainWindow", "0"))
        self.corbin_rslt_num.setText(_translate("MainWindow", "0"))
        self.xander_rslt_num.setText(_translate("MainWindow", "0"))
        self.george_rslt_num.setText(_translate("MainWindow", "0"))
        self.total_rslt_num.setText(_translate("MainWindow", "0"))
        self.back_button.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
