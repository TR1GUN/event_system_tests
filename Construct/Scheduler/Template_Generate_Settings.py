class GenerateSettingsScheduler:
    """
    В этом классе генерируем поле Settings для JSON Scheduler

    """

    settings = []

    def __init__(self,
                 # Количество генераций - или полный список того что должны сгенерировать
                 generate: int = 1,
                 # Наличие месяца
                 mon: bool = True,
                 # Наличие для
                 day: bool = True,
                 # наличие часа
                 hour: bool = True,
                 # Установка минут
                 min: int = None,
                 # айдищник старта генерации - Вырезаем
                 # start: int = 0
                 ):

        # Итак - основная логика работы -
        # 1) в НЭЙМ можно спускать
        #     - количество имен - и они генерируются
        #         - Поле тупес подставляется
        #         - Поле тупес генерируется уникальным
        #         - Поле тупес генерируется одинаковое для всех
        #     - список имен и они подставляются
        #     - Уже готовый Settings

        # ИТАК ПОГНАЛИ
        self.settings = []
        from Construct.Scheduler.Template_construct_field_settings import ConstructFieldSettings

        # ЕСЛИ У НАС ЧИСЛО
        if type(generate) == int:
            # Генерируем нужное количество данных
            settings = []
            # ищем максимальное значение - это будет точкой отсчета
            start = self._find_max_value() + 1
            for idx in range(generate):
                # Генерируем один из элементов
                setting = ConstructFieldSettings(idx=start + idx, mon=mon, day=day, hour=hour, min=min).settings
                settings.append(setting)

        # ----->
        # Если имена только список
        elif (type(generate) == list) or (type(generate) == tuple) or (type(generate) == set):
            # ПРОВЕРЯЕМ ЧАСТНЫЙ ВАРИАНТ ЭТОГО- мы подали все верно

            # ЕСЛИ ЭТО СПИСОК ИЗ ИМЕН - оставляем все как есть
            if type(generate[0]) == int:
                settings = []
                for idx in range(len(generate)):
                    # Генерируем один из элементов
                    setting = ConstructFieldSettings(idx=generate[idx], mon=mon, day=day, hour=hour, min=min).settings
                    settings.append(setting)

            elif type(generate[0]) == dict:
                # Если у нас спускается то что должны пристроить - то
                settings = list(generate)
                settings = self._checkup_correct_JSON(settings=settings)

            else:
                settings = []
        # ----->
        else:
            # ищем максимальное значение - это будет точкой отсчета
            start = self._find_max_value()

            # Иначе генерируем ОДНУ ШТУКУ
            setting = ConstructFieldSettings(idx=start + 1, mon=mon, day=day, hour=hour, min=min).settings

            setting = [setting]
        # ----->

        self.settings = settings

    def _checkup_correct_JSON(self, settings):

        """
        Проверка Корректности типов
        :param settings:
        :return:
        """

        for setting in settings:

            # ПРОВЕРЯЕМ ОБЯЗАТЕЛЬНЫЕ ПОЛЯ
            if setting.get('id') is None:
                setting['id'] = 1

            if setting.get('min') is None:
                setting['min'] = 10

        return settings

    def _find_max_value(self):
        """
        В Этом методе ищем максимальное значение

        :return:
        """
        from Service.SQL import execute_command
        command = 'SELECT max(Id) FROM Scheduler'

        max_id = execute_command(command=command)

        # idx = None
        for i in max_id:
            idx = i.get('max(Id)')
        if idx is None:
            idx = 0

        return idx


# //---------------------------------------------------------------------------------------------------------------
#                       класс ДЛЯ ФОРМИРОВАНИЯ поля id ДЯЛ GET\DELETE запроса
# //---------------------------------------------------------------------------------------------------------------

class GenerateIdsScheduler:
    """
    Класс для формирования поля IDS

    """
    idx = [0]

    def __init__(self, ids=0, settings=[{"id": 1}]):
        """
        Конструктор

        :param ids:
        :param settings:

        """

        # ЕСЛИ у нас int
        if (type(ids) == int) and (ids > 0):
            # сначала получаем все айдишники что есть
            all_idx = []
            for i in settings :
                all_idx.append(i.get('id'))

            # чтоб не выстрелить себе в ногу
            if ids > len(all_idx):
                ids = len(all_idx)

           # ТЕПЕРЬ - ставим нужные айдишники из сгенерированных
            from random import randint
            idx = set()
            while len(idx) < ids:
                idx.add(all_idx[randint(0, (len(all_idx) - 1))])
            idx = list(idx)

        # ЕСЛИ У НАС СПИСОК - Проверяем - все ли айдишники есть
        elif (type(ids) == list) or (type(ids) == tuple) or (type(ids) == set):
            ids = set(ids)
            # сначала получаем все айдишники что есть
            all_idx = set()
            for i in settings :
                all_idx.add(i.get('id'))

            # Теперь перебираем все айдишники
            idx = ids & all_idx
            idx = list(idx)

        else:
            idx = []

        self.idx = idx