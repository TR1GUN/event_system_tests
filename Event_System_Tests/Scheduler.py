# Здесь расположим тест для Scheduler
from Event_System_Tests.Template_EventDataAPI import EventDataAPI
from time import sleep

from Template.Template_DataBase_by_JSON import DataBase

class Scheduler(EventDataAPI):
    """
    Этот класс Работает с таблицей Scheduler

    """
    _template_post =  {'table': 'Scheduler', 'method': 'post', 'settings': [{ 'min': 9, 'id': 1}]}
    def POST(self, JSON:dict = _template_post ):
        # Отправляем данные
        Answer = self.SETUP(JSON)
        sleep(2)
        # Теперь селектим что записали
        result = DataBase().SELECT(JSON=JSON)

        print(result)

# Генерируем JSON
from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

JSON = SchedulerJSON().POST()['settings'] + SchedulerJSON().POST()['settings'] + SchedulerJSON().POST()['settings']

JSON = SchedulerJSON().POST(generate=JSON)
print(JSON)

Scheduler().POST(JSON=JSON)

# Scheduler().POST()