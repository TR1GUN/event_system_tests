class ReConstructSchedulerJSON:
    JSON = []

    def __init__(self):
        self.JSON = []

    def GET_from_POSTorPUT(self, JSON):

        """
        Итак - что делаем - переделываем ИЗ ПОСТ-ПУТ ЗАПРСОА ГЕТ ЗАПРОС
        :param JSON: СЮДА пихаем наш
        :return: Нормальный JSON
        """
        from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

        # так - если у нас словарь

        if (type(JSON) == dict) and (type(JSON.get('settings')) == list):
            settings = JSON.get('settings')
            ids = []

            for setting in settings:
                ids.append(setting.get('id'))


        else:
            ids = 0
        JSON = SchedulerJSON().GET(ids=ids)
        return JSON
