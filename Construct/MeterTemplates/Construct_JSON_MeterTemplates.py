from copy import deepcopy
from Construct.Template_Construct_JSON import TemplateJSON


class MeterTemplatesJSON(TemplateJSON):
    """
    Класс который конструирует JSON для таблицы MeterTemplates

    """

    custom_data = {}

    JSON = {"table": "MeterTemplates"}

    def __init__(self, custom_data: list = []):
        self.custom_data = custom_data

    # def _generate_values(self, count_setting, count_meter, unique_meter):
    #
    #     """
    #     Генерация поля сеттинг - Это очень важно
    #
    #     :param count_setting:
    #     :param count_meter:
    #     :param unique_meter:
    #     :return:
    #     """
    #
    #     from Construct.MeterTemplates.Template_Generate_MeterId import GenerateMeterId
    #     settings = []
    #     if unique_meter:
    #         # Ищем самый страрший счетчик
    #         Meter_Id = 0
    #         for i in count_setting:
    #             Meter_Id_list = GenerateMeterId(count_meter=count_meter, start=Meter_Id).MeterId
    #             element = {"name": "Test_Name_" + str(i), "meters": Meter_Id_list}
    #             Meter_Id = max(Meter_Id_list)
    #             settings.append(element)
    #     else:
    #         # очень важный момент - если у нас указано 0 в количетве счетчиков - то ничего не ставим
    #         Meter_Id_list = GenerateMeterId(count_meter=count_meter, start=0).MeterId
    #         for i in count_setting:
    #             element = {"name": "Test_Name_" + str(i)}
    #             if count_meter > 0:
    #                 element["meters"] = Meter_Id_list
    #             settings.append(element)
    #
    #     return settings
    #
    # def POST(self, count_setting: int = 1, count_meter: int = 3, unique_meter: bool = True):
    #
    #     """
    #     Метод для работы с методом пост
    #     :param unique_meter:
    #     :param count_setting: Количество Элементов в нашей п
    #     :param count_meter:
    #     :return:
    #     """
    #
    #     # Итак - для начала определяем что подали - Если у нас уже спущенные значения - то забиваем на все и ставим
    #     # их с проверкой
    #     if type(count_setting) == list:
    #         settings = self._custom_settings(settings=count_setting)
    #     elif type(count_setting) == int:
    #         settings = self._generate_values(count_setting=count_setting,
    #                                          count_meter=count_meter,
    #                                          unique_meter=unique_meter)
    #     else:
    #         settings = self._generate_values(count_setting=1,
    #                                          count_meter=1,
    #                                          unique_meter=False)
    #
    #     # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
    #     JSON = deepcopy(self.JSON)
    #
    #     JSON["method"] = "post"
    #     JSON["settings"] = list(settings)
    #     # И ОТДАЕМ В ЗАД
    #
    #     return JSON
    #
    # def PUT(self, count_setting: int = 1, count_meter: int = 3, unique_meter: bool = True):
    #
    #     """
    #     Метод для работы с методом пост
    #     :param unique_meter:
    #     :param count_setting: Количество Элементов в нашей п
    #     :param count_meter:
    #     :return:
    #     """
    #
    #     # Итак - для начала определяем что подали - Если у нас уже спущенные значения - то забиваем на все и ставим
    #     # их с проверкой
    #     if type(count_setting) == list:
    #         settings = self._custom_settings(settings=count_setting)
    #     elif type(count_setting) == int:
    #         settings = self._generate_values(count_setting=count_setting,
    #                                          count_meter=count_meter,
    #                                          unique_meter=unique_meter)
    #     else:
    #         settings = self._generate_values(count_setting=1,
    #                                          count_meter=1,
    #                                          unique_meter=False)
    #
    #     # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
    #     JSON = deepcopy(self.JSON)
    #
    #     JSON["method"] = "put"
    #     JSON["settings"] = list(settings)
    #     # И ОТДАЕМ В ЗАД
    #
    #     return JSON
    #
    # def GET(self, names: int):
    #     """
    #     Получение Имени по
    #     Здесь генерируем запрос для получения нужных данных
    #
    #     :param ids: - int - Если задан int , то получаем нужное количество id из БД.При 0 - помещаем туда все ,
    #     если спускаем list / tuple / set - то что поделать вставляем их
    #     :param names:
    #     :return:
    #     """
    #
    #     # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
    #     JSON = deepcopy(self.JSON)
    #
    #     JSON["method"] = "get"
    #
    #     if (type(names) == list) or (type(names) == tuple) or (type(names) == set):
    #         JSON["names"] = list(names)
    #
    #     if names > 0:
    #         names_list = []
    #         for i in range(names):
    #             element = "Test_Name_" + str(i)
    #             names_list.append(element)
    #         JSON["names"] = names_list
    #
    #     return JSON
    #
    #
    #
    #
    #
    #
    #
    #
    #

    # -------------------------------------------------------------------------------------->

    def POST(self, name: int = 1, meter: int = 3, unique_meter: bool = True):
        """
        Метод для работы с с методотом POST
        :param unique_types:
        :param types: - Количество поля, Либо сюда спускаем ВСЕ НАСТРЙОКИ полностью
        :param name: - Либо сюда спускаем ВСЕ НАСТРЙОКИ полностью
        :return:
        """
        from Construct.MeterTemplates.Template_Generate_Settings import GenerateSettings
        from copy import deepcopy

        # Генерируем поле сетттингс

        Settings = deepcopy(GenerateSettings(name=name, meters=meter, unique_meter=unique_meter).settings)

        # Формируем JSON
        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "post"
        JSON["settings"] = list(Settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def PUT(self, name: int = 1, meter: int = 3, unique_meter: bool = True):
        """


        :param name:
        :param types:
        :param unique_types:
        :return:
        """
        from Construct.MeterTemplates.Template_Generate_Settings import GenerateSettings
        from copy import deepcopy

        # Генерируем поле сетттингс

        Settings = deepcopy(GenerateSettings(name=name, meters=meter, unique_meter=unique_meter).settings)

        # Формируем JSON
        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "put"
        JSON["settings"] = list(Settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def GET(self, names):
        """
        :param names:
        :return:
        """
        # Формируем JSON
        JSON = deepcopy(self.JSON)
        # Если У нас имя -  число

        if names > 0:
            from Construct.MeterDataTemplates.Template_Generate_Field_Name import GenerateFieldName

            JSON["names"] = GenerateFieldName(name=names).GET_name_list()

        elif (type(names) == list) or (type(names) == tuple) or (type(names) == set):

            names = list(names)

            for name in range(len(names)):
                names[name] = str(names[name])

            JSON["names"] = names

        JSON["method"] = "get"
        # И ОТДАЕМ В ЗАД
        return JSON
