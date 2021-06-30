# Здесь расположим тест для Scheduler
from Event_System_Tests.Template_EventDataAPI import EventDataAPI
from time import sleep

from Template.Template_DataBase_by_JSON import DataBase


class Scheduler(EventDataAPI):
    """
    Этот класс Работает с таблицей Scheduler

    """
    _template_post = {'table': 'Scheduler', 'method': 'post', 'settings': [{'min': 9, 'id': 1}]}
    _template_put = {'table': 'Scheduler', 'method': 'put', 'settings': [{'min': 9, 'id': 1}]}
    _template_get = {"method": "get", "table": "Scheduler"}

    def POST(self, JSON: dict = _template_post):
        # Отправляем данные
        Answer = self.SETUP(JSON)
        sleep(2)
        # Теперь селектим что записали
        result = DataBase().SELECT(JSON=JSON)
        print(result)
        print(JSON['settings'])
        assert result == JSON['settings']


    def PUT(self, JSON: dict = _template_put):
        # Отправляем данные
        Answer = self.SETUP(JSON)
        sleep(2)
        # Теперь селектим что записали
        result = DataBase().SELECT(JSON=JSON)
        print(result)
        print(JSON['settings'])
        assert result == JSON['settings']


    def GET(self, JSON: dict = _template_post, ):
        """
        Метод для тестирования

        :param JSON:
        :return:
        """

        # Первое - Записываем POST запрос

        record = DataBase().INSERT(JSON=JSON)
# ТУT все серьезно. генерируем данные по ID

# Генерируем JSON
from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
#
JSON = SchedulerJSON().POST(generate=3)['settings'] + SchedulerJSON().POST()['settings'] + SchedulerJSON().POST()[
    'settings']
#
JSON = SchedulerJSON().POST(generate=JSON)


# print(JSON)


# JSON = '''{'table': 'Scheduler', 'method': 'put', 'settings': []}'''
# Scheduler().PUT(JSON=JSON)

# Scheduler().POST()

Scheduler().GET(JSON=JSON)