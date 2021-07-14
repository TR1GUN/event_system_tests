# В этом классе генериуем события - ДАП

class GenerateSettingsEventType:
    Event_Types = \
        {
            1: 'Scheduler',
            2: 'Calendar',
            3: 'IntDigitalSensor',
            4: 'ExtDigitalSensor',
            5: 'IntAnalogSensor',
            6: 'ExtAnalogSensor',
        }

    Settings = []

    def __init__(self, settings, EventType):

        """
        Итак Этот класс формирует Поля EventType и Event ID

        :param settings:
        :param EventType:
        """

        self.Settings = []

        # Первое что делаем - ЭТО Подготавливаем нужные нам вещи - а именно ГЕНЕРИУЕМ СПИСОК НЕОБХОДИМЫХ ЭВЕНТОВ
        EventTypes = self._Generate_Event(len_settings=len(settings), EventType=EventType)

        # Получаем айдишники -

        EventID = self._Generation_EventID(len_settings=len(settings))
        # ТЕПЕРЬ ПЕРЕБИРАЕМ все значения и добавляем нужные элементы
        for i in range(len(settings)):
            settings[i]['eventId'] = EventID[i]
            settings[i]['eventType'] = EventTypes[i]

        self.Settings = settings

    def _Generate_Event(self, len_settings, EventType):
        """
        Генерируем список необходимых ЭВЕНТОВ

        :param len_settings:
        :param EventType:
        :return:
        """

        # Первое что смотрим - Если у нас спущен массив -
        if (type(EventType) == list) or (type(EventType) == tuple) or (type(EventType) == set):
            EventType = list(EventType)

            # Получаем все значения
            EventTypes_all = list(self.Event_Types.values())
            # Получаем список который будем подставлять
            EventType_settings = []
            for i in EventType:
                # Если такое сущетсвуеь , то улыбьаемся
                if i in EventTypes_all:
                    EventType_settings.append(i)

            # ТЕПЕРЬ ПОНИМАЕМ СКОЛЬКО НАДО ДОПОЛНИТЬ
            if len_settings > len(EventType_settings):
                # Выясняем сколько нужно добавить
                count_added = len_settings - len(EventType_settings)

                # Генерируем -
                EventType_added = self._generation_EventType_list(count_added)
                EventType_settings = EventType_settings + EventType_added

        else:
            # Иначе генерируем сколько нужно

            # Генерируем -
            EventType_settings = self._generation_EventType_list(len_settings)

        return EventType_settings

    def _generation_EventType_list(self, count):
        """
        Здесь генерируем рандомно какой то из EventType

        :param count:
        :return:
        """

        from random import randint
        EventType = []
        # Получаем максимальные значения ключей - для генерации
        min_key = min(list(self.Event_Types.keys()))
        max_key = max(list(self.Event_Types.keys()))
        for i in range(count):
            element = self.Event_Types[randint(min_key, max_key)]
            EventType.append(element)

        return EventType

    def _Generation_EventID(self,  len_settings):

        """
        Здесь генерируем наши айдишники - это выжно

        :param len_settings:
        :return:
        """

        EventID = []

        # Получаем максимальный айдишник
        eventID_max = self._find_max_Event_ID() + 1

        for i in range(len_settings):

            EventID.append(i+int(eventID_max))

        return EventID

    def _find_max_Event_ID(self):

        """
        ЗАГЛУШКА -
        Поскольку я так и не разобрался к чему ID Event

        Будем ставить МАКСИМАЛЬНЫЙ

        :return:
        """

        from Service.SQL import execute_command

        command = 'SELECT MAX(EventId) AS Id  FROM Manager'
        result = execute_command(command)

        if len(result) > 1:
            result = result[0].get('Id')
            if result is None:
                result = 0
        else:
            result = 0
        return result
