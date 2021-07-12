# Здесь генерируем УНИКАЛЬЫНЕ Типы


# class GenerateFieldTypes:
#     """
#     Генерируем поле Тайпс
#
#     """
#     types_list = []
#
#     def __init__(self, types: int = 1):
#         """
#
#         :param types:
#         """
#         if type(types) != int:
#             types = 1
#
#         from random import randint
#         # ГЕНЕРИРУЕМ УНИКАЛЬНЫЕ АЙДИШНИКИ КОТОРЫЕ НЕ ПЕРЕСЕКАЮТСЯ
#         id_set = set()
#
#         while len(id_set) < types:
#             id_set.add((randint(0, 9999)))
#         # Переводим в сет
#         id_set = list(id_set)
#
#         types_list = []
#
#         adding_types = 'Adding_types_'
#         for i in range(types):
#             types_list.append(adding_types + str(id_set[i]))
#
#         self.types_list = types_list


# //---------------------------------------------------------------------------------------------------------------//
# //----             Сделаем Альтернативный генератор для  MeterDataTemplates                                  ----//
# //---------------------------------------------------------------------------------------------------------------//
All_ArchTypes = \
    [
        # Конфиги
        'ElConfig',
        'PlsConfig',
        'DigConfig',
        # Энергия -
        'ElMomentEnergy', 'ElDayEnergy', 'ElMonthEnergy',
        # Потребленная Энергия
        'ElDayConsEnergy', 'ElMonthConsEnergy',
        # Моментное сотояние фаз
        'ElMomentQuality',
        # Профиль мощности
        'ElArr1ConsPower',
        # Импульсные показатели
        'PlsMomentPulse', 'PlsDayPulse', 'PlsMonthPulse', 'PlsHourPulse',
        # Диджитал показатели
        'DigMomentState', 'DigJournalState',
        # ЖУРНАЛЬЧИКИ ММММ
        'ElJrnlPwr', 'ElJrnlTimeCorr', 'ElJrnlReset', 'ElJrnlC1Init', 'ElJrnlC2Init',
        'ElJrnlTrfCorr', 'ElJrnlOpen', 'ElJrnlUnAyth',
        'ElJrnlPwrA', 'ElJrnlPwrB', 'ElJrnlPwrC',
        'ElJrnlProg', 'ElJrnlRelay', 'ElJrnlLimESumm',
        'ElJrnlLimETrf', 'ElJrnlLimETrf1', 'ElJrnlLimETrf2', 'ElJrnlLimETrf3', 'ElJrnlLimETrf4',
        'ElJrnlLimUAMax', 'ElJrnlLimUAMin',
        'ElJrnlLimUBMax', 'ElJrnlLimUBMin',
        'ElJrnlLimUCMax', 'ElJrnlLimUCMin',
        'ElJrnlLimUABMax', 'ElJrnlLimUABMin',
        'ElJrnlLimUBCMax', 'ElJrnlLimUBCMin',
        'ElJrnlLimUCAMax', 'ElJrnlLimUCAMin',
        'ElJrnlLimIAMax', 'ElJrnlLimIBMax', 'ElJrnlLimICMax',
        'ElJrnlLimFreqMax', 'ElJrnlLimFreqMin',
        'ElJrnlLimPwr', 'ElJrnlLimPwrPP', 'ElJrnlLimPwrPM', 'ElJrnlLimPwrQP', 'ElJrnlLimPwrQM',
        'ElJrnlReverce', 'PlsJrnlTimeCorr',
    ]


class GenerateFieldTypes:
    """
    Генерируем поле Тайпс

    """
    types_list = []

    All_ArchTypes = \
        [
            # Конфиги
            'ElConfig',
            'PlsConfig',
            'DigConfig',
            # Энергия -
            'ElMomentEnergy', 'ElDayEnergy', 'ElMonthEnergy',
            # Потребленная Энергия
            'ElDayConsEnergy', 'ElMonthConsEnergy',
            # Моментное сотояние фаз
            'ElMomentQuality',
            # Профиль мощности
            'ElArr1ConsPower',
            # Импульсные показатели
            'PlsMomentPulse', 'PlsDayPulse', 'PlsMonthPulse', 'PlsHourPulse',
            # Диджитал показатели
            'DigMomentState', 'DigJournalState',
            # ЖУРНАЛЬЧИКИ ММММ
            'ElJrnlPwr', 'ElJrnlTimeCorr', 'ElJrnlReset', 'ElJrnlC1Init', 'ElJrnlC2Init',
            'ElJrnlTrfCorr', 'ElJrnlOpen', 'ElJrnlUnAyth',
            'ElJrnlPwrA', 'ElJrnlPwrB', 'ElJrnlPwrC',
            'ElJrnlProg', 'ElJrnlRelay', 'ElJrnlLimESumm',
            'ElJrnlLimETrf', 'ElJrnlLimETrf1', 'ElJrnlLimETrf2', 'ElJrnlLimETrf3', 'ElJrnlLimETrf4',
            'ElJrnlLimUAMax', 'ElJrnlLimUAMin',
            'ElJrnlLimUBMax', 'ElJrnlLimUBMin',
            'ElJrnlLimUCMax', 'ElJrnlLimUCMin',
            'ElJrnlLimUABMax', 'ElJrnlLimUABMin',
            'ElJrnlLimUBCMax', 'ElJrnlLimUBCMin',
            'ElJrnlLimUCAMax', 'ElJrnlLimUCAMin',
            'ElJrnlLimIAMax', 'ElJrnlLimIBMax', 'ElJrnlLimICMax',
            'ElJrnlLimFreqMax', 'ElJrnlLimFreqMin',
            'ElJrnlLimPwr', 'ElJrnlLimPwrPP', 'ElJrnlLimPwrPM', 'ElJrnlLimPwrQP', 'ElJrnlLimPwrQM',
            'ElJrnlReverce', 'PlsJrnlTimeCorr',
        ]

    def __init__(self, types: int or list = 1):
        # Что делаем - Определяем тип переменной
        self.types_list = []

        if type(types) == int:
            types_list = self.generate_int(types=types)
        elif (type(types) == list) or (type(types) == tuple) or (type(types) == set):
            types_list = self.generate_list(types=types)
        else:
            types_list = self.generate_int(types=1)
        self.types_list = types_list

    def generate_int(self, types):
        """
        Здесь генерим рандомно типы данных по количеству
        :return:
        """

        from random import randint
        # ГЕНЕРИРУЕМ УНИКАЛЬНЫЕ АЙДИШНИКИ КОТОРЫЕ НЕ ПЕРЕСЕКАЮТСЯ
        types_set = set()

        while len(types_set) < types:
            types_set.add(self.All_ArchTypes[randint(0, (len(self.All_ArchTypes) - 1))])
        # Переводим в сет
        types_set = list(types_set)

        return types_set

    def generate_list(self, types):
        """
        Здесь генериурем из списка - все те части что не подходят выбрасываем - если ничего не подходит - генерим один
        :param types:
        :return:
        """
        types = list(types)

        types_set = []

        for ArchType in types:
            if ArchType in self.All_ArchTypes:
                types_set.append(ArchType)

        # ЕСЛИ У НАС ПУСТОТА - НЕ БЕДА
        if len(types_set) < 1:
            types_set = self.generate_int(types=1)

        return types_set
