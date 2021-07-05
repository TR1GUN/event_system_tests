from Construct.Scheduler.Template_construct_field_settings import ConstructFieldSettings
from copy import deepcopy


# Здесь Сделаем КОНСТРУКТОР JSON дял таблицы
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

        JSON["method"] = "put"
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
