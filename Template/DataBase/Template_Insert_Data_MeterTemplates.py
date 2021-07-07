# Здесь расположим класс в котором сгенерируем данные для БД по GET запросу
from Template.Template_SQL_Database import TemplateSQL


class InsertIntoMeterTemplates(TemplateSQL):
    """

    Класс для работы с таблицей MeterTemplates - Запись данных

    """
    result = None
    # Таблица для прописывания имени
    table_MeterTemplates = ' MeterTemplates '
    # Таблица для прописывания счетчиков
    table_MeterTemplateArray = ' MeterTemplateArray '

    # Поля Таблицы для прописывания имени
    field_table_MeterTemplates = \
        {
            'name': 'TemplateName',
            'id': 'Id',
        }

    # Поля Таблицы для прописывания счетчиков
    field_table_MeterTemplateArray = \
        {
            'id': 'Id',
            'meters': 'MeterId',
            'name': 'MeterTemplateId',
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
                result = self._insert_MeterTemplates(name=name)

                meters = setting.get('meters')

                # Очищаем айдишники
                nameId = result.get('id')
                if (meters is not None) and (nameId is not None):
                    nameId = int(nameId)
                    # Записываем айдишники
                    result = self._insert_MeterTemplateArray(MeterTemplateId=nameId, MeterId=meters)

        return result

    def _insert_MeterTemplateArray(self, MeterTemplateId: int, MeterId: list):
        """
        ЭТОТ МЕТОД НУЖЕН ДЛЯ ИНСЕРТА  таблицу MeterTemplateArray
        :param MeterTemplateId: Первичный ключ из MeterTemplates
        :param MeterId: список ид счетчиков
        :return:
        """

        # ТЕПЕРЬ собираем команду -
        command_insert = ' INSERT INTO ' + self.table_MeterTemplateArray + ' '

        # сначала делаем строку полей
        command_field = ' ( ' + self.field_table_MeterTemplateArray['name'] + ' , ' + \
                        self.field_table_MeterTemplateArray['meters'] + ' ) '

        # ТЕПЕРЬ формируем values
        command_values = ''

        for meter in MeterId:
            command_values = command_values + ' ( ' + str(MeterTemplateId) + ' , ' + str(meter) + ' ) , '

        command_values = command_values[:-2]

        command_values = ' VALUES ' + command_values

        command = command_insert + command_field + command_values + ' ; '

        # Отправляем ее на запись
        result = self.execute_command(command)

        return result

    def _insert_MeterTemplates(self, name):

        """
        Этот метод нужен для того чтоб записать поле NAME и отдать его айдишник
        :param name: САМО значение NAME
        :return: Отдает его первичный ключ в БД
        """
        # Итак - Составляем массив из команд
        name = '\'' + str(name) + '\''
        command_insert = ' INSERT INTO ' + self.table_MeterTemplates + \
                         ' ( ' + self.field_table_MeterTemplates['name'] + ' ) ' \
                         + ' VALUES ' + \
                         ' ( ' + name + ' ) ' + \
                         ' ; '

        # Отправляем ее на запись

        result = self.execute_command(command_insert)

        # Теперь селектим то что записали

        # ЗАБИРАЕМ ПОЛЯ

        fields = ''

        for field in self.field_table_MeterTemplates:
            fields = fields + self.field_table_MeterTemplates[field] + ' AS ' + field + ' , '

        fields = fields[:-2]

        # Собираем команду - ТИМ КУК
        command_select = ' SELECT ' + fields + ' FROM ' + self.table_MeterTemplates + ' WHERE ' + \
                         self.field_table_MeterTemplates['name'] + ' = ' + name


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
