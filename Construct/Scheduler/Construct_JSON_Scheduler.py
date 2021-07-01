from Construct.Scheduler.Template_construct_field_settings import ConstructFieldSettings
from copy import deepcopy


# Здесь Сделаем КОНСТРУКТОР JSON дял таблицы
#
# class SchedulerJSON:
#     """
#
#     Класс который конструирует JSON для таблицы Scheduler
#
#     """
#
#     Generate_data = None
#
#     JSON = {"table": "Scheduler"}
#
#     def __init__(self, custom_data: list = []):
#         self.custom_data = custom_data
#
#     def _update_settings(self, settings: list):
#
#         """
#         В Этом методе берем и переписываем наши сгенерированные ID
#         :param settings:
#         :return:
#         """
#         custom_data = self.custom_data
#
#         # Перебираем все наши возможные переписываемые значения
#         for i in custom_data:
#             idx = i.get('id')
#
#             # ТЕПЕРЬ - если есть значение - То ищем его в нашем сгененрирвоанных значениях
#             if type(idx) == int:
#                 coincidence = False
#                 for x in settings:
#                     # ЕСЛИ ЕСТЬ СОВПАДЕНИЯ - перезаписываем весь словарь
#                     if idx == x.get('id'):
#                         # ставим что совпадение найдено
#                         coincidence = True
#                         x.update(i)
#                 # Если совпадения не найдено , просто добавляем
#                 if not coincidence:
#                     settings.append(i)
#
#             # ЕСли это не инт то просто захламляем список
#             else:
#                 settings.append(i)
#
#         return settings
#
#     def _find_max_value(self):
#         """
#         В Этом методе ищем максимальное значение
#
#         :return:
#         """
#         from Service.SQL import execute_command
#         command = 'SELECT max(Id) FROM Scheduler'
#
#         max_id = execute_command(command=command)
#
#         # idx = None
#         for i in max_id:
#             idx = i.get('max(Id)')
#         if idx is None:
#             idx = 0
#
#         return idx
#
#     def _find_all_value(self):
#         """
#         В ЭТОМ МЕТОДЕ ИЩЕМ ВСЕ ЗНАЧЕНИЯ ID
#
#         :return:
#         """
#         from Service.SQL import execute_command
#         command = 'SELECT Id FROM Scheduler'
#
#         id_dict = execute_command(command=command)
#
#         id_list = []
#
#         for idx in id_dict:
#             id_list.append(idx.get('Id'))
#
#         return id_list
#
#     def POST(self, mon: bool = True, day: bool = True, hour: bool = True, generate: int = 1, min: int = None,
#              start: int = 0):
#         """
#         Метод для перезаписи\ дополнения записей - Це важно
#
#         :param generate: - int/list - Количество записей что генерируем / или сам лист Settings
#         :param mon: - bool - Генерируем или нет месяцы
#         :param day: - bool - Генерируем или нет дни
#         :param hour: - bool - Генерируем или нет часы
#
#         :param min: - int - Устанавливает нужное количество минут для всех элементов
#         :param start: - int - стартовый айдишник - Если установлен в 0 то старт начинается с последней записи
#         :return:
#         """
#
#         # Итак - основная логика работы -
#         # 1) в generate можно спускать -
#         #     - количество - и они генерируются ПО заданым булевым параметрам  от числа что указано в start
#         #         - Поле тупес подставляется
#         #         - Поле тупес генерируется уникальным
#         #         - Поле тупес генерируется одинаковое для всех
#         #     - список имен и они подставляются
#         #     - Уже готовый Settings
#
#         if start < 1:
#             start = int(self._find_max_value()) + 1
#
#         from Construct.Scheduler.Template_Generate_Settings import GenerateSettingsScheduler
#
#         settings = GenerateSettingsScheduler(
#             # Количество генераций - или полный список того что должны сгенерировать
#             generate=generate,
#             # Наличие месяца
#             mon=mon,
#             # Наличие для
#             day=day,
#             # наличие часа
#             hour=hour,
#             # Установка минут
#             min=min,
#             # айдищник старта генерации
#             start=start).settings
#         # Теперь получившееся недоразумение берем и дополняем параметрами которые мы дополняем
#         # settings = self._update_settings(settings)
#
#         # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
#         JSON = deepcopy(self.JSON)
#
#         JSON["method"] = "post"
#         JSON["settings"] = list(settings)
#         # И ОТДАЕМ В ЗАД
#
#         return JSON
#
#     def PUT(self, mon: bool = True, day: bool = True, hour: bool = True, count: int = 1, min: int = None,
#             start: int = 1):
#
#         """
#          Метод для Полной Перезаписи всех Значений
#
#         :param mon:- bool - Генерируем или нет месяцы
#         :param day:- bool - Генерируем или нет дни
#         :param hour:- bool - Генерируем или нет часы
#         :param count:- int - Количество записей что генерируем
#         :param min: - int - Устанавливает нужное количество минут для всех элементов
#         :param start: - int - стартовый айдишник
#         :return:
#         """
#         if start < 1:
#             start = 1
#
#         settings = []
#         for idx in range(count):
#             # Генерируем один из элементов
#             setting = ConstructFieldSettings(idx=start + idx, mon=mon, day=day, hour=hour, min=min).settings
#             settings.append(setting)
#
#         # Теперь получившееся недоразумение берем и дополняем параметрами корые мы дополняем
#         settings = self._update_settings(settings)
#
#         # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
#         JSON = deepcopy(self.JSON)
#
#         JSON["method"] = "put"
#         JSON["settings"] = list(settings)
#         # И ОТДАЕМ В ЗАД
#
#         return JSON
#
#     def GET(self, ids=0):
#
#         """
#         Здесь генерируем запрос для получения нужных данных
#
#         :param ids: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
#         если спускаем list / tuple / set - то что поделать вставляем их
#
#
#         :return:
#
#         """
#
#         # ЕСЛИ у нас int
#         if type(ids) == int:
#             # сначала получаем все айдишники что есть
#             all_idx = self._find_all_value()
#
#             # чтоб не выстрелить себе в ногу
#             if ids > len(all_idx):
#                 ids = len(all_idx)
#
#             # если у нас 0 - То всех их получаем
#             if ids == 0:
#                 idx = all_idx
#
#             else:
#                 from random import randint
#                 idx = set()
#                 while len(idx) < ids:
#                     idx.add(all_idx[randint(0, (len(all_idx) - 1))])
#
#                 idx = list(idx)
#
#         elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
#             idx = list(ids)
#
#         # иначе селектим все
#         else:
#             idx = self._find_all_value()
#
#         # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
#         JSON = deepcopy(self.JSON)
#
#         JSON["method"] = "get"
#         JSON["ids"] = list(idx)
#         # И ОТДАЕМ В ЗАД
#
#         return JSON
#
#     def DELETE(self, ids=0):
#
#         """
#         Здесь генерируем запрос для Удаления нужных данных
#
#         :param ids: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
#         если спускаем list / tuple / set - то что поделать вставляем их
#
#         :return:
#
#         """
#
#         # ЕСЛИ у нас int
#         if type(ids) == int:
#             # сначала получаем все айдишники что есть
#             all_idx = self._find_all_value()
#
#             # чтоб не выстрелить себе в ногу
#             if ids > len(all_idx):
#                 ids = len(all_idx)
#
#             # если у нас 0 - То всех их получаем
#             if ids == 0:
#                 idx = all_idx
#
#             else:
#                 from random import randint
#                 idx = set()
#                 while len(idx) < ids:
#                     idx.add(all_idx[randint(0, (len(all_idx) - 1))])
#
#                 idx = list(idx)
#
#         elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
#             idx = list(ids)
#
#         # иначе селектим все
#         else:
#             idx = self._find_all_value()
#
#         # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
#         JSON = deepcopy(self.JSON)
#         JSON["method"] = "delete"
#         JSON["ids"] = list(idx)
#         # И ОТДАЕМ В ЗАД
#         return JSON


