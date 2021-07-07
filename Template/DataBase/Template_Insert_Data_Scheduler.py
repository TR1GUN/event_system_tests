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
        # итак - отделяем мух от котлет

        # Итак - Составляем массив из команд
        print(data)
        command_insert = ' INSERT INTO ' + self.table

        command = ' '
        # сначала делаем строку полей
        command_field = ' '
        for field_data_base in self.field:
            command_field = command_field + str(self.field.get(field_data_base)) + ' , '

        command_field = command_field[:-2]
        # получаем необходимые рабочие поля
        Field_all = list(self.field.keys())
        # Теперь берем значения
        for Element in data:

            command_value = ' '

            for field in Field_all:
                value = Element.get(field)
                if value == None :
                    value = 'Null'
                command_value = command_value + str(value) + ' , '

            # Слупливаем это
            command = command + ' ( ' + command_value[:-2] + ' ) , '

        command = command[:-2]

        command = command_insert + ' ( ' + command_field + ' ) ' + ' VALUES ' + command  + ' ; '

        # print(command)
        # Теперь отправляем в космос

        result = self.execute_command(command)

        return result

    def _update_data(self):

        pass
        # Итак - если у нас уже этот айдишник есть - перезаписываем значения
    # =========================================================================================================
