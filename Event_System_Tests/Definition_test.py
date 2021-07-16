# Здесь расположим параметризаторы тестов


class DefineTest:
    """

    Этот класс нужен для параметризации тестов - ЭТО ВАЖНО


    """
    result = None

    def __init__(self, JSON):
        self.result = self._definition_table(JSON=JSON)

    def _definition_table(self, JSON):
        """

        Здесь определяем наши таблицы

        :param JSON:
        :return:
        """

        # Получаем JSON
        result = self.table_dict.get(JSON['table'])(self, JSON)

        return result

    def _test_to_Scheduler(self, JSON):
        """
        Мы определили таблицу Scheduler, теперь определяем метод

        :param JSON:
        :return:
        """
        from Event_System_Tests.Scheduler import Scheduler

        result = self.method_dict.get(JSON['method'])(self, JSON, Scheduler)

        return result


    def _test_to_MeterTemplates(self, JSON):

        """
        Выбрали таблицу MeterTemplates
        :param JSON:
        :return:
        """

        from Event_System_Tests.MeterTemplates import MeterTemplates

        result = self.method_dict.get(JSON['method'])(self, JSON, MeterTemplates)

        return result

    def _test_to_MeterDataTemplates(self, JSON):
        """
        Выбрали таблицу MeterTemplates
        :param JSON:
        :return:
        """

        from Event_System_Tests.MeterDataTemplates import MeterDataTemplates

        result = self.method_dict.get(JSON['method'])(self, JSON, MeterDataTemplates)

        return result

    def _test_to_Poller(self, JSON):
        """
        Выбрали таблицу Poller
        :param JSON:
        :return:
        """

        from Event_System_Tests.Poller import Poller

        result = self.method_dict.get(JSON['method'])(self, JSON, Poller)

        return result

    def _test_to_Manager(self, JSON):
        """
        Выбрали таблицу Poller
        :param JSON:
        :return:
        """

        from Event_System_Tests.Manager import Manager

        result = self.method_dict.get(JSON['method'])(self, JSON, Manager)

        return result

    def _SETUP_POST(self, JSON, TEST):
        """
        Здесь запускаем метод POST
        :param JSON:
        :param TEST:
        :return:
        """

        result = TEST().POST(JSON=JSON)

        return result

    def _SETUP_PUT(self, JSON, TEST):
        """
        Здесь запускаем метод POST
        :param JSON:
        :param TEST:
        :return:
        """

        result = TEST().PUT(JSON=JSON)

        return result

    def _SETUP_GET(self, JSON, TEST):
        """
        Здесь запускаем метод POST
        :param JSON:
        :param TEST:
        :return:
        """

        result = TEST().GET(JSON=JSON)

        return result

    def _SETUP_DELETE(self, JSON, TEST):
        """
        Здесь запускаем метод POST
        :param JSON:
        :param TEST:
        :return:
        """

        result = TEST().DELETE(JSON=JSON)

        return result

    def get_result(self):

        return self.result

    # ---------------->
    table_dict = \
        {
            'Scheduler': _test_to_Scheduler,
            'MeterTemplates': _test_to_MeterTemplates,
            'MeterDataTemplates': _test_to_MeterDataTemplates,
            'Poller': _test_to_Poller,
            'Manager': _test_to_Manager,
        }

    method_dict = \
        {
            'get': _SETUP_GET,
            'delete': _SETUP_DELETE,
            'put': _SETUP_PUT,
            'post': _SETUP_POST,
        }
