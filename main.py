from fios.io import console


# JSON_FILE = os.path.join(BASE_DIR, "json.txt")


"""
..............................................................................................................
................................................ MAIN ........................................................
..............................................................................................................
"""


def main():
    # from lib import settings
    from lib.controllers.menu import Menu
    # from lib.utils.main import Database

    # Database.init_storage()

    menu = Menu(
        time_interval=0.0000000000000000000000001,
    )
    menu.run()


if __name__ == '__main__':
    import sys

    # try:
    console.log("Загружаются модули для скрипта...")
    main()
    console.log("Скрипт успешно завершил работу!")
    # except Exception as e:
    #     import traceback
    #     console.log("Работа скрипта прервана из за непредвиденной ошибки")
    #     print(str(e), file=sys.stderr, flush=True)

    input("Нажмите любую клавишу для выхода... ")
