
class ConstructFieldSettings:
    """

    Класс для генерации поля Settings

    """
    settings = {}

    def __init__(self, idx: int, mon: bool = True, day: bool = True, hour: bool = True, min: int = None):
        """
        Генерируем ОДНО поле settings

        :param idx: - int - ID что генерируем
        :param mon: - bool - Генерируем или нет месяцы
        :param day: - bool - Генерируем или нет дни
        :param hour: - bool - Генерируем или нет часы
        :param min: - int - Устанавливает нужное количество минут для всех элементов
        """

        from random import randint
        settings = {}

        # Если генерируем месяц :
        if mon:
            settings['mon'] = randint(1, 12)
        elif type(mon) == int:
            settings['mon'] = mon

        # Если генерируем день :
        if day:
            settings['day'] = randint(1, 31)
        elif type(day) == int:
            settings['day'] = day

        # Если генерируем час
        if hour:
            settings['hour'] = randint(1, 23)
        elif type(hour) == int:
            settings['hour'] = hour

        # Генерируем минуты
        if min is None:
            settings['min'] = randint(1, 59)
        elif type(hour) == int:
            settings['min'] = min
        else:
            settings['min'] = 1

        # Ставим айдишник
        settings['id'] = int(idx)

        self.settings = settings


