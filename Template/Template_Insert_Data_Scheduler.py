# Здесь расположим класс в котором сгенерируем данные для БД по GET запросу
from Template.Template_SQL_Database import TemplateSQL


class InsertIntoScheduler(TemplateSQL):

    result = None

    """

    Класс для работы с таблицей Scheduler - Запись данных

    """

    table = ' Scheduler '

    field = {
        'id': 'Id',
        'mon': 'Mon',
        'day': 'Day',
        'hour': 'Hour',
        'min': 'Min',

            }

    def __init__(self, JSON):
        self.result = self._insert_data(JSON['settings'])

    def _insert_data(self, data):

        """

        Записываем данные

        :param data:
        :return:
        """

        from copy import deepcopy


        # Итак - Составляем массив из команд
        print(data)
        command_insert = ' INSERT INTO ' + self.table

        command = ' '

        for Element in data :
            command_field = ' '
            command_value = ' '
            for field in Element :

                command_field = command_field + str(self.field.get(field)) + ' , '
                command_value = command_value + str(Element.get(field)) + ' , '

            command = command + command_insert + ' ( ' + command_field[:-2] + ' ) ' + ' VALUES ' +\
                                                 ' ( ' + command_value[:-2] + ' ) ' + ' ; '
        print(command)
        # Теперь отправляем в космос

        result = self.execute_command(command)


        return result

    # =========================================================================================================









