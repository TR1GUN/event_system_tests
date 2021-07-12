# здесь генерируем наши настройки - Это важно


class GenerateSettingsPoller:
    """
    В этом классе генерируем поле Settings для JSON Poller

    """

    # Количество типов данных что записывается в таблицу для каждого элемента таблицы MeterDataTemplates
    ArchTypes = 2
    # Количество типов данных что записывается в таблицу для каждого элемента таблицы MeterTemplates
    CountMeter = 2
    # ОЧЕНЬ ВАЖНЫЙ ПАРАМЕТР - ГЕНЕАРЦИЯ - от максимального чила ил с 0
    generate_of_max = False
    settings = []

    def __init__(self,
                 ids: int = 1,
                 metersName: int = 1,
                 archTypesName: int = 1,
                 generate_of_max: bool = True,
                 ArchTypes: int = 2,
                 CountMeter: int = 2
                 ):
        """
        Здесь генерируем наш Settings для JSON

        :param ids: - Либо готовый  Settings , либо список айдишников, либо число сколько генерирвоать
        :param metersName:  либо список имен, либо число сколько генерирвоать
        :param archTypesName: либо список имен, либо число сколько генерирвоать
        :param generate_of_max: - Булевый параметр - идет от наибольшего айдишника или нет
        :param ArchTypes: Количество генерируемых ArchTypes
        :param CountMeter: Количество генерируемых счетчиков
        """
        # Итак - основная логика работы -

        # ИТАК ПОГНАЛИ
        self.settings = []
        self.generate_of_max = bool(generate_of_max)
        if type(ArchTypes) == int:
            self.ArchTypes = ArchTypes
        if type(CountMeter) == int:
            self.CountMeter = CountMeter

        # Сначала получаем вспомогательные данные
        # ----->
        # ЕСЛИ У НАС ЧИСЛО
        if type(ids) == int:
            # Генерируем список из айдишников
            settings = self._Generate_Settings_IDS_int(ids=ids)
            # ТЕПЕРЬ ДОСТРАИВАЕМ ИМЯ
            settings = self._Generate_Settings_metersName_archTypesName(Settings=settings,
                                                                        MetersName=metersName,
                                                                        ArchTypesName=archTypesName
                                                                        )

        # Если имена только список
        elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            # ПРОВЕРЯЕМ ЧАСТНЫЙ ВАРИАНТ ЭТОГО- мы подали все верно
            if type(ids[0]) == dict:
                settings = FieldPollerCheckUP(settings=ids).settings
                # ЕСЛИ НЕ получилось - ГЕНЕРИРУЕМ ОДНО
                # ----->
                if len(settings) < 1:
                    settings = self._Generate_Settings_IDS_int(ids=1)
                    # ТЕПЕРЬ ДОСТРАИВАЕМ ИМЯ
                    settings = self._Generate_Settings_metersName_archTypesName(
                        Settings=settings,
                        MetersName=1,
                        ArchTypesName=1
                    )
            # ----->
            # ЕСЛИ ЭТО СПИСОК ИЗ ИМЕН - оставляем все как есть
            elif type(ids[0]) == str:
                # Заполняем Айдишниками из листа
                settings = self._Generate_Settings_IDS_list(ids=ids)
                # ТЕПЕРЬ ДОСТРАИВАЕМ ИМЯ
                settings = self._Generate_Settings_metersName_archTypesName(
                    Settings=settings,
                    MetersName=metersName,
                    ArchTypesName=archTypesName
                )

            else:
                settings = []
        # ----->
        else:
            settings = self._Generate_Settings_IDS_int(ids=1)
            # ТЕПЕРЬ ДОСТРАИВАЕМ ИМЯ
            settings = self._Generate_Settings_metersName_archTypesName(
                Settings=settings,
                MetersName=1,
                ArchTypesName=1
            )

        # ----->

        self.settings = settings

    # --------------------------------------------------------------------------------------------------------->
    #                                           ГЕНЕРАЦИЯ ПОЛЯ id
    # --------------------------------------------------------------------------------------------------------->
    def _Generate_Settings_IDS_int(self, ids):

        """
        Итак - у нас тут идет генерация необходимого количества
        :param ids:
        :return:
        """
        settings = []
        # Первое - узнаем откуда ведем генерацию
        start = self._find_max_id_Poller()
        start = int(start) + 1
        # ТЕПЕРЬ формируем
        for i in range(ids):
            setting = {
                'id': start + i,
            }
            settings.append(setting)

        return settings

    def _Generate_Settings_IDS_list(self, ids):

        """
        Итак - у нас тут идет генерация необходимого количества
        :param ids:
        :return:
        """
        if len(ids) > 0:
            settings = []
            # ТЕПЕРЬ формируем
            for i in ids:
                setting = \
                    {
                        'id': i,
                    }
                settings.append(setting)
        else:
            settings = self._Generate_Settings_IDS_int(ids=1)

        return settings

    # --------------------------------------------------------------------------------------------------------->
    #                                           ГЕНЕРАЦИЯ ПОЛЕЙ metersName и archTypesName
    # --------------------------------------------------------------------------------------------------------->
    def _Generate_Settings_archTypesName(self, Settings, ArchTypesName):

        """
        Здесь генерируем наши ArchTypesName - Це важно

        :param Settings:
        :param ArchTypesName:
        :return:

        """
        # ПОЛЕ ОБЯЗАТЕЛЬНО
        # НУЖНЫЕ ЖОПОЛНИТЕЛЬНЫЕ ШТУКИ - Если задали меньше

        ArchTypesName_added = []
        # Если у нас лист и у нас их не ХВАТАЕТ!!!
        if (type(ArchTypesName) in [list, tuple, set]) and (len(ArchTypesName) < len(Settings)):
            # находим разницу
            added = len(Settings) - len(ArchTypesName)
            # И Генерируем ее
            ArchTypesName_added = self._generate_MeterDataTemplateId(archTypesName=added)
        # Если у нас инт и у нас их не ХВАТАЕТ!!!
        if (type(ArchTypesName) == int) and (ArchTypesName < len(Settings)):
            # находим разницу
            added = len(Settings) - ArchTypesName
            # И Генерируем ее
            ArchTypesName_added = self._generate_MeterDataTemplateId(archTypesName=added)

        # Теперь генерируем все
        ArchTypesNameSettings = self._generate_MeterDataTemplateId(archTypesName=ArchTypesName)

        ArchTypesNameSettings = ArchTypesNameSettings + ArchTypesName_added

        # ТЕПЕРЬ Дополняем наш сеттинг
        for i in range(len(Settings)):
            Settings[i]['archTypesName'] = ArchTypesNameSettings[i]['name']

        # print('Settings' , Settings)
        #
        # print('ArchTypesNameSettings', ArchTypesNameSettings)

        return Settings

    def _Generate_Settings_metersName(self, Settings, MetersName):

        """
        Здесь генерируем наши ArchTypesName - Це важно

        :param Settings:
        :param MetersName:
        :return:

        """
        # Теперь генерируем все
        MetersNameNameSettings = self._generate_MeterTemplateId(metersName=MetersName)

        # ТЕПЕРЬ Дополняем наш сеттинг
        for i in range(len(MetersNameNameSettings)):
            Settings[i]['metersName'] = MetersNameNameSettings[i]['name']

        return Settings

    def _Generate_Settings_metersName_archTypesName(self, Settings, MetersName, ArchTypesName):
        """
        Общий метод для генерации полей metersName и archTypesName

        :param metersName:
        :param archTypesName:
        :return:
        """

        # ТЕПЕРЬ - Очень важный момент - СООТНОШЕНИЯ

        # СНАЧАЛА ГЕНЕРИРУЕМ ArchTypesName - ЭТО ПОЛЕ ОБЯЗАТЕЛЬНО
        # ОНО ДОЛЖНО БЫТЬ ОДИНАКОВОЙ ДЛИНЫ ЧТО и наши айдишники
        if type(ArchTypesName) in [list, int, tuple, set]:
            Settings = self._Generate_Settings_archTypesName(Settings=Settings, ArchTypesName=ArchTypesName)
        else:
            Settings = self._Generate_Settings_archTypesName(Settings=Settings, ArchTypesName=len(Settings))

        # ТЕПЕРЬ ДОПОЛНЯЕМ НАШ список metersName
        if type(MetersName) in [list, int, tuple, set]:
            Settings = self._Generate_Settings_metersName(Settings=Settings, MetersName=MetersName)

        return Settings

    # --------------------------------------------------------------------------------------------------------->
    #                                           Служебные методы
    # --------------------------------------------------------------------------------------------------------->
    def _find_max_value(self):
        """
        В Этом методе ищем максимальное значение

        :return:
        """
        from Service.SQL import execute_command
        command = 'SELECT MAX(Id) AS Id FROM Poller ; '

        max_id = execute_command(command=command)

        # idx = None
        for i in max_id:
            idx = i.get('Id')
        if idx is None:
            idx = 0

        return idx

    def _find_max_id_Poller(self):

        """
        Здесь узнаем с кого числа мы генерируем наш Id
        :return:
        """
        if self.generate_of_max:
            start = self._find_max_value()
        else:
            start = 0

        return start

    def _generate_MeterDataTemplateId(self, archTypesName):

        """
        Здесь генерируем имена

        :param metersName:
        :return:
        """

        from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON

        # ИТАК - ГЕНЕРИРУЕМ и СРАЗУ ЗАПИСЫВАЕМ В БД
        # print(archTypesName)
        MeterDataTemplate = MeterDataTemplatesJSON(name=archTypesName, types=self.ArchTypes)
        MeterDataTemplate.RecordData()
        MeterDataTemplate_Id = MeterDataTemplate.Generate_data

        # print(MeterDataTemplate_Id)

        return MeterDataTemplate_Id

    def _generate_MeterTemplateId(self, metersName):

        """
        Здесь генерируем имена

        :param metersName:
        :return:
        """

        from Construct.MeterTemplates.Construct_JSON_MeterTemplates import MeterTemplatesJSON

        # ИТАК - ГЕНЕРИРУЕМ и СРАЗУ ЗАПИСЫВАЕМ В БД
        MeterTemplate = MeterTemplatesJSON(name=metersName, meter=self.CountMeter)
        MeterTemplate.RecordData()
        MeterTemplateId = MeterTemplate.Generate_data

        # ТЕПЕРЬ СЕЛЕКТИМ ВСЕ ДАННЫЕ

        # print(MeterTemplateId)

        return MeterTemplateId


# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
#                                           Класс проверки корректности JSON
# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
class FieldPollerCheckUP:
    """

    Здесь проверяем корректность формирования полей

    """
    settings = []
    # Поле айдишника
    field_ID = 'id'
    # Обязательное Поле
    field_Mandatory = 'archTypesName'
    # Дополнительное Поле
    field_Additional = 'metersName'

    def __init__(self, settings):
        """
        Здесь проверяем корректность формирования полей
        :param settings:

        """
        settings_normal = []

        # ПЕРЕБИРАЕМ ВСЕ ЭЛЕМЕНТЫ
        for setting in settings:
            # setting_normal= {}
            # проверяем наличие айдишника и обязхательного поля
            if (type(setting.get(self.field_ID)) == int) and (setting.get(self.field_Mandatory) is not None):
                # Если да - То добавляем всю эту кучку в новый словарь
                setting_normal = {
                    self.field_ID: setting.get(self.field_ID),
                    self.field_Mandatory: setting.get(self.field_Mandatory),
                }
                # Добавляем дополнительный айдишник
                if setting.get(self.field_Additional) is not None:
                    setting_normal[self.field_Additional] = setting.get(self.field_Additional)

                settings_normal.append(setting_normal)

        self.settings = settings_normal


# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
#                       класс ДЛЯ ФОРМИРОВАНИЯ поля id ДЯЛ GET\DELETE запроса
# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
class GenerateIdPoller:
    """
    Класс для формирования поля Names

    """
    ids = []

    def __init__(self, ids=0, settings=[{"id": 1, "hour": 4, "min": 18}]):
        """
        Конструктор

        :param ids:
        :param settings:

        """
        # сначала получаем все names что есть
        all_ids = set()
        for i in settings:
            all_ids.add(i.get('id'))

        all_ids = list(all_ids)

        # ЕСЛИ у нас int
        if (type(ids) == int) and (ids > 0):

            # чтоб не выстрелить себе в ногу
            if ids > len(all_ids):
                ids = len(all_ids)

            # ТЕПЕРЬ - ставим нужные names из сгенерированных
            from random import randint
            idx = set()
            while len(idx) < ids:
                idx.add(all_ids[randint(0, (len(all_ids) - 1))])
            ids = list(idx)

        # ЕСЛИ У НАС СПИСОК - Проверяем - все ли айдишники есть
        elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            # Теперь перебираем все names
            ids_list = []
            for idx in ids:
                if idx in all_ids:
                    ids_list.append(idx)
            ids = ids_list

        else:
            ids = []

        self.ids = ids
