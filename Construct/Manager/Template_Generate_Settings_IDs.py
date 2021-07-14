# Здесь генирируем наш список SETTINGS


class GenerateSettingsIDs:
    """
    Здесь генерируем Settings с полем ID
    """

    settings = []

    def __init__(self, ids):

        """
        Здесь генерируем Settings с полем ID



        :param ids:
        """

        self.settings = []

        # Если имена только список
        if (type(ids) is list) or (type(ids) is tuple) or (type(ids) is set):
            ids = list(ids)
            settings = self._generate_list(ids=ids)

        elif type(ids) is int:
            settings = self._generate_int(ids=ids)

        else:
            settings = self._generate_int(ids=1)

        self.settings = settings

    def _generate_list(self, ids: list):
        """
        Генерируем наш список - исходя из тех значений что мы спустили

        :param ids:
        :return:
        """
        # сначала ищем ВСЕ айдишники
        idx_list = self._find_all_ID()

        settings = []
        for i in ids:
            if i not in idx_list:
                setting = {'id': i}
                settings.append(setting)

        return settings

    def _generate_int(self, ids: int):
        """
        Генерируем наш список  - по айдишнеикам

        :param ids:
        :return:
        """
        # сначала ищем максимльный айдишник
        idx = self._find_max_ID() + 1
        settings = []
        for i in range(ids):
            setting = {'id': i + idx}
            settings.append(setting)

        return settings

    def _find_max_ID(self):

        """
        Здесь ищем максимальный Айдишник
        :return:
        """
        from Service.SQL import execute_command

        command = 'SELECT MAX(Id) AS Id  FROM Manager'
        result = execute_command(command)
        if len(result) > 0 :
            result = result[0].get('Id')
            if result is None:
                result = 0
        else:
            result = 0
        return result

    def _find_all_ID(self):

        """
        Здесь ищем ВСЕ айдишники
        :return:
        """
        from Service.SQL import execute_command

        command = 'SELECT Id AS Id  FROM Manager'
        result = execute_command(command)

        result_all = []
        if len(result) > 1:
            for i in result:
                value = i.get('Id')
                result_all.append(value)

        return result_all

    def get(self):

        return self.settings
