import os
import sys
import logging
from logging.handlers import RotatingFileHandler

class Logger(object):
    @staticmethod
    def setup(level: int, save_dir: str, max_size: int = 5000000, backup_count: int = 24) -> None:
        log = logging.getLogger('')
        log.setLevel(level)
        format = logging.Formatter("%(asctime)-19s \t %(levelname)-8s \t %(message)s")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        handler1 = RotatingFileHandler(f"{save_dir}/log", maxBytes=max_size, backupCount=backup_count)

        handler1.setFormatter(format)
        log.addHandler(handler1)

        handler2 = logging.StreamHandler(sys.stdout)
        handler2.setFormatter(format)
        log.addHandler(handler2)
