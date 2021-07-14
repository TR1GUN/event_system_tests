# Здесь расположим класс в котором сгенерируем данные для БД по GET запросу
from Template.Template_SQL_Database import TemplateSQL


class InsertIntoManager(TemplateSQL):
    """

    Класс для работы с таблицей Manager - Запись данных

    """
    result = None
    table = ' Manager '

    # ВСЕ ПОЛЯ ОСНОВНОЙ ТАБЛИЦЫ
    field = {
        'id': 'Id',
        'eventType': 'EventTypeId',
        'eventId': 'EventId',
        'actionType': 'ActionTypeId',
        'actionId': 'ActionId',
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
        values_by_Manager = []
        # Перебираем все элементы
        for element in data:
            # Получаем айдишники
            ActionTypeId = self._Get_ID_ActionType(element.get("actionType"))

            EventTypeId = self._Get_ID_EventType(element.get("eventType"))

            # Формируем наш список
            values_by_Manager.append(
                {
                    'id': element.get('id'),
                    'actionType': ActionTypeId,
                    'actionId': element.get('actionId'),
                    'eventType': EventTypeId,
                    'eventId': element.get('eventId'),

                }
            )
            # ТЕПЕРЬ ВСЕ ЭТО ОТПРАВЛЯЕМ НА ЗАПИСЬ
        # ТЕПЕРЬ -
        # Отправляем всю штуку на запись

        result = self._insert_data_to_Manager(values_by_Manager=values_by_Manager)

        return result

    def _Get_ID_ActionType(self, ActionType):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param archTypesName:
        :return:
        """

        select_value = ' ( ' + ' \'' + str(ActionType) + '\' ' + ' ) '
        # что селектим -
        ID_ActionType = ' Id AS Id '
        # ТАБЛИЦА
        command_select_table = self.table_ActionTypes

        select_field_where = self.field_table_ActionTypes['actionType']

        command = ' SELECT ' + ID_ActionType + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        # print(command)
        result = self.execute_command(command)
        ActionTypeId = self.value_None
        # Теперь обрабатываем резульатат
        if len(result) > 0:
            for i in result:
                ActionTypeId = i.get(self.field_table_ActionTypes['Id'])
            # ЧТОБ НЕ ВЫСТРЕЛИТЬ СЕБЕ В НОГУ
            if ActionTypeId is None:
                ActionTypeId = self.value_None

        return ActionTypeId

    def _Get_ID_EventType(self, EventType):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param EventType:
        :return:
        """

        select_value = ' ( ' + ' \'' + str(EventType) + '\' ' + ' ) '
        # что селектим -
        ID_EventType = ' Id AS Id '
        # ТАБЛИЦА
        command_select_table = self.table_EventTypes

        select_field_where = self.field_table_EventTypes['eventType']

        command = ' SELECT ' + ID_EventType + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        # print(command)
        result = self.execute_command(command)
        EventTypeId = self.value_None
        # Теперь обрабатываем резульатат
        if len(result) > 0:
            for i in result:
                EventTypeId = i.get(self.field_table_EventTypes['Id'])
            # ЧТОБ НЕ ВЫСТРЕЛИТЬ СЕБЕ В НОГУ
            if EventType is None:
                EventTypeId = self.value_None

        return EventTypeId

    def _insert_data_to_Manager(self, values_by_Manager):

        """
        Здесь Записываем нужные данные
        :param values_by_Manager:
        :return:
        """
        # итак - отделяем мух от котлет

        # Итак - Составляем массив из команд
        command_insert = ' INSERT INTO ' + self.table

        command = ' '
        # сначала делаем строку полей
        command_field = ' '

        # ЗАПИСЫАЕМ ПОЛЯ
        for field_data_base in self.field:
            command_field = command_field + str(self.field.get(field_data_base)) + ' , '

        command_field = command_field[:-2]

        # print(command_field)
        # # получаем необходимые рабочие поля
        Field_all = list(self.field.keys())
        # Теперь берем значения
        for Element in values_by_Manager:

            command_value = ' '

            for field in Field_all:
                value = Element.get(field)
                if value is None:
                    value = 'Null'
                command_value = command_value + str(value) + ' , '

            # Слупливаем это
            command = command + ' ( ' + command_value[:-2] + ' ) , '

        command = command[:-2]
        #
        command = command_insert + ' ( ' + command_field + ' ) ' + ' VALUES ' + command + ' ; '

        # print(command)
        # Теперь отправляем в космос

        result = self.execute_command(command)

        return result
