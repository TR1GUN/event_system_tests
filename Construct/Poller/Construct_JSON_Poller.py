from copy import deepcopy
from Construct.Template_Construct_JSON import TemplateJSON


class PollerJSON(TemplateJSON):
    """
    Класс который конструирует JSON для таблицы Poller

    """

    custom_data = {}

    JSON = {"table": "Poller"}

    def __init__(self, custom_data: list = []):
        self.custom_data = custom_data

    def GET(self, ids=0):

        # Формируем JSON
        JSON = deepcopy(self.JSON)
        # Если У нас имя -  число

        if ids > 0:
            from Construct.MeterDataTemplates.Template_Generate_Field_Name import GenerateFieldName

            JSON["ids"] = GenerateFieldName(name=ids).GET_name_list()

        elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):

            ids = list(ids)

            for idx in range(len(ids)):
                ids[idx] = str(ids[idx])

            JSON["ids"] = ids

        JSON["method"] = "get"
        # И ОТДАЕМ В ЗАД
        return JSON

    # def PUT(self, ):
