from copy import deepcopy
from Construct.Template_Construct_JSON import TemplateJSON


class MeterDataTemplatesJSON(TemplateJSON):
    """
    Класс который конструирует JSON для таблицы MeterDataTemplates

    """
    Generate_data = None

    JSON = {"table": "MeterDataTemplates"}

    def __init__(self, name: int = 1, types: int = 3, unique_types: bool = True):

        """

        Генератор JSON таблицы MeterDataTemplates

        :param name: - Либо количество автосгенерирвоанных имен, либо список имен для генерации , либо Полноценный JSON
        :param types: - либо количество ArchTypes для автогенерации либо список ArchTypes
        :param unique_types: Уникальны ли ArchTypes для каждого name
        """

        self.Generate_data = None
        self.JSON = {"table": "MeterDataTemplates"}

        from Construct.MeterDataTemplates.Template_Generate_Settings import GenerateSettings
        from copy import deepcopy

        # Генерируем поле сетттингс

        self.Generate_data = deepcopy(GenerateSettings(name=name, types=types, unique_types=unique_types).settings)

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
            # ИМЕНА которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            names=0,
            # Записываем или нет полученные значения
            Record_Values: bool = True,
            # Свои значения - Не проверяются
            custom_settings=None
            ):

        """
        Здесь генерируем запрос для получения нужных данных

        :param names: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
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
        if ((type(names) == int) and (names > 0)) or (type(names) == list) or (type(names) == tuple) or (
                type(names) == set):
            from Construct.MeterDataTemplates.Template_Generate_Settings import GenerateNamesMeterDataTemplates
            # Генерируем IDS
            names = GenerateNamesMeterDataTemplates(names=names, settings=settings).names

            print(names)
            # Добавляем
            JSON["names"] = list(names)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "get"

        if custom_settings is not None:
            JSON["names"] = custom_settings

        # если надо - то записываем данные
        if Record_Values:
            self.RecordData()

        # И ОТДАЕМ В ЗАД

        return JSON

    def DELETE(
               self,
               # # ИМЕНА которые удалчяемп  - Либо сколько, либо какие - 0 запрашиваем все
               names=0,
               # Записываем или нет полученные значения
               Record_Values: bool = True,
               # Свои значения - Не проверяются
               custom_settings=None
               ):

        """
        Здесь генерируем запрос для удаления  нужных данных

        :param names: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
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
        if ((type(names) == int) and (names > 0)) or (type(names) == list) or (type(names) == tuple) or (type(names) == set):
            from Construct.MeterDataTemplates.Template_Generate_Settings import GenerateNamesMeterDataTemplates
            # Генерируем IDS
            names = GenerateNamesMeterDataTemplates(names=names, settings=settings).names
            # Добавляем
            JSON["names"] = list(names)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "delete"

        if custom_settings is not None:
            JSON["names"] = custom_settings

        # если надо - то записываем данные
        if Record_Values:
            self.RecordData()

        # И ОТДАЕМ В ЗАД

        return JSON

# -------------------------------------------------------------------------------------->
# -------------------------------------------------------------------------------------->
# -------------------------------------------------------------------------------------->
# -------------------------------------------------------------------------------------->
# -------------------------------------------------------------------------------------->
