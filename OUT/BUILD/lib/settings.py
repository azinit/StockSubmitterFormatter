import os
import sys


class SettingsMaster(object):
    BASE_DIR        = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.dirname(__file__))
    LIB             = os.path.join(BASE_DIR, "lib")
    FORMATTER       = os.path.join(BASE_DIR, "Formatter")
    INPUT_DIR       = os.path.join(FORMATTER, "input")
    OUTPUT_DIR      = os.path.join(FORMATTER, "output")
    CHROME_DRIVER   = os.path.join(LIB, "chromedriver", "75.0.3770.140", "win32", "chromedriver.exe")

    @staticmethod
    def info():
        labels = ["BASE_DIR", "LIB", "FORMATTER", "INPUT_DIR", "OUTPUT_DIR", "CHROME_DRIVER"]
        for label in labels:
            path = getattr(SettingsMaster, label)
            print(label.ljust(16), path)

    @staticmethod
    def is_formatted(file_name):
        return os.path.exists(os.path.join(SettingsMaster.OUTPUT_DIR, file_name))

#
# if __name__ == '__main__':
#     import pyperclip
#     s = pyperclip.paste()
#     print(s)
