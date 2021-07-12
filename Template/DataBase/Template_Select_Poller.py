# итак - тут расположим файл для селекта наших записей MeterTemplates
from Template.Template_SQL_Database import TemplateSQL


class SelectPoller(TemplateSQL):
    """

    Класс для работы с таблицей Scheduler

    """

    # result = None
    # # Таблица для прописывания имени
    # table_MeterDataTemplates = ' MeterDataTemplates '
    # # Таблица для прописывания счетчиков
    # table_MeterDataTemplateArray = ' MeterDataTemplateArray '
    #
    # # Поля Таблицы для прописывания имени
    # field_table_MeterDataTemplates = \
    #     {
    #         'name': 'TemplateName',
    #         'id': 'Id',
    #     }
    #
    # # Поля Таблицы для прописывания счетчиков
    # field_table_MeterDataTemplateArray = \
    #     {
    #         'id': 'Id',
    #         'name': 'MeterDataTemplateId',
    #         'types': 'ArchTypeName',
    #     }
    result = None
    table = ' Poller '

    field = {
        'id': 'Id',
        # 'ArchTypesId': 'MeterDataTemplateId',
        # 'MetersNameId': 'MeterTemplateId',
        'ArchTypesId': 'MeterDataTemplateId',
        'MetersNameId': 'MeterTemplateId',
    }
    value_None = '\'Null\''
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

        self.result = self.execute_dict.get(JSON['method'])(self, JSON)

    def _Get_Name_ArchTypesId(self, archTypesID):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param archTypesName:
        :return:
        """

        select_value = ' ( ' + str(archTypesID) + ' ) '
        # что селектим -
        ID_archTypes = ' TemplateName AS archTypesName '
        # ТАБЛИЦА
        command_select_table = self.table_ArchTypesName

        select_field_where = self.field_ArchTypesName['Id']

        command = ' SELECT ' + ID_archTypes + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        # print(command)
        result = self.execute_command(command)
        ArchTypesName = None
        # Теперь обрабатываем резульатат
        for i in result:
            ArchTypesName = i.get('archTypesName')
        return ArchTypesName

    def _Get_Name_MetersNameId(self, MetersNameId):
        """
        Итак - Здесь ищем  айдишник в таблице

        :param MetersNameId:
        :return:
        """
        select_value = ' ( ' + ' \'' + str(MetersNameId) + '\' ' + ' ) '
        # что селектим -
        ID_MetersNameId = ' TemplateName AS metersName '
        # ТАБЛИЦА
        command_select_table = self.table_MetersName

        select_field_where = self.field_table_MetersName['Id']

        command = ' SELECT ' + ID_MetersNameId + ' FROM ' + command_select_table \
                  + " WHERE " \
                  + select_field_where + ' IN ' + select_value

        result = self.execute_command(command)
        metersName = None
        # Теперь обрабатываем резульатат
        for i in result:
            metersName = i.get('metersName')

        return metersName

    def _select_POST(self, JSON):

        """
        Селектим для пост запроса

        :param JSON:
        :return:

        """
        settings = JSON.get('settings')
        # Получаем список всех имен

        # select_fields = ' Id AS id , MeterDataTemplateId AS ArchTypesId , MetersNameId AS MeterTemplateId '

        # Собираем поля для селекта
        select_fields = ''

        for field in self.field:
            select_fields = select_fields + ' ' + self.field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        fields_id = self.field['id']

        # Теперь собираем все айдишники
        command_id = ''
        for setting in settings:
            command_id = command_id + str(setting.get('id')) + ' , '

        command_id = command_id[:-2]

        # Собираем
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table) + \
                  ' WHERE ' + fields_id + ' IN ' + ' ( ' + command_id + ' ) '

        # Получаем
        print(command)
        TablePoller = self.execute_command(command=command)

        print(TablePoller)

        result = []
        for element in TablePoller:
            element_poller = {}
            # Сначала добавляем айдишник
            element_poller['id'] = element.get('id')
            # ТЕПЕРЬ ИЩЕМ archTypesName
            element_poller['archTypesName'] = self._Get_Name_ArchTypesId(archTypesID=element.get('ArchTypesId'))
            # ТЕПЕРЬ ИЩЕМ metersName
            element_poller['archTypesName'] = self._Get_Name_MetersNameId(MetersNameId=element.get('MetersNameId'))

            # Добавляем
            result.append(element_poller)

        return result

    def _select_GET(self, JSON):
        """
        Селектим для GET запроса

        :param JSON:
        :return:
        """
        # Получаем список айдишников

        ids = JSON.get("id")

        print('---->',ids)
        # Собираем поля для селекта
        select_fields = ''

        for field in self.field:
            select_fields = select_fields + ' ' + self.field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]
        # Теперь собираем все айдишники

        if (ids is not None) and (len (ids) > 0):
            fields_id = self.field['id']
            command_id = ''
            for idx in ids:
                command_id = command_id + str(idx) + ' , '

            command_id = command_id[:-2]
            # Собираем
            command = ' SELECT ' + select_fields + ' FROM ' + str(self.table) + \
                      ' WHERE ' + fields_id + ' IN ' + ' ( ' + command_id + ' ) '

        else:
            command = ' SELECT ' + select_fields + ' FROM ' + str(self.table)

        # Получаем
        print(command)
        TablePoller = self.execute_command(command=command)

        print(TablePoller)

        result = []
        for element in TablePoller:
            element_poller = {}
            # Сначала добавляем айдишник
            element_poller['id'] = element.get('id')
            # ТЕПЕРЬ ИЩЕМ archTypesName
            element_poller['archTypesName'] = self._Get_Name_ArchTypesId(archTypesID=element.get('ArchTypesId'))
            # ТЕПЕРЬ ИЩЕМ metersName
            element_poller['archTypesName'] = self._Get_Name_MetersNameId(MetersNameId=element.get('MetersNameId'))

            # Добавляем
            result.append(element_poller)

        print('aboba',result)

        return result

    def _select_DELETE(self, JSON):
        """
        Селектим для DELETE запроса

        :param settings:
        :return:
        """
        # Получаем список айдишников

        # Получаем список айдишников

        ids = JSON.get("id")

        print('---->', ids)
        # Собираем поля для селекта
        select_fields = ''

        for field in self.field:
            select_fields = select_fields + ' ' + self.field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        if (ids is not None) and (len(ids) > 0):
            fields_id = self.field['id']
            command_id = ''
            for idx in ids:
                command_id = command_id + str(idx) + ' , '

            command_id = command_id[:-2]
            # Собираем
            command = ' SELECT ' + select_fields + ' FROM ' + str(self.table) + \
                      ' WHERE ' + fields_id + ' IN ' + ' ( ' + command_id + ' ) '

        else:
            command = ' SELECT ' + select_fields + ' FROM ' + str(self.table)

        # Получаем
        print(command)
        TablePoller = self.execute_command(command=command)

        print(TablePoller)

        result = []
        for element in TablePoller:
            element_poller = {}
            # Сначала добавляем айдишник
            element_poller['id'] = element.get('id')
            # ТЕПЕРЬ ИЩЕМ archTypesName
            element_poller['archTypesName'] = self._Get_Name_ArchTypesId(archTypesID=element.get('ArchTypesId'))
            # ТЕПЕРЬ ИЩЕМ metersName
            element_poller['archTypesName'] = self._Get_Name_MetersNameId(MetersNameId=element.get('MetersNameId'))

            # Добавляем
            result.append(element_poller)

        print('aboba', result)

        return result

    def _select_PUT(self, JSON):

        """
        Селектим для PUT запроса- Селектим все

        :param settings:
        :return:

        """
        settings = JSON.get('settings')
        # Получаем список всех имен

        # select_fields = ' Id AS id , MeterDataTemplateId AS ArchTypesId , MetersNameId AS MeterTemplateId '

        # Собираем поля для селекта
        select_fields = ''

        for field in self.field:
            select_fields = select_fields + ' ' + self.field[field] + ' AS ' + field + ' , '

        select_fields = select_fields[:-2]

        # Собираем
        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table)

        # Получаем
        print(command)
        TablePoller = self.execute_command(command=command)

        print(TablePoller)

        result = []
        for element in TablePoller:
            element_poller = {}
            # Сначала добавляем айдишник
            element_poller['id'] = element.get('id')
            # ТЕПЕРЬ ИЩЕМ archTypesName
            element_poller['archTypesName'] = self._Get_Name_ArchTypesId(archTypesID=element.get('ArchTypesId'))
            # ТЕПЕРЬ ИЩЕМ metersName
            element_poller['archTypesName'] = self._Get_Name_MetersNameId(MetersNameId=element.get('MetersNameId'))

            # Добавляем
            result.append(element_poller)

        return result

    # =========================================================================================================
    execute_dict = \
        {
            'post': _select_POST,
            'put': _select_PUT,
            'get': _select_GET,
            'delete': _select_DELETE,
        }
