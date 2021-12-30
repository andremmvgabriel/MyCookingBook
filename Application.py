import sys
import logging

from PyQt5 import QtWidgets

class Application:
    class Windows:
        _windows: dict = dict()

        @classmethod
        def setup(cls) -> None:
            logging.debug("Setting up the multiple windows of the application.")

            # Local imports to create each window
            from windows import MainWindow

            logging.debug("Windows setup completed.")

    @classmethod
    def start(cls) -> None:
        logging.info("Starting application: My Cooking Book")

        #app = QtWidgets.QApplication(sys.argv)
        #app.exec_()

        logging.info("Closed application.")