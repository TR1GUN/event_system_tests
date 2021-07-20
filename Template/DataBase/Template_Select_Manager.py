# Здесь селектим все то что ДОЛЖНЫ

# итак - тут расположим файл для селекта наших записей MeterTemplates
from Template.Template_SQL_Database import TemplateSQL


class SelectManager(TemplateSQL):
    """

    Класс для работы с таблицей Manager

    """

    result = None
    table = 'Manager'
    table_all = ' Manager  , EventTypes , ActionTypes '
    # ВСЕ ПОЛЯ ОСНОВНОЙ ТАБЛИЦЫ
    field = {
        'id': 'Id',
        'eventType': 'EventTypeId',
        'eventId': 'EventId',
        'actionType': 'ActionTypeId',
        'actionId': 'ActionId',
    }

    select_field = {
        'id': 'Manager.Id',
        'eventType': 'EventTypes.EventName',
        'eventId': 'Manager.EventId',
        'actionType': 'ActionTypes.ActionName',
        'actionId': 'Manager.ActionId',
    }

    # НУЛЕВОЕ ЗНАЧЕНИЕ
    value_None = ' null '

    # ----->
    table_EventTypes = ' EventTypes '
    field_table_EventTypes = \
        {
            'eventType': 'EventName',
            'Id': "Id"
        }

    # ----->
    table_ActionTypes = ' ActionTypes '
    field_table_ActionTypes = \
        {
            'actionType': 'ActionName',
            'Id': "Id"
        }

    # ----->
    # Здесь устанавливаем связь таблиц через условие WHERE
    relations_table_where = ' Manager.EventTypeId = EventTypes.Id AND  Manager.ActionTypeId = ActionTypes.Id '

    # ----->

    def __init__(self, JSON):

        self.result = self.execute_dict.get(JSON['method'])(self, JSON)

    def _select_POST(self, JSON):

        """
        Селектим для пост запроса

        :param JSON:
        :return:

        """
        settings = JSON.get('settings')
        # Получаем список всех имен
        # Собираем поля для селекта
        select_fields = ''

        for field in self.select_field:
            select_fields = select_fields + ' ' + self.select_field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        fields_id = self.field['id']

        # Теперь собираем все айдишники
        command_id = ''
        for setting in settings:
            command_id = command_id + str(setting.get('id')) + ' , '

        command_id = command_id[:-2]

        # Собираем

        # селект + поля + фром + все таблицы + условия связи + анд + нужные значения
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_all) + ' ' +\
                  ' WHERE ' + str(self.relations_table_where) \
                  + ' AND ' +\
                  str(self.table) + '.' + str(fields_id) + ' IN ' + ' ( ' + command_id + ' ) '

        print(command)
        # Получаем
        result = self.execute_command(command=command)

        return result

# -------------->
    def _select_GET(self, JSON):
        """
        Селектим для GET запроса

        :param JSON:
        :return:
        """
        # Начинаем с другого - собираемнужные поля

        # Получаем список айдишников

        ids = JSON.get("ids")

        # Собираем поля для селекта
        select_fields = ''

        for field in self.select_field:
            select_fields = select_fields + ' ' + self.select_field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        # Теперь формируем выборку по условиям
        command_id = ''
        # ЕСЛИ У НАС ЧТО ТО ЕСТЬ
        if (ids is not None) and (len(ids) > 0):
            # Берем само поле что нам надо попасть в выборку

            fields_id = ' AND ' + str(self.table) + '.' + str(self.field['id'])
            # Перебираем все что есть - и пихаем все это в команду
            for idx in ids:
                command_id = command_id + str(idx) + ' , '
            # Обрезаем
            command_id = command_id[:-2]

            command_id = fields_id + ' IN ' + ' ( ' + command_id + ' ) '
        # ТЕПЕРЬ СОБИРАЕМ НАШЕ СЧАСТЬЕ

        # селект + поля + фром + все таблицы + условия связи + анд + нужные значения
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_all) + ' ' + \
                      ' WHERE ' + str(self.relations_table_where) + command_id

        print(command)
        # Получаем
        result = self.execute_command(command=command)

        return result

    def _select_DELETE(self, JSON):
        """
        Селектим для DELETE запроса

        :param settings:
        :return:
        """
        # Начинаем с другого - собираемнужные поля

        # Получаем список айдишников

        ids = JSON.get("ids")

        # Собираем поля для селекта
        select_fields = ''

        for field in self.select_field:
            select_fields = select_fields + ' ' + self.select_field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        # Теперь формируем выборку по условиям
        command_id = ''
        # ЕСЛИ У НАС ЧТО ТО ЕСТЬ
        if (ids is not None) and (len(ids) > 0):
            # Берем само поле что нам надо попасть в выборку

            fields_id = ' AND ' + str(self.table) + '.' + str(self.field['id'])
            # Перебираем все что есть - и пихаем все это в команду
            for idx in ids:
                command_id = command_id + str(idx) + ' , '
            # Обрезаем
            command_id = command_id[:-2]

            command_id = fields_id + ' IN ' + ' ( ' + command_id + ' ) '
        # ТЕПЕРЬ СОБИРАЕМ НАШЕ СЧАСТЬЕ

        # селект + поля + фром + все таблицы + условия связи + анд + нужные значения
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_all) + ' ' + \
                      ' WHERE ' + str(self.relations_table_where) + command_id

        print('-->', command)
        print('command_id-->', command_id)
        # Получаем
        result = self.execute_command(command=command)

        return result

    def _select_PUT(self, JSON):

        """
        Селектим для PUT запроса- Селектим все

        :param settings:
        :return:

        """
        settings = JSON.get('settings')
        # Получаем список всех имен
        # Собираем поля для селекта
        select_fields = ''

        for field in self.select_field:
            select_fields = select_fields + ' ' + self.select_field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]


        # Собираем

        # селект + поля + фром + все таблицы + условия связи + анд + нужные значения
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_all) + ' ' +\
                  ' WHERE ' + str(self.relations_table_where)

        print(command)
        # Получаем
        result = self.execute_command(command=command)

        return result

    # =========================================================================================================
    execute_dict = \
        {
            'post': _select_POST,
            'put': _select_PUT,
            'get': _select_GET,
            'delete': _select_DELETE,
        }
