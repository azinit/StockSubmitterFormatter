import os
import sys


class SettingsMaster(object):
    BASE_DIR    = os.path.dirname(os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__))
    LIB         = os.path.join(BASE_DIR, "lib")
    FORMATTER   = os.path.join(BASE_DIR, "Formatter")
    INPUT_DIR   = os.path.join(FORMATTER, "input")
    OUTPUT_DIR  = os.path.join(FORMATTER, "output")

    @staticmethod
    def is_formatted(file_name):
        return os.path.exists(os.path.join(SettingsMaster.OUTPUT_DIR, file_name))
