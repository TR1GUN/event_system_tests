# Здесь расположим класс в котором сгенерируем данные для БД по GET запросу
from Template.Template_SQL_Database import TemplateSQL


class InsertIntoMeterDataTemplates(TemplateSQL):
    """

    Класс для работы с таблицей MeterTemplates - Запись данных

    """
    result = None
    # Таблица для прописывания имени
    table_MeterDataTemplates = ' MeterDataTemplates '
    # Таблица для прописывания счетчиков
    table_MeterDataTemplateArray = ' MeterDataTemplateArray '

    # Поля Таблицы для прописывания имени
    field_table_MeterDataTemplates = \
        {
            'name': 'TemplateName',
            'id': 'Id',
        }

    # Поля Таблицы для прописывания счетчиков
    field_table_MeterDataTemplateArray = \
        {
            'id': 'Id',
            'name': 'MeterDataTemplateId',
            'types': 'ArchTypeName',
        }

    def __init__(self, JSON):
        self.result = self._insert_data(JSON['settings'])

    def _insert_data(self, data):

        """

        Записываем данные

        :param data:
        :return:
        """
        result = None

        # итак - отделяем мух от котлет
        # Перебираем вест массив

        for setting in data:
            # Сначала апгрейд им найм
            name = setting.get('name')
            # Отправляем на запись
            if name is not None:
                # Инсертим таблицу MeterTemplates
                result = self._insert_MeterDataTemplates(name=name)

                types = setting.get('types')

                # Очищаем айдишники
                nameId = result.get('id')
                if (types is not None) and (nameId is not None):
                    nameId = int(nameId)
                    # Записываем айдишники
                    result = self._insert_MeterDataTemplateArray(TypesTemplateId=nameId, TypesId=types)

        return result

    def _insert_MeterDataTemplateArray(self, TypesTemplateId: int, TypesId: list):
        """
        ЭТОТ МЕТОД НУЖЕН ДЛЯ ИНСЕРТА  таблицу MeterTemplateArray
        :param MeterTemplateId: Первичный ключ из MeterTemplates
        :param MeterId: список ид счетчиков
        :return:
        """

        # ТЕПЕРЬ собираем команду -
        command_insert = ' INSERT INTO ' + self.table_MeterDataTemplateArray + ' '

        # сначала делаем строку полей
        command_field = ' ( ' + self.field_table_MeterDataTemplateArray['name'] + ' , ' + \
                        self.field_table_MeterDataTemplateArray['types'] + ' ) '

        # ТЕПЕРЬ формируем values
        command_values = ''

        for type in TypesId:
            command_values = command_values + ' ( ' + str(TypesTemplateId) + ' , ' + '\'' + str(type) + '\'' + ' ) , '

        command_values = command_values[:-2]

        command_values = ' VALUES ' + command_values

        command = command_insert + command_field + command_values + ' ; '

        # Отправляем ее на запись
        result = self.execute_command(command)

        return result

    def _insert_MeterDataTemplates(self, name):

        """
        Этот метод нужен для того чтоб записать поле NAME и отдать его айдишник
        :param name: САМО значение NAME
        :return: Отдает его первичный ключ в БД
        """
        # Итак - Составляем массив из команд
        name = '\'' + str(name) + '\''
        command_insert = ' INSERT INTO ' + self.table_MeterDataTemplates + \
                         ' ( ' + self.field_table_MeterDataTemplates['name'] + ' ) ' \
                         + ' VALUES ' + \
                         ' ( ' + name + ' ) ' + \
                         ' ; '

        # Отправляем ее на запись

        result = self.execute_command(command_insert)

        # Теперь селектим то что записали

        # ЗАБИРАЕМ ПОЛЯ

        fields = ''

        for field in self.field_table_MeterDataTemplates:
            fields = fields + self.field_table_MeterDataTemplates[field] + ' AS ' + field + ' , '

        fields = fields[:-2]

        # Собираем команду - ТИМ КУК
        command_select = ' SELECT ' + fields + ' FROM ' + self.table_MeterDataTemplates + ' WHERE ' + \
                         self.field_table_MeterDataTemplates['name'] + ' = ' + name

        # Отправляем ее на запись
        result = self.execute_command(command_select)

        # Очищаем
        result = self._find_id(result)
        return result

    def _find_id(self, result):

        """
        Этот метод нужен дял вытаскивания первого айдишника
        :param result:
        :return:
        """
        if len(result) > 0:
            result = result[0]
        else:
            result = {'name': None, 'id': None}
        return result

    def _update_data(self):

        pass
        # Итак - если у нас уже этот айдишник есть - перезаписываем значения
    # =========================================================================================================
