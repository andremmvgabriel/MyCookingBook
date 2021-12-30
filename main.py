import sys
import logging
from PyQt5 import QtWidgets

from utils import Logger
from Application import Application

if __name__ == "__main__":
    # Setup logging...
    logging.getLogger("PyQt5").setLevel(logging.WARNING)
    Logger.setup(logging.DEBUG, "logs")

    Application.start()
