# Итак - Здесь селектим таблицу Scheduler


class SelectScheduler:
    """

    Класс для работы с таблицей Scheduler

    """

    table = ' Scheduler '

    def __init__(self, JSON):

        self.result = self.execute_dict.get(JSON['method'])(self, JSON['settings'])

    def execute_command(self, command):

        """
        Исполянем команду
        :param command:
        :return:
        """

        from Service.SQL import execute_command

        result = execute_command(command=command)

        return result

    def _select_POST(self, settings):

        """
        Селектим для пост запроса

        :param settings:
        :return:

        """



        # Получаем список айдишников

        ids = []
        print('IJJJJJJ')
        for i in settings:
            idx = i.get('id')
            print(i)
            if idx is not None:
                ids.append(idx)

        # Теперь собираем команду
        fields = ' Id '

        command = ' SELECT ' + ' * ' + ' FROM ' + str(self.table) + ' WHERE ' + fields + ' IN '

        command_ids = ''


        for i in ids:
            command_ids = ' ' + command_ids + str(i) + ' ,'
        print('IJJJJJJ', ids)
        # Теперь обрезаем последнюю запятую

        command_ids = ' ( ' + command_ids[:-1] + ' ) '

        command = command + command_ids + ' ;'

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        return result

    execute_dict = \
        {
            'post': _select_POST
        }
