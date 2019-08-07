from fios.io import console


# JSON_FILE = os.path.join(BASE_DIR, "json.txt")


"""
..............................................................................................................
................................................ MAIN ........................................................
..............................................................................................................
"""


def main():
    # from lib import settings
    from lib.controllers.maincontroller import MainController
    from lib.settings import SettingsMaster
    SettingsMaster.info()
    # from lib.utils.main import Database

    # Database.init_storage()

    main_controller = MainController(
        time_interval=0.0000000000000000000000001,
    )
    main_controller.run()


if __name__ == '__main__':
    import sys

    try:
        console.log("Загружаются модули для скрипта...")
        main()
        console.log("Скрипт успешно завершил работу!")
    except Exception as e:
        import traceback
        print(e)
        console.log("Работа скрипта прервана из за непредвиденной ошибки")
        print(str(e), file=sys.stderr, flush=True)

    input("Нажмите любую клавишу для выхода... ")
