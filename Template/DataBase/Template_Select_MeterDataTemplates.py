# итак - тут расположим файл для селекта наших записей MeterTemplates
from Template.Template_SQL_Database import TemplateSQL


class SelectMeterDataTemplates(TemplateSQL):
    """

    Класс для работы с таблицей Scheduler

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

        self.result = self.execute_dict.get(JSON['method'])(self, JSON)

    def _added_MeterTemplateArray(self, settings):

        """
        Метод добавляющий поле счетчиков - ЭТО ОЧЕНЬ ВАЖНО
        :param settings:
        :return:
        """

        for element in settings:

            idx = element.get('id')
            types = self._select_MeterDataTemplateArray(MeterDataTemplateId=idx)
            if len(types) > 0:
                element['types'] = types
            # Удаляем айдишник
            element.pop('id')

        return settings

    def _select_MeterDataTemplateArray(self, MeterDataTemplateId):

        """
        Итак - Здесь формируем список из таблицы MeterTemplateArray
        :param MeterDataTemplateId:
        :return:
        """

        # Теперь собираем команду :

        # Поля связи - первичный ключ имени MeterTemplateId
        fields = self.field_table_MeterDataTemplateArray['name']
        # Поля счетчиков
        select_fields = ' ' + self.field_table_MeterDataTemplateArray['types'] + ' AS  types '

        # Собираем наши айтишники

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_MeterDataTemplateArray) + \
                  ' WHERE ' + fields + ' IN ' + ' ( ' + str(MeterDataTemplateId) + ' ) '

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        meters = []

        for meter in result:
            meters.append(meter.get('types'))

        return meters

    def _select_POST(self, JSON):

        """
        Селектим для пост запроса

        :param JSON:
        :return:

        """
        settings = JSON.get('settings')
        # Получаем список всех имен

        Names = []
        for i in settings:
            name = i.get('name')
            if name is not None:
                Names.append(name)

        # Теперь собираем команду
        fields = ' TemplateName '

        select_fields = ' ' + \
                        self.field_table_MeterDataTemplates['name'] + ' AS name' + \
                        ' , ' + \
                        self.field_table_MeterDataTemplates['id'] + ' AS id'

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_MeterDataTemplates) + ' WHERE ' + fields + ' IN '

        command_ids = ''

        for i in Names:
            command_ids = ' ' + command_ids + '\'' + str(i) + '\'' + ' ,'

        # Теперь обрезаем последнюю запятую

        command_ids = ' ( ' + command_ids[:-1] + ' ) '

        command = command + command_ids + ' ;'

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        result = self._added_MeterTemplateArray(settings=result)

        return result

    def _select_GET(self, JSON):
        """
        Селектим для GET запроса

        :param JSON:
        :return:
        """
        # Получаем список айдишников

        names = JSON.get("names")

        # итак - Если у нас None - то селектим все - Иначе - Только по айдишникам
        if names is None:

            command_names = ' '

        else:
            command_names = ''

            for i in names:
                command_names = ' ' + command_names + '\'' + str(i) + '\'' + ' ,'

            # Теперь обрезаем последнюю запятую

            command_names = ' ( ' + command_names[:-1] + ' ) '

            fields = self.field_table_MeterDataTemplates['name']

            command_names = ' WHERE ' + fields + ' IN ' + command_names

        # # Теперь собираем команду

        select_fields = ' ' + \
                        self.field_table_MeterDataTemplates['name'] + ' AS name' + \
                        ' , ' + \
                        self.field_table_MeterDataTemplates['id'] + ' AS id'

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_MeterDataTemplates)

        command = command + command_names + ' ;'

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        result = self._added_MeterTemplateArray(settings=result)

        return result

    def _select_DELETE(self, JSON):
        """
        Селектим для DELETE запроса

        :param settings:
        :return:
        """
        # Получаем список айдишников

        names = JSON.get("names")

        # итак - Если у нас None - то селектим все - Иначе - Только по айдишникам
        if names is None:

            command_names = ' '

        else:
            command_names = ''

            for i in names:
                command_names = ' ' + command_names + '\'' + str(i) + '\'' + ' ,'

            # Теперь обрезаем последнюю запятую

            command_names = ' ( ' + command_names[:-1] + ' ) '

            fields = self.field_table_MeterDataTemplates['name']

            command_names = ' WHERE ' + fields + ' IN ' + command_names

        # # Теперь собираем команду

        select_fields = ' ' + \
                        self.field_table_MeterDataTemplates['name'] + ' AS name' + \
                        ' , ' + \
                        self.field_table_MeterDataTemplates['id'] + ' AS id'

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_MeterDataTemplates)

        command = command + command_names + ' ;'

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        result = self._added_MeterTemplateArray(settings=result)

        return result

    def _select_PUT(self, JSON):

        """
        Селектим для PUT запроса- Селектим все

        :param settings:
        :return:

        """
        settings = JSON.get('settings')

        # Теперь собираем команду
        fields = ' TemplateName '

        select_fields = ' ' + \
                        self.field_table_MeterDataTemplates['name'] + ' AS name' + \
                        ' , ' + \
                        self.field_table_MeterDataTemplates['id'] + ' AS id'

        command = ' SELECT ' + select_fields + ' FROM ' + str(self.table_MeterDataTemplates)

        # И запускаем ее в космос

        result = self.execute_command(command=command)

        result = self._added_MeterTemplateArray(settings=result)

        return result

    # =========================================================================================================
    execute_dict = \
        {
            'post': _select_POST,
            'put': _select_PUT,
            'get': _select_GET,
            'delete': _select_DELETE,
        }
