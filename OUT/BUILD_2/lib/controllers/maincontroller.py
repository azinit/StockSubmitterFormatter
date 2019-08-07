from fios.io import console

from lib.controllers.formatcontroller import FormatController


class MainController(FormatController):
    def __init__(self, time_interval):
        super().__init__()

    def run(self):
        while True:
            var         = self.__ask_user()
            force_stop  = self.__match(var) is False
            if force_stop:
                console.process("Завершение работы", symb='.', width=72)
                break
    """
    ..............................................................................................................
    ................................................ BUILT-IN ....................................................
    ..............................................................................................................
    """

    def __ask_user(self):
        # box
        console.box("Stock Submitter v.0.2", width=64)
        # interface
        variants = [
            "0. Открыть папку с исходными данными",
            "1. Запустить форматирование",
            "2. Открыть папку с выходным данными",
            # "3. Выход из программы",
        ]

        msg = '\r\n'.join(variants)
        print(msg)
        # input
        var = input(">>> ")
        print()
        if var not in ["0", "1", "2"]:
            return self.__ask_user()
        else:
            return int(var)

    def __match(self, var: int):
        from fios.os import explorer
        from lib.settings import SettingsMaster
        if var == 0:
            """ Open [input] """
            explorer.open_(SettingsMaster.INPUT_DIR, wait_message="(Нажмите любую клавишу для продолжения)")
            return True
        elif var == 1:
            """ Start format """
            FormatController.run(self)
        elif var == 2:
            """ Open [output] """
            explorer.open_(SettingsMaster.OUTPUT_DIR, wait_message="(Нажмите любую клавишу для продолжения)")
            return True
        # elif var == 3:
        #     """ Exit """
        #     return False
        else:
            """ Invalid command """
            return None
