from copy import deepcopy
from Construct.Template_Construct_JSON import TemplateJSON


class PollerJSON(TemplateJSON):
    """
    Класс который конструирует JSON для таблицы Poller

    """

    custom_data = {}

    JSON = {"table": "Poller"}

    def __init__(self,
                 ids: int = 1,
                 metersName: int = 1,
                 archTypesName: int = 1,
                 generate_of_max: bool = True,
                 ArchTypes: int = 2,
                 CountMeter: int = 2):
        """
                Конструктор для составления JSON

        :param ids: - ЛИБО количетво ID , Либо список ID , ЛИБО ПОЛНОЦЕННЫЙ JSON
        :param metersName: - MeterTemplates  - name - ЛИБО количество name, Либо список name
        :param archTypesName:  - MeterDataTemplates - name - количество Name , Либо список name
        :param generate_of_max: - Булевый параметр - идет от наибольшего айдишника или нет
        :param ArchTypes: Количество генерируемых ArchTypes
        :param CountMeter: Количество генерируемых счетчиков
        """
        # Конструктор для составления JSON
        # id - Свой
        # metersName - MeterTemplates  - name
        # archTypesName - MeterDataTemplates - name

        self.Generate_data = None
        self.JSON = {"table": "Poller"}

        from Construct.Poller.Template_Construct_Settings import GenerateSettingsPoller
        from copy import deepcopy

        # Генерируем поле сетттингс

        self.Generate_data = deepcopy(GenerateSettingsPoller(ids=ids,
                                                             metersName=metersName,
                                                             archTypesName=archTypesName,
                                                             generate_of_max=generate_of_max,
                                                             ArchTypes=ArchTypes,
                                                             CountMeter=CountMeter
                                                             ).settings)

        # print(self.Generate_data)
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
            ids=0,
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
        if ((type(ids) == int) and (ids > 0)) or (type(ids) == list) or (type(ids) == tuple) or (
                type(ids) == set):
            from Construct.Poller.Template_Construct_Settings import GenerateIdPoller
            # Генерируем IDS
            idx = GenerateIdPoller(ids=ids, settings=settings).ids

            # Добавляем
            JSON["id"] = list(idx)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "get"

        if custom_settings is not None:
            JSON["names"] = custom_settings

        # print(JSON)

        # если надо - то записываем данные
        if Record_Values:
            self.RecordData()

        # И ОТДАЕМ В ЗАД

        return JSON

    def DELETE(
               self,
               # # ИМЕНА которые удалчяемп  - Либо сколько, либо какие - 0 запрашиваем все
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
        if ((type(ids) == int) and (ids > 0)) or (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            from Construct.Poller.Template_Construct_Settings import GenerateIdPoller
            # Генерируем IDS
            idx = GenerateIdPoller(ids=ids, settings=settings).ids

            # Добавляем
            JSON["id"] = list(idx)

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
# PollerJSON(ids=3,metersName=2,archTypesName=2, generate_of_max=True,ArchTypes=2, CountMeter=6).GET(ids=2)