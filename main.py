from logic import *


def main() -> None:
    """
    Runs programs contents and opens gui
    :return: None
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()