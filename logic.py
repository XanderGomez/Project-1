from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from gui import *

id_list = []

try:
    with open('voted_id.txt', 'r') as file:
        id_list = file.readline().split()
except FileNotFoundError:
    id_list = []


class Logic(QMainWindow, Ui_MainWindow):
    """
    Class for the Gui logic components
    """
    def __init__(self) -> None:
        """
        Initializes and defines variables within the Gui
        :return: None
        """
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda: self.submit())
        self.results_button.clicked.connect(lambda: self.result())
        self.exit_button.clicked.connect(lambda: self.exit())
        self.back_button.clicked.connect(lambda: self.back())

        try:
            with open(f'vote_results.txt', 'r+', newline='') as vote_file:
                votes = vote_file.readline().split()
                self.tristan_votes = int(votes[0])
                self.corbin_votes = int(votes[1])
                self.xander_votes = int(votes[2])
                self.george_votes = int(votes[3])
                self.tristan_rslt_num.setText(votes[0])
                self.corbin_rslt_num.setText(votes[1])
                self.xander_rslt_num.setText(votes[2])
                self.george_rslt_num.setText(votes[3])
                self.total = 0
                for x in votes:
                    self.total += int(x)
                self.total_rslt_num.setText(str(self.total))

        except FileNotFoundError:
            self.tristan_votes = 0
            self.corbin_votes = 0
            self.xander_votes = 0
            self.george_votes = 0

    def submit(self) -> None:
        """
        Provides functionality for the submit button
        :return: None
        """
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

            with open('vote_results.txt', 'r+') as vote_file:
                votes = vote_file.readline().split()
                self.tristan_rslt_num.setText(votes[0])
                self.corbin_rslt_num.setText(votes[1])
                self.xander_rslt_num.setText(votes[2])
                self.george_rslt_num.setText(votes[3])
                self.total += 1
                self.total_rslt_num.setText(str(self.total))

            id_list.append(self.id_entry.text())
            with open('voted_id.txt', 'w') as file:
                for x in range(len(id_list)):
                    file.write(f'{id_list[x]} ')
            print(id_list)
            self.id_entry.setText('')
            self.error_label.setText('')
            self.buttonGroup.setExclusive(False)
            if self.tristan_vote.isChecked():
                self.tristan_vote.setChecked(False)
            elif self.corbin_vote.isChecked():
                self.corbin_vote.setChecked(False)
            elif self.xander_vote.isChecked():
                self.xander_vote.setChecked(False)
            elif self.george_vote.isChecked():
                self.george_vote.setChecked(False)
            self.id_entry.setFocus()

        except ValueError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('Invalid ID!')
        except TypeError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('You must select a candidate!')
        except ZeroDivisionError:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('ID already voted!')
        except:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('Error')

    def result(self) -> None:
        """
        Provides functionality for the result button
        :return: None
        """
        if self.id_entry.text() == '052221':
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.error_label.setStyleSheet("color: rgb(255, 0, 0)")
            self.error_label.setText('Incorrect ID to view results')

    def back(self) -> None:
        """
        Provides functionality for the back button
        :return: None
        """
        self.stackedWidget.setCurrentIndex(0)

    def exit(self) -> None:
        """
        Provides functionality for the exit button
        :return: None
        """
        QCoreApplication.instance().quit()
