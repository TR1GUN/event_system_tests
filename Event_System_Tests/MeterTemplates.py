# Здесь расположим тест для Scheduler
from Event_System_Tests.Template_EventDataAPI import EventDataAPI
from time import sleep

from Template.Template_DataBase_by_JSON import DataBase


# from Event_System_Tests.CheckUp import CheckUpGET , CheckUpPUT ,CheckUpPOST ,CheckUpDELETE

class MeterTemplates(EventDataAPI):
    """

    Этот класс Работает с таблицей MeterTemplates

    """
    _template_post = {"method": "post", "table": "MeterTemplates", "settings": [{"name": "pupkin", "meters": [1]}]}
    _template_put = {"method": "put", "table": "MeterTemplates", "settings": [{"name": "tester"}]}
    _template_get = {"method": "get", "table": "MeterTemplates"}
    # _template_delete = {"method": "delete", "table": "Scheduler"}
