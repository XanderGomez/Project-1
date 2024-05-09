from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from gui import *

id_list = []


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda: self.submit())
        self.results_button.clicked.connect(lambda: self.result())
        self.exit_button.clicked.connect(lambda: self.exit())
        self.back_button.clicked.connect(lambda: self.back())

        try:
            with open(f'vote_results.txt', 'r+', newline='') as vote_file:
                votes = vote_file.readline().split()
                self.tristan_votes = votes[0]
                self.corbin_votes = votes[1]
                self.xander_votes = votes[2]
                self.george_votes = votes[3]
        except FileNotFoundError:
            self.tristan_votes = 0
            self.corbin_votes = 0
            self.xander_votes = 0
            self.george_votes = 0

    def submit(self):
        try:
            if self.id_entry.text().isdigit() != True or len(self.id_entry.text()) != 6:
                raise ValueError
            elif self.id_entry.text() in id_list:
                raise ZeroDivisionError

            if self.tristan_vote.isChecked():
                self.tristan_votes += 1
            elif self.corbin_vote.isChecked():
                self.corbin_votes += 1
            elif self.xander_vote.isChecked():
                self.xander_votes += 1
            elif self.george_vote.isChecked():
                self.george_votes += 1
            else:
                raise TypeError

            with open('vote_results.txt', 'w+') as vote_file:
                vote_file.write(f'{self.tristan_votes} {self.corbin_votes} {self.xander_votes} {self.george_votes}')

            self.id_entry.text().append(id_list)
            self.id_entry.setText('')
            self.error_label.setText('')
            self.tristan_vote.setChecked(False)
            self.corbin_vote.setChecked(False)
            self.xander_vote.setChecked(False)
            self.george_vote.setChecked(False)

        except ValueError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('Invalid ID!')
        except TypeError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('You must select a candidate!')
        except ZeroDivisionError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('ID already voted!')

    def result(self):
        if self.id_entry.text() == '052221':
            self.stackedWidget.setCurrentIndex(self.result_page)
        else:
            self.error_label.setText('Incorrect ID to view results')

    def back(self):
        self.stackedWidget.setCurrentIndex(self.vote_page)

    def exit(self):
        QCoreApplication.instance().quit()