# --------------------------------------------------------------------------------------------------------------------
#                                    Все хуйня миша , давай по новой
# --------------------------------------------------------------------------------------------------------------------


class SchedulerJSON:
    """

    Класс который конструирует JSON для таблицы Scheduler

    """

    Generate_data = None

    JSON = {"table": "Scheduler"}


    def __init__(self,
                 # Генерация количества ID , Либо Список ID , Либо готовый Settings
                 generate: int = 1,
                 # Наличие месяца в генерации
                 mon: bool = True,
                 # Наличие дня в генерации
                 day: bool = True,
                 # Наличие часа в генерации
                 hour: bool = True,
                 # Значение минут в генерации
                 min: int = None,
                 # Стартовый айдишник , если используется генерация - ВЫРЕЗАЕМ
                 # start: int = 0
                 ):

        self.Generate_data = None
        self.JSON = {"table": "Scheduler"}


        # Итак - основная логика работы -
        # 1) в generate можно спускать -
        #     - количество - и они генерируются ПО заданым булевым параметрам  от числа что указано в start
        #         - Поле тупес подставляется
        #         - Поле тупес генерируется уникальным
        #         - Поле тупес генерируется одинаковое для всех
        #     - список имен и они подставляются
        #     - Уже готовый Settings

        from Construct.Scheduler.Template_Generate_Settings import GenerateSettingsScheduler
        # Итак - генерируем наш тестовый сет
        self.Generate_data = GenerateSettingsScheduler(
            # Количество генераций -
            # или полный список того что должны сгенерировать
            generate=generate,
            # Наличие месяца
            mon=mon,
            # Наличие для
            day=day,
            # наличие часа
            hour=hour,
            # Установка минут
            min=min,
            # айдищник старта генерации - ВЫРЕЗАНО
            # start=start
        ).settings

    def POST(self, custom_settings=None):
        """
         Метод для перезаписи или дополнения записей

         Берутся значения что были сгенерированы в конструкторе класса, и формируется JSON

        :param custom_settings: - Если необходимо вставить свои записи - НИКАК не проверяются
        :return: Возвращает готовый к употреблению JSON
        """

        # ТЕПЕРЬ СМОТРИМ - подставляем нужные значения

        if custom_settings is None:
            settings = self.Generate_data
        else:
            settings = custom_settings

        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "post"
        JSON["settings"] = list(settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def PUT(self, custom_settings=None):

        """
         Метод для Полной Перезаписи всех Значений

         Берутся значения что были сгенерированы в конструкторе класса, и формируется JSON

        :param custom_settings: - Если необходимо вставить свои записи - НИКАК не проверяются
        :return: Возвращает готовый к употреблению JSON
        """
        # ТЕПЕРЬ СМОТРИМ - подставляем нужные значения

        if custom_settings is None:
            settings = self.Generate_data
        else:
            settings = custom_settings

        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "post"
        JSON["settings"] = list(settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def GET(self,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            ids=0,
            # Записываем или нет полученные значения
            Record_Values: bool = True,
            # Свои значения - Не проверяются
            custom_settings=None
            ):

        """
        Здесь генерируем запрос для получения нужных данных

        :param ids: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
                если спускаем list / tuple / set - то что поделать вставляем их
        :param custom_settings: - Если необходимо вставить свои записи - НИКАК не проверяются
        :param Record_Values: - Значения что запрашиваем - сразу записываем
        :return: Возвращает готовый к употреблению JSON

        """
        # ПОЛУЧАЕМ НАШ JSON
        JSON = deepcopy(self.JSON)

        # ТЕПЕРЬ СМОТРИМ - подставляем нужные значения
        settings = self.Generate_data

        # ТЕПЕРЬ ЕСЛИ У НАС число либо список
        if (type(ids) == int) or (ids > 0) or (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            from Construct.Scheduler.Template_Generate_Settings import GenerateIdsScheduler

            # Генерируем IDS
            idx = GenerateIdsScheduler(ids=ids, settings=settings).idx
            # Добавляем
            JSON["ids"] = list(idx)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "get"

        if custom_settings is not None:
            JSON["ids"] = custom_settings

        # если надо - то записываем данные
        if Record_Values:
            self.RecordData()


        # И ОТДАЕМ В ЗАД

        return JSON

    def DELETE(self,
               # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
               ids=0,
               # Записываем или нет полученные значения
               Record_Values: bool = True,
               # Свои значения - Не проверяются
               custom_settings=None
               ):

        """
        Здесь генерируем запрос для удаления  нужных данных

        :param ids: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
                если спускаем list / tuple / set - то что поделать вставляем их
        :param custom_settings: - Если необходимо вставить свои записи - НИКАК не проверяются
        :param Record_Values: - Значения что запрашиваем - сразу записываем
        :return: Возвращает готовый к употреблению JSON

        """
        # ПОЛУЧАЕМ НАШ JSON
        JSON = deepcopy(self.JSON)

        # ТЕПЕРЬ СМОТРИМ - подставляем нужные значения
        settings = self.Generate_data

        # ТЕПЕРЬ ЕСЛИ У НАС число либо список
        if (type(ids) == int) or (ids > 0) or (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            from Construct.Scheduler.Template_Generate_Settings import GenerateIdsScheduler

            # Генерируем IDS
            idx = GenerateIdsScheduler(ids=ids, settings=settings).idx
            # Добавляем
            JSON["ids"] = list(idx)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "delete"

        if custom_settings is not None:
            JSON["ids"] = custom_settings

        # если надо - то записываем данные
        if Record_Values:
            self.RecordData()

        # И ОТДАЕМ В ЗАД

        return JSON

    def RecordData(self):

        """
        Этот метод Записывает То что мы сгенерировали в конструкторе класса
        :return:
        """

        from Template.Template_DataBase_by_JSON import DataBase

        record_JSON = {'settings': self.Generate_data}
        record_JSON.update(self.JSON)
        record = DataBase().INSERT(JSON=record_JSON)
