# Здесь расположим класс в котором сгенерируем данные для БД по GET запросу
from Template.Template_SQL_Database import TemplateSQL


class InsertIntoPoller(TemplateSQL):
    """

    Класс для работы с таблицей Poller - Запись данных

    """
    result = None
    table = ' Poller '

    field = {
        'id': 'Id',
        # 'ArchTypesId': 'MeterDataTemplateId',
        # 'MetersNameId': 'MeterTemplateId',
        'ArchTypesId': 'MeterDataTemplateId',
        'MetersNameId': 'MeterTemplateId',
            }
    value_None = ' null '
    table_ArchTypesName = ' MeterDataTemplates '
    field_ArchTypesName = \
        {
            'name': 'TemplateName',
            'Id': "Id"
        }
    table_MetersName = ' MeterTemplates '
    field_table_MetersName = \
        {
            'name': 'TemplateName',
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
        values_by_Poller = []
        # Перебираем все элементы
        for element in data:
            # Получаем айдишники
            ArchTypesId = self._Get_ID_ArchTypesId(element.get("archTypesName"))

            MetersNameId = element.get('metersName')
            if MetersNameId is None:
                MetersNameId = self.value_None
            else:
                MetersNameId = self._Get_ID_MetersNameId(MetersNameId)

            # Формируем наш список
            values_by_Poller.append(
                {
                    'id': element.get('id'),
                    'ArchTypesId': ArchTypesId,
                    'MetersNameId': MetersNameId
                }
            )
            # ТЕПЕРЬ ВСЕ ЭТО ОТПРАВЛЯЕМ НА ЗАПИСЬ
        # ТЕПЕРЬ -
        # Отправляем всю штуку на запись

        result = self._insert_data_to_Poller(values_by_Poller=values_by_Poller)

    def _Get_ID_ArchTypesId(self, archTypesName):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param archTypesName:
        :return:
        """

        select_value = ' ( ' + ' \'' + str(archTypesName) + '\' ' + ' ) '
        # что селектим -
        ID_archTypes = ' Id AS Id '
        # ТАБЛИЦА
        command_select_table = self.table_ArchTypesName

        select_field_where = self.field_ArchTypesName['name']

        command = ' SELECT ' + ID_archTypes + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        # print(command)
        result = self.execute_command(command)
        ArchTypesId = self.value_None
        # Теперь обрабатываем резульатат
        if len(result) > 0:

            for i in result:
                ArchTypesId = i.get(self.field_ArchTypesName['Id'])
            # ЧТОБ НЕ ВЫСТРЕЛИТЬ СЕБЕ В НОГУ
            if ArchTypesId is None:
                ArchTypesId = self.value_None

        return ArchTypesId

    def _Get_ID_MetersNameId(self, MetersNameId):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param MetersNameId:
        :return:
        """
        select_value = ' ( ' + ' \'' + str(MetersNameId) + '\' ' + ' ) '
        # что селектим -
        ID_MetersNameId = ' Id AS Id '
        # ТАБЛИЦА
        command_select_table = self.table_MetersName

        select_field_where = self.field_table_MetersName['name']

        command = ' SELECT ' + ID_MetersNameId + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        result = self.execute_command(command)
        MetersNameId = self.value_None
        # Теперь обрабатываем резульатат
        if len(result) > 0:
            for i in result:
                MetersNameId = i.get(self.field_ArchTypesName['Id'])
            # ЧТОБ НЕ ВЫСТРЕЛИТЬ СЕБЕ В НОГУ
            if MetersNameId is None:
                MetersNameId = self.value_None

        return MetersNameId

    def _insert_data_to_Poller(self, values_by_Poller):

        """
        Здесь Записываем нужные данные
        :param values_by_Poller:
        :return:
        """
        # итак - отделяем мух от котлет

        # Итак - Составляем массив из команд
        command_insert = ' INSERT INTO ' + self.table

        command = ' '
        # сначала делаем строку полей
        command_field = ' '

        # Id, MeterDataTemplateId, MeterTemplateId
        for field_data_base in self.field:
            command_field = command_field + str(self.field.get(field_data_base)) + ' , '

        command_field = command_field[:-2]

        # print(command_field)
        # # получаем необходимые рабочие поля
        Field_all = list(self.field.keys())
        # Теперь берем значения
        for Element in values_by_Poller:

            command_value = ' '

            for field in Field_all:
                value = Element.get(field)
                if value == None:
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
