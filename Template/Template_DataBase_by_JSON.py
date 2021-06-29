# Здесь Пытаемся Заселектить по JSON то что должны получить


class DataBase:
    """
    Данный класс  Работает с БД Получает
    """

    JSON = {}

    def __init__(self):
        self.JSON = {}

    def SELECT(self, JSON):
        """
        Если нам нужно сделать селект - ЭТО ОЧЕНЬ ВАЖНО

        :return:
        """

        # Получаем JSON
        result = self.SELECT_dict.get(JSON['table'])(self, JSON)

        return result

    def _select_to_Scheduler(self, JSON):
        """
        Выполянмем селект по JSON для таблицы Scheduler
        :param JSON:
        :return:
        """

        from Template.Template_Select_Scheduler import SelectScheduler

        result = SelectScheduler(JSON=JSON).result

        return result

    SELECT_dict = {
        'Scheduler': _select_to_Scheduler

                 }
