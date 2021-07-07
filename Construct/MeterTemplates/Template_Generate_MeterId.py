# Здесь генерируем наш MeterId

class GenerateMeterId:
    """
    Генерируем наш список MeterId

    """

    MeterId = []

    def __init__(self, count_meter: int = 1, start: int = 0):
        """
        Класс генерации нужного списка с MeterID

        :param count_meter: - Количество счетчиков
        :param start: - точка отсчета
        """
        self.MeterId = []
        self.MeterId = self._generate(count_meter=count_meter, start=start)

    def _generate(self, count_meter, start):
        # Важный момент - МЫ отправляемся в БД если у нас start стоит в нулину или человек подал другое значение
        if (type(start) == int) and (start > 0):
            start = start + 1

        else:
            start = self._find_max_MeterId()

        # После чего начинаем отсчет

        MeterId = []
        for i in range(count_meter):
            MeterId.append(start + i)

        return MeterId

    def _find_max_MeterId(self):
        """
        В Этом методе ищем максимальное значение

        :return:
        """
        from Service.SQL import execute_command
        command = 'SELECT max(MeterId) AS MeterId FROM MeterTemplateArray'

        max_id = execute_command(command=command)

        idx = None

        for i in max_id:
            idx = i.get('MeterId')
        if idx is None:
            idx = 0

        return idx + 1
