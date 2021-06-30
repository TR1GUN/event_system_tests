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
                 # айдищник старта генерации
                 start: int = 0):

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

