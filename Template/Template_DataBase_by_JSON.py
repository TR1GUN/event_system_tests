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

    def INSERT(self, JSON):
        """
        Если нам нужно сделать ИНСЕРТ - ЭТО ОЧЕНЬ ВАЖНО

        :return:
        """

        # Получаем JSON

        result = self.INSERT_dict.get(JSON['table'])(self, JSON)

        return result

    def _select_to_Scheduler(self, JSON):
        """
        Выполянмем селект по JSON для таблицы Scheduler
        :param JSON:
        :return:
        """

        from Template.DataBase.Template_Select_Scheduler import SelectScheduler

        result = SelectScheduler(JSON=JSON).result

        return result

    def _insert_to_Scheduler(self, JSON):
        """
        Выполянмем инстерт по JSON для таблицы Scheduler
        :param JSON:
        :return:
        """

        from Template.DataBase.Template_Insert_Data_Scheduler import InsertIntoScheduler

        result = InsertIntoScheduler(JSON=JSON).result

        return result

    def _select_to_MeterTemplates(self, JSON):
        """
        Выполянмем инстерт по JSON для таблицы MeterTemplates
        :param JSON:
        :return:
        """
        from Template.DataBase.Template_Select_MeterTemplates import SelectMeterTemplates

        result = SelectMeterTemplates(JSON=JSON).result

        return result

    def _insert_to_MeterTemplates(self, JSON):
        """
        Выполянмем инстерт по JSON для таблицы Scheduler
        :param JSON:
        :return:
        """

        from Template.DataBase.Template_Insert_Data_MeterTemplates import InsertIntoMeterTemplates

        result = InsertIntoMeterTemplates(JSON=JSON).result

        return result

    def _select_to_MeterDataTemplates(self, JSON):
        """
        Выполянмем инстерт по JSON для таблицы MeterTemplates
        :param JSON:
        :return:
        """
        from Template.DataBase.Template_Select_MeterDataTemplates import SelectMeterDataTemplates

        result = SelectMeterDataTemplates(JSON=JSON).result

        return result

    def _insert_to_MeterDataTemplates(self, JSON):
        """
        Выполянмем инстерт по JSON для таблицы Scheduler
        :param JSON:
        :return:
        """

        from Template.DataBase.Template_Insert_Data_MeterDataTemplates import InsertIntoMeterDataTemplates

        result = InsertIntoMeterDataTemplates(JSON=JSON).result

        return result

    SELECT_dict = \
        {
            'Scheduler': _select_to_Scheduler,
            'MeterTemplates': _select_to_MeterTemplates,
            'MeterDataTemplates': _select_to_MeterDataTemplates
        }

    INSERT_dict = \
        {
            'Scheduler': _insert_to_Scheduler,
            'MeterTemplates': _insert_to_MeterTemplates,
            'MeterDataTemplates': _insert_to_MeterDataTemplates

        }
