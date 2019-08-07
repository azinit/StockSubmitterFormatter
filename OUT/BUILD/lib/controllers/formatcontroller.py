from fios.io import console
from fios.util import fstring

THREAD_NAME = "FORMATTER"

progress_options = {
    "allowed_sys_time": True,
    "allowed_iterator": True,
    "allowed_percent":  False,
    "symb_wait":        "~",
    "symb_finished":    "V",
}

process_options = {
    "symb": ".",
    "width": 72,
}


class FormatController(object):
    def __init__(self):
        self.file       = None
        self.name       = None
        self.lines      = None
        self.new_lines  = None
        self.stocker    = None

    def run(self):
        from fios.util import fpath
        console.process("ФОРМАТИРОВАНИЕ ФАЙЛОВ", **process_options)
        files        = self.__init_files()
        if not files:
            console.log("В ДИРЕКТОРИИ INPUT НЕ ОБНАРУЖЕНО ФАЙЛОВ", thread=THREAD_NAME)
        else:
            from lib.utils.PapaStocker import PapaStocker
            self.stocker = PapaStocker()
            console.process("", indent=False, **process_options)
            for i, file in enumerate(files):
                self.file = file
                self.name = fpath.cut(file, level=1)

                console.progress(
                    title="Обработка файлов",
                    done=i + 1, total=len(files),
                    extra_data=self.name + "\n", **progress_options,
                )

                if self.__is_formatted():
                    console.log("ДАННЫЙ ФАЙЛ УЖЕ БЫЛ ФОРМАТИРОВАН", thread=THREAD_NAME)
                else:
                    self.__read()
                    if not self.lines:
                        console.log("НА ВХОД ПОСТУПИЛ ПУСТОЙ ФАЙЛ", thread=THREAD_NAME)
                    else:
                        self.__format()
                        self.__save()
                console.process("", indent=False, **process_options)
            self.reset()
        print()
        print()
        print()

    """
    ..............................................................................................................
    ................................................ RUN STEPS ...................................................
    ..............................................................................................................
    """

    def __init_files(self):
        """ Init files in [input] directory"""
        console.log("Инициализация файлов")
        import os
        from lib.settings import SettingsMaster

        directory = SettingsMaster.INPUT_DIR
        files = [os.path.join(directory, f) for f in os.listdir(directory)]
        files = [f for f in files if os.path.isfile(f)]
        return files

    def __read(self):
        """ Read active file content """
        from fios.io import reader
        console.log("[{file}]: {process}".format(file=self.name, process="чтение..."), thread=THREAD_NAME)
        self.lines = reader.readlines(self.file, remove_empty_rows=True)

    def __format(self):
        """ Format file by lines """
        self.new_lines = []
        for i, line in enumerate(self.lines):
            console.progress("Форматирование строк", done=i + 1, total=len(self.lines),
                             extra_data=str([line]).ljust(64), **progress_options)
            self.stocker.run()
            if self.__is_line_formatted(line):
                formatted_line  = line
            else:
                term            = fstring.split(line, separator=',', soft=True)
                import time
                import random
                time.sleep(random.choice(range(1, 10)) / 10)
                keywords        = self.stocker.get_keywords(term)
                formatted_line  = "{src},,\"{keys}\"".format(src=line, keys=";".join(keywords))

            self.new_lines.append(formatted_line)

    def __save(self):
        """ Saving formatted file """
        from fios.io import writer
        from lib.settings import SettingsMaster
        import os

        console.log("[{file}]: {process}".format(file=self.name, process="сохранение..."), thread=THREAD_NAME)
        name = os.path.split(self.file)[1]
        path = os.path.join(SettingsMaster.OUTPUT_DIR, name)
        writer.writelines(path=path, content=self.new_lines, joiner="\n")

    def reset(self):
        """ Reset controller """
        self.file                       = None
        self.name                       = None
        self.lines                      = None
        self.new_lines                  = None

        if self.stocker is not None:    self.stocker.close()
        self.stocker                    = None

    def __is_formatted(self):
        """ Check if file is not formatted (by lines) """
        from lib.settings import SettingsMaster
        # return not all([self.__is_line_formatted(l) for l in self.lines])
        # and not SettingsMaster.is_formatted(self.file)
        return SettingsMaster.is_formatted(self.name)

    def __is_line_formatted(self, line):
        """ Check if line is already formatted """
        MAX_WORDS = 50
        return str(line).count(",") >= 2 and str(line).count('"') == 2 and str(line).count(";") == MAX_WORDS - 1
