# Итак - здесь разместим конструктор JSON для таблицы Manager

from copy import deepcopy
from Construct.Template_Construct_JSON import TemplateJSON


class ManagerJSON(TemplateJSON):
    """
    Класс который конструирует JSON для таблицы MeterDataTemplates

    """
    Generate_data = None

    JSON = {"table": "Manager"}

    def __init__(self,
                 # Количенство айдишников что мы генерим , либо их с список , либо ПОЛНОЦЕННЫЙ JSON
                 ids: int = 1,
                 # Либо сам тип - str/int либо список из всего этого добра
                 EventType: list = ["Scheduler"],
                 # Либо сам тип - str/int либо список из всего этого добра
                 ActionType: list = ["Poller"]
                 ):

        """
        Генератор JSON таблицы Manager

        :param ids: Количество айдишников что мы генерим , либо их с список , либо ПОЛНОЦЕННЫЙ JSON
        :param EventType: # Либо сам тип - str/int либо список из всего этого добра
        :param ActionType: # Либо сам тип - str/int либо список из всего этого добра
        """

        self.Generate_data = None
        self.JSON = {"table": "Manager"}

        from Construct.Manager.Template_Generate_Settings import GenerateSettingsManager
        from copy import deepcopy

        # Генерируем поле сетттингс

        self.Generate_data = deepcopy(GenerateSettingsManager(
                                                                ids=ids,
                                                                EventType=EventType,
                                                                ActionType=ActionType
                                                              ).settings)

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
        if ((type(ids) == int) and (ids > 0)) or (type(ids) == list) or (type(ids) == tuple) or (
                type(ids) == set):
            from Construct.Manager.Template_Generate_Settings import GenerateIdManager
            # Генерируем IDS
            ids = GenerateIdManager(ids=ids, settings=settings).ids
            # Добавляем
            JSON["ids"] = list(ids)

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
        if ((type(ids) == int) and (ids > 0)) or (type(ids) == list) or (type(ids) == tuple) or (
                type(ids) == set):
            from Construct.Manager.Template_Generate_Settings import GenerateIdManager
            # Генерируем IDS
            ids = GenerateIdManager(ids=ids, settings=settings).ids
            # Добавляем
            JSON["ids"] = list(ids)

        # ПОСЛЕ ЭТОГО СОЕДЕНЯЕМ
        JSON["method"] = "delete"

        if custom_settings is not None:
            JSON["ids"] = custom_settings

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
a = ManagerJSON().GET(5)

print(a)