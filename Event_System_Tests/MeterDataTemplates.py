# Здесь расположим тест для Scheduler
from Event_System_Tests.Template_EventDataAPI import EventDataAPI
from time import sleep

from Template.Template_DataBase_by_JSON import DataBase

from Template.CheckUp_MeterDataTemplates import CheckUpGET, CheckUpPUT, CheckUpPOST, CheckUpDELETE


class MeterDataTemplates(EventDataAPI):
    """

    Этот класс Работает с таблицей MeterTemplates

    """
    _template_post = {"method": "post", "table": "MeterDataTemplates", "settings": [{"name": "lol", "types": ["test"]}]}
    _template_put = {"method": "put", "table": "MeterDataTemplates", "settings": [{"name": "%2%2%2"}]}
    _template_get = {"method": "get", "table": "MeterDataTemplates"}
    _template_delete = {"method": "delete", "table": "MeterDataTemplates"}

    # //----------------------------------             POST запрос        ------------------------------------------
    def POST(self, JSON: dict = _template_post):

        """
        Метод для тестирования POST запроса
        :param Тестовый JSON что отправляем
        :return:
        """
        print(JSON)
        # Отправляем данные
        Answer = self.SETUP(JSON)
        sleep(2)
        # Теперь селектим что записали
        data_base = DataBase().SELECT(JSON=JSON)
        print('data_base', data_base)

        # ТЕПЕРЬ - Отправляем в сравнивыатель
        if Answer['res'] == 0:
            result = CheckUpPOST(JSON=JSON['settings'], data_base=data_base).error
        else:
            result = Answer
        print(result)

        return result

    # //----------------------------------             PUT запрос        ------------------------------------------

    def PUT(self, JSON: dict = _template_put):

        """
        Метод Для тестирования PUT запроса
        :param JSON: Тестовый JSON что отправляем
        :return:
        """

        # Отправляем данные

        Answer = self.SETUP(JSON)
        sleep(2)
        # Теперь селектим что записали
        data_base = DataBase().SELECT(JSON=JSON)
        print('data_base', data_base)
        print(JSON['settings'])
        # ТЕПЕРЬ - Отправляем в сравниватель
        if Answer['res'] == 0:
            result = CheckUpPUT(JSON=JSON['settings'], data_base=data_base).error
        else:
            result = Answer
        print(result)

        return result

    # //----------------------------------             GET запрос        ------------------------------------------
    def GET(self, JSON: dict = _template_get, ):
        """
        Метод для тестирования GET запроса

        :param JSON: Тестовый JSON что отправляем
        :return:
        """
        print(JSON)
        # итак - что делаем - мы селектим все что у нас есть
        # Теперь селектим что записали
        data_base = DataBase().SELECT(JSON=JSON)
        print(data_base)
        # Отправляем данные
        Answer = self.SETUP(JSON)
        # ТЕПЕРЬ - Отправляем в сравниватель
        if Answer['res'] == 0:
            result = CheckUpGET(JSON=Answer['settings'], data_base=data_base).error
        else:
            result = Answer

        print(result)

        return result

    # //----------------------------------             DELETE запрос        ------------------------------------------
    def DELETE(self, JSON: dict = _template_delete, ):
        """
        Метод для тестирования

        :param JSON:
        :return:
        """

        # итак - что делаем - мы селектим все что у нас есть
        # Теперь селектим что записали
        database_before = DataBase().SELECT(JSON=self._template_delete)
        print(database_before)
        # Отправляем данные

        Answer = self.SETUP(JSON)
        sleep(2)

        # Теперь селектим что записали
        database_after = DataBase().SELECT(JSON=self._template_delete)
        print('database_after', database_after)
        # ТЕПЕРЬ - Отправляем в сравнивыатель
        if Answer['res'] == 0:
            result = CheckUpDELETE(JSON=JSON, database_after=database_after, database_before=database_before).error
        else:
            result = Answer
        print(result)

        return result


# //-----------------------------------------------------------------------------------------------------------------
# //-----------------------------------------------------------------------------------------------------------------
#                                           тестовые запуски
# //-----------------------------------------------------------------------------------------------------------------
# //-----------------------------------------------------------------------------------------------------------------
# # ТУT все серьезно. генерируем данные по ID
# from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
#
# JSON = MeterDataTemplatesJSON().DELETE()
# print('lolol',JSON)
#
# # Генерируем JSON
# MeterDataTemplates().DELETE()
#
#
# a = MeterDataTemplates(name=[{'name': '3', 'types': ['3', '2', '1']}], types=3, unique_types=False).GET()
#
# print(a)


JSON_param = {
            # Либо количество автосгенерирвоанных имен, либо список имен для генерации , либо Полноценный JSON
            'name': 1,
            # либо количество ArchTypes для автогенерации либо список ArchTypes
            'types': 3,
            # Уникальны ли ArchTypes для каждого name
            'unique_types': True,
            # ИМЕНА которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'names': 1,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None,
        }

# from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
# JSON = MeterDataTemplatesJSON(name=JSON_param.get('name'),
#                                   types=JSON_param.get('types'),
#                                   unique_types=JSON_param.get('unique_types')).GET(
#         custom_settings=JSON_param.get('custom_settings')
#     )
#
#
#
# print(JSON)
# result = MeterDataTemplates(Type_Connect='virtualbox').GET(JSON=JSON)
