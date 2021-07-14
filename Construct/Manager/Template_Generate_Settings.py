class GenerateSettingsManager:
    """
    В этом классе генерируем поле Settings для JSON Manager

    """

    settings = []

    def __init__(self,
                 # Количенство айдишников что мы генерим , либо их с список , либо ПОЛНОЦЕННЫЙ JSON
                 ids: int = 1,
                 # Либо сам тип - str/int либо список из всего этого добра
                 EventType: list = [],
                 # Либо сам тип - str/int либо список из всего этого добра
                 ActionType: list = []
                 ):
        """
        В этом классе генерируем поле Settings для JSON Manager

        :param ids: Количество айдишников что мы генерим , либо их с список , либо ПОЛНОЦЕННЫЙ JSON
        :param EventType: Либо сам тип - str/int либо список из всего этого добра
        :param ActionType: Либо сам тип - str/int либо список из всего этого добра
        """
        # Итак - погнали.
        self.settings = []
        # ПЕРВОЕ ЧТО ДЕЛАЕМ - РАЗБИРАЕМ АЙДИШНИКИ
        if type(ids) is int:
            # Доп проверка чтоб не выстрелить себе в ногу
            if ids < 1:
                ids = 1
            # Итак тогда - генерируем Поля айди
            settings = self._Generate_Template_Settings(ids=ids)
            # Теперь генерируем поля actionType
            settings = self._Generate_Template_ActionType(settings=settings, ActionType=ActionType)
            # Теперь генерируем поля eventType
            settings = self._Generate_Template_EventType(settings=settings, EventType=EventType)

        # Если имена только список
        elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            # ЗДЕСЬ ВСЕ МОЖЕТ ИЗМЕНИТЬСЯ ОТ СЛОВА СОВСЕМ
            ids = list(ids)
            # Проверяем сначала из чего состоит наш список
            # ЕСЛИ из уже готового JSON - проверяем его на корректность
            if type(ids[0]) is dict:
                settings = self._Field_Manager_CheckUp(settings=ids)
            else:
                # Итак тогда - генерируем Поля айди
                settings = self._Generate_Template_Settings(ids=ids)
                # Теперь генерируем поля actionType
                settings = self._Generate_Template_ActionType(settings=settings, ActionType=ActionType)
                # Теперь генерируем поля eventType
                settings = self._Generate_Template_EventType(settings=settings, EventType=EventType)

        # Иначе - генериурем стандарт
        else:
            settings = self._Generate_Template_Settings(ids=1)
            # Теперь генерируем поля actionType
            settings = self._Generate_Template_ActionType(settings=settings, ActionType=ActionType)
            # Теперь генерируем поля eventType
            settings = self._Generate_Template_EventType(settings=settings, EventType=EventType)

        self.settings = settings

    def _Generate_Template_Settings(self, ids):

        """
        В этом методе получаем шаблон Settings с уже сформированными полями ID и самое важное - ТОЛЬКО С НИМИ
        :param ids:
        :return:
        """

        from Construct.Manager.Template_Generate_Settings_IDs import GenerateSettingsIDs
        from copy import deepcopy
        # сначала генериурем сам сеттингс
        settings = deepcopy(GenerateSettingsIDs(ids=ids).settings)

        # ПОСЛЕ ЕГО ДОСТРАИВАЕМ

        return settings

    def _Generate_Template_EventType(self, settings, EventType):
        """
        Генерируем поле EventType и EventID

        :param settings:
        :param EventType:
        :return:
        """

        from Construct.Manager.Template_Generate_Settings_Event_Type import GenerateSettingsEventType
        from copy import deepcopy
        # сначала генериурем сам сеттингс
        settings = deepcopy(GenerateSettingsEventType(settings=settings, EventType=EventType).Settings)

        # ПОСЛЕ ЕГО ДОСТРАИВАЕМ

        return settings

    def _Generate_Template_ActionType(self, settings, ActionType):
        """
        Генерируем поле EventType и EventID

        :param settings:
        :param ActionType:
        :return:
        """

        from Construct.Manager.Template_Generate_Settings_ActionType import GenerateSettingsActionType
        from copy import deepcopy
        # сначала генериурем сам сеттингс
        settings = deepcopy(GenerateSettingsActionType(settings=settings, ActionType=ActionType).Settings)

        # ПОСЛЕ ЕГО ДОСТРАИВАЕМ

        return settings

    def _Field_Manager_CheckUp(self, settings):

        """
        В этом методе проверяем корректность нашего JSON
        :param settings:
        :return:
        """
        from copy import deepcopy
        # сначала генериурем сам сеттингс
        settings = deepcopy(FieldManagerCheckUP(settings=settings).settings)

        # еслт не вышло -то генерируем
        if len(settings) < 1:
            settings = self._Generate_Template_Settings(ids=1)
            # Теперь генерируем поля actionType
            settings = self._Generate_Template_ActionType(settings=settings, ActionType=1)
            # Теперь генерируем поля eventType
            settings = self._Generate_Template_EventType(settings=settings, EventType=1)

        return settings


# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
#                                           Класс проверки корректности JSON
# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
class FieldManagerCheckUP:
    """

    Здесь проверяем корректность формирования полей

    """
    settings = []
    # Поле айдишника
    field_ID = 'id'
    # Обязательное Поля
    field_EventId = "eventId"
    field_EventType = "eventType"
    field_ActionId = "actionId"
    field_ActionType = "actionType"

    def __init__(self, settings):
        """
        Здесь проверяем корректность формирования полей
        :param settings:

        """
        settings_normal = []

        # ПЕРЕБИРАЕМ ВСЕ ЭЛЕМЕНТЫ
        for setting in settings:
            # setting_normal= {}
            # проверяем наличие айдишника и обязательного поля
            if (type(setting.get(self.field_ID)) is int) and \
                    (type(setting.get(self.field_EventId)) is int) and \
                    (type(setting.get(self.field_ActionId)) is int):
                # Если да - То добавляем всю эту кучку в новый словарь
                setting_normal = {
                    self.field_ID: setting.get(self.field_ID),
                    self.field_EventId: setting.get(self.field_EventId),
                    self.field_ActionId: setting.get(self.field_ActionId),
                }
                # Добавляем Поля - самих дейсвтвий
                if (setting.get(self.field_EventType) is not None) and (setting.get(self.field_ActionType) is not None):

                    setting_normal[self.field_EventType] = setting.get(self.field_EventType)
                    setting_normal[self.field_ActionType] = setting.get(self.field_ActionType)
                # ЕСЛи их нет - ставим значения по умолчанию
                else:
                    setting_normal[self.field_EventType] = 'Scheduler'
                    setting_normal[self.field_ActionType] = 'Poller'

                settings_normal.append(setting_normal)

        self.settings = settings_normal


# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
#                       класс ДЛЯ ФОРМИРОВАНИЯ поля id ДЯЛ GET\DELETE запроса
# // ---------------------------------------------------------------------------------------------------------//
# // ---------------------------------------------------------------------------------------------------------//
class GenerateIdManager:
    """
    Класс для формирования поля Names

    """
    ids = []

    def __init__(self, ids=0, settings=[{"id":1, "eventId":1, "eventType":"Scheduler", "actionId":2, "actionType":"Poller"}]):
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


# -------------------------------------------------------------------------------------->
# -------------------------------------------------------------------------------------->
