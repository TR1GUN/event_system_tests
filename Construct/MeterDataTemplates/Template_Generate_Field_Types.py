# Здесь генерируем УНИКАЛЬЫНЕ Типы


class GenerateFieldTypes:
    """
    Генерируем поле Тайпс

    """
    types_list = []

    def __init__(self, types: int = 1):
        """

        :param types:
        """
        if type(types) != int:
            types = 1

        from random import randint
        # ГЕНЕРИРУЕМ УНИКАЛЬНЫЕ АЙДИШНИКИ КОТОРЫЕ НЕ ПЕРЕСЕКАЮТСЯ
        id_set = set()

        while len(id_set) < types:
            id_set.add((randint(0, 9999)))
        # Переводим в сет
        id_set = list(id_set)

        types_list = []

        adding_types = 'Adding_types_'
        for i in range(types):
            types_list.append(adding_types + str(id_set[i]))

        self.types_list = types_list


