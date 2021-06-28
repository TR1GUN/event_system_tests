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

    def POST(self, name, types, unique_types: bool):
        """
        Метод для работы с с методотом POST
        :param unique_types:
        :param types: - Количество поля, Либо сюда спускаем ВСЕ НАСТРЙОКИ полностью
        :param name: - Либо сюда спускаем ВСЕ НАСТРЙОКИ полностью
        :return:
        """
        from Construct.MeterDataTemplates.Template_Generate_Settings import GenerateSettings
        from copy import deepcopy

        # Генерируем поле сетттингс

        Settings = deepcopy(GenerateSettings(name=name, types=types, unique_types=unique_types).settings)

        # Формируем JSON
        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "post"
        JSON["settings"] = list(Settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def PUT(self, name, types, unique_types: bool):
        """


        :param name:
        :param types:
        :param unique_types:
        :return:
        """

        from Construct.MeterDataTemplates.Template_Generate_Settings import GenerateSettings
        from copy import deepcopy

        # Генерируем поле сетттингс

        Settings = deepcopy(GenerateSettings(name=name, types=types, unique_types=unique_types).settings)

        # Формируем JSON
        # ТЕПЕРЬ ЭТО ОБОРАЧИВАЕМ
        JSON = deepcopy(self.JSON)

        JSON["method"] = "post"
        JSON["settings"] = list(Settings)
        # И ОТДАЕМ В ЗАД

        return JSON

    def GET(self, names ):
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

            for name in range(len(names)) :
                names[name] = str(names[name])

            JSON["names"] = names

        JSON["method"] = "get"
        # И ОТДАЕМ В ЗАД
        return JSON