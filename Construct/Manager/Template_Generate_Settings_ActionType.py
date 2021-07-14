# В этом классе генериуем события - ДАП

class GenerateSettingsActionType:
    Action_Types = \
        {
            1: 'Poller',
            2: 'IntRelay',
            3: 'ExtRelay',
            4: 'MQTTMeterMessages',
            5: 'SMTPMeterMessages',
        }

    Settings = []

    def __init__(self, settings, ActionType):

        """
        Итак Этот класс формирует Поля EventType и Event ID

        :param settings:
        :param ActionType:
        """

        self.Settings = []

        # Первое что делаем - ЭТО Подготавливаем нужные нам вещи - а именно ГЕНЕРИУЕМ СПИСОК НЕОБХОДИМЫХ ЭВЕНТОВ
        ActionTypes = self._Generate_Action(len_settings=len(settings), ActionType=ActionType)

        # Получаем айдишники -

        ActionID = self._Generation_ActionID(len_settings=len(settings))
        # ТЕПЕРЬ ПЕРЕБИРАЕМ все значения и добавляем нужные элементы
        for i in range(len(settings)):
            settings[i]['actionId'] = ActionID[i]
            settings[i]['actionType'] = ActionTypes[i]

        self.Settings = settings

    def _Generate_Action(self, len_settings, ActionType):
        """
        Генерируем список необходимых Дейсвитвий

        :param len_settings:
        :param ActionType:
        :return:
        """

        # Первое что смотрим - Если у нас спущен массив -
        if (type(ActionType) == list) or (type(ActionType) == tuple) or (type(ActionType) == set):
            EventType = list(ActionType)

            # Получаем все значения
            ActionType_all = list(self.Action_Types.values())
            # Получаем список который будем подставлять
            ActionType_settings = []
            for i in ActionType:
                # Если такое сущетсвуеь , то улыбьаемся
                if i in ActionType_all:
                    ActionType_settings.append(i)

            # ТЕПЕРЬ ПОНИМАЕМ СКОЛЬКО НАДО ДОПОЛНИТЬ
            if len_settings > len(ActionType_settings):
                # Выясняем сколько нужно добавить
                count_added = len_settings - len(ActionType_settings)

                # Генерируем -
                ActionType_added = self._generation_ActionType_list(count_added)
                ActionType_settings = ActionType_settings + ActionType_added

        else:
            # Иначе генерируем сколько нужно

            # Генерируем -
            ActionType_settings = self._generation_ActionType_list(len_settings)

        return ActionType_settings

    def _generation_ActionType_list(self, count):
        """
        Здесь генерируем рандомно какой то из EventType

        :param count:
        :return:
        """

        from random import randint
        ActionType = []
        # Получаем максимальные значения ключей - для генерации
        min_key = min(list(self.Action_Types.keys()))
        max_key = max(list(self.Action_Types.keys()))
        for i in range(count):
            element = self.Action_Types[randint(min_key, max_key)]
            ActionType.append(element)

        return ActionType

    def _Generation_ActionID(self, len_settings):

        """
        Здесь генерируем наши айдишники - это выжно

        :param len_settings:
        :return:
        """

        ActionID = []

        # Получаем максимальный айдишник
        ActionID_max = self._find_max_Action_ID() + 1

        for i in range(len_settings):
            ActionID.append(i + int(ActionID_max))

        return ActionID

    def _find_max_Action_ID(self):

        """
        ЗАГЛУШКА -
        Поскольку я так и не разобрался к чему ID Event

        Будем ставить МАКСИМАЛЬНЫЙ

        :return:
        """

        from Service.SQL import execute_command

        command = 'SELECT MAX(ActionId) AS Id  FROM Manager'
        result = execute_command(command)

        if len(result) > 1:
            result = result[0].get('Id')
            if result is None:
                result = 0
        else:
            result = 0
        return result
