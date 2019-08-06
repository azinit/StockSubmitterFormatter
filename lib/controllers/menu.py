from fios.io import console

from lib.controllers.maincontroller import MainController


class Menu(MainController):
    def __init__(self, time_interval):
        super().__init__(time_interval)

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
        console.box("Case Parser 0.8", width=64)
        # interface
        variants = [
            "0. -",
            "1. -",
            "2. Выход из программы",
            "3. -",
        ]

        msg = '\r\n'.join(variants)
        print(msg)
        # input
        var = int(input(">>> "))
        print()
        return var

    def __match(self, var: int):
        if var == 0:
            # self.run_parser()
            return True
        elif var == 1:
            # self.run_generator()
            pass
        elif var == 2:
            """ Exit """
            return False
        elif var == 3:
            self.reset()
            return True
        else:
            """ Invalid command """
            return None
