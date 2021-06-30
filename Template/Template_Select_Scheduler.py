# Итак - Здесь селектим таблицу Scheduler
from Template.Template_SQL_Database import TemplateSQL


class SelectScheduler(TemplateSQL):
    """

    Класс для работы с таблицей Scheduler

    """

    table = ' Scheduler '

    def __init__(self, JSON):

        self.result = self.execute_dict.get(JSON['method'])(self, JSON['settings'])

    def _select_POST(self, settings):

        """
        Селектим для пост запроса

        :param settings:
        :return:

        """

        # Получаем список айдишников

        ids = []

        for i in settings:
            idx = i.get('id')
            if idx is not None:
                ids.append(idx)

        # Теперь собираем команду
        fields = ' Id '

        select_fields = ' Id AS id , Mon AS mon ,  Day AS day , Hour AS hour , Min AS min '

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table) + ' WHERE ' + fields + ' IN '

        command_ids = ''

        for i in ids:
            command_ids = ' ' + command_ids + str(i) + ' ,'

        # Теперь обрезаем последнюю запятую

        command_ids = ' ( ' + command_ids[:-1] + ' ) '

        command = command + command_ids + ' ;'

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        return result

    def _select_PUT(self, settings):

        """
        Селектим для пост запроса

        :param settings:
        :return:

        """

        # Теперь собираем команду

        select_fields = ' Id AS id , Mon AS mon ,  Day AS day , Hour AS hour , Min AS min '

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table)

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        return result

    # =========================================================================================================
    execute_dict = \
        {
            'post': _select_POST,
            'put': _select_PUT
        }
