import sys
import logging

from PyQt5 import QtWidgets

class Application:
    class Windows:
        __windows: dict = dict()

        @classmethod
        def setup(cls) -> None:
            logging.debug("Setting up the multiple windows of the application.")

            # Local imports to create each window
            from windows import MainWindow

            # Windows creation
            cls.__windows["main"] = MainWindow()

            logging.debug("Windows setup completed.")
        
        @classmethod
        def open(cls, tag: str) -> None:
            logging.debug(f"Open window: {tag}.")
            cls.__windows[tag].show()

    @classmethod
    def start(cls) -> None:
        logging.info("Starting application: My Cooking Book")

        app = QtWidgets.QApplication(sys.argv)
        
        cls.Windows.setup()
        cls.Windows.open("main")

        app.exec_()

        logging.info("Closed application.")
