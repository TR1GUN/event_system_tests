# Здесь расположим тестовый класс
# Здесь расположим тест для Scheduler
from Event_System_Tests.Template_EventDataAPI import EventDataAPI
from time import sleep

from Template.Template_DataBase_by_JSON import DataBase

from Template.CheckUP_Manager import CheckUpGET, CheckUpPUT, CheckUpPOST, CheckUpDELETE


class Manager(EventDataAPI):
    """

    Этот класс Работает с таблицей MeterTemplates

    """
    _template_post ={"method":"post", "table":"Manager", "settings":[{"id":1, "eventId":1, "eventType":"Scheduler", "actionId":2, "actionType":"Poller"}]}
    _template_put = {"method":"put", "table":"Manager", "settings":[{"id":1, "eventId":1, "eventType":"Scheduler", "actionId":2, "actionType":"Poller"}]}
    _template_get = {"method":"get", "table":"Manager"}
    _template_delete = {"method":"delete", "table":"Manager"}

    # //----------------------------------             POST запрос        ------------------------------------------
    def POST(self, JSON: dict = _template_post):

        """
        Метод для тестирования POST запроса
        :param Тестовый JSON что отправляем
        :return:
        """

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
        # print(JSON['settings'])
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

        # итак - что делаем - мы селектим все что у нас есть
        # Теперь селектим что записали
        data_base = DataBase().SELECT(JSON=JSON)
        print('data_base', data_base)
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
    def DELETE(self, JSON: dict = _template_delete ):
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
# ТУT все серьезно. генерируем данные по ID
from Construct.Manager.Construct_JSON_Manager import ManagerJSON

JSON = ManagerJSON(ids=3, EventType=3, ActionType=3).DELETE(ids=2)

Manager().DELETE(JSON=JSON)
