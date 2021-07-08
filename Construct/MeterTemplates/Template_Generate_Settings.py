class GenerateSettings:
    """
    В этом классе генерируем поле Settings для JSON MeterTemplates

    """

    settings = []

    def __init__(self, name: int = 1, meters: int = 3, unique_meter: bool = True):
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
        # ЕСЛИ У НАС ЧИСЛО
        if type(name) == int:
            # Генерируем список из словаря имен
            settings = self._generation_name(name=name)
            # ТЕПЕРЬ ДОСТРАИВАЕМ ИМЯ
            settings = self._generation_settings(settings=settings, meter=meters, unique_types=unique_meter)
        # ----->
        # Если имена только список
        elif (type(name) == list) or (type(name) == tuple) or (type(name) == set):
            # ПРОВЕРЯЕМ ЧАСТНЫЙ ВАРИАНТ ЭТОГО- мы подали все верно

            # ЕСЛИ ЭТО СПИСОК ИЗ ИМЕН - оставляем все как есть
            if type(name[0]) == str:
                settings = []
                for i in range(len(name)):
                    settings.append({'name': name[i]})
                settings = self._generation_settings(settings=settings, meter=meters, unique_types=unique_meter)

            elif type(name[0]) == dict:
                from Construct.Template_Construct_Settings import ConstructSettings
                settings = ConstructSettings(Settings=name, default_name_1='name', default_name_2='meters').Settings

            else:
                settings = []
        # ----->
        else:
            settings = self._generation_settings(settings=self._generation_name(name=1), meter=1, unique_types=True)

        # ----->

        self.settings = settings

    def _generation_name(self, name: int):
        """
        ЗДЕСЬ генерируем Список из имен - ЭТО ОЧЕНЬ ВАЖНО

        :param name:
        :return:
        """

        from Construct.MeterDataTemplates.Template_Generate_Field_Name import GenerateFieldName
        name = GenerateFieldName
        name.adding_name = str(self._find_Max_Tempplate_name())

        name = GenerateFieldName(name=name).settings

        return name

    def _generation_meter(self, meter, Meter_Id):

        """

        Генерация списка Meter

        :return:
        """

        from Construct.MeterTemplates.Template_Generate_MeterId import GenerateMeterId
        from copy import deepcopy

        Meter_Id_list = deepcopy(GenerateMeterId(count_meter=meter, start=Meter_Id).MeterId)

        return Meter_Id_list

    def _generation_settings(self, settings, meter, unique_types):

        """
        Генерация поля settings

        :param settings:
        :param types:
        :param unique_types:
        :return:
        """

        # ЕСЛИ У НАС ЕСТЬ ЧИСЛО
        if (type(meter) == int) and (meter > 0):

            # если у нас уникальные для всех типы
            if unique_types:
                # Ищем самый страрший счетчик
                Meter_Id = 0

                for setting in settings:
                    # Генерируем уникальный набор для каждого элемента
                    Meter_Id_list = self._generation_meter(meter=meter, Meter_Id=Meter_Id)
                    setting['meters'] = Meter_Id_list
                    Meter_Id = max(Meter_Id_list)
            # если у нас не уникальное значение
            else:

                Meter_Id_list = self._generation_meter(meter=meter, Meter_Id=0)
                for setting in settings:
                    setting['meters'] = Meter_Id_list

        # ЕСЛИ У НАС КАСТРОМНЫЙ СПИСОК
        elif (type(meter) == list) or (type(meter) == tuple) or (type(meter) == set):
            for setting in settings:
                setting["meters"] = meter

        else:
            for setting in settings:
                setting["meters"] = ["test"]

        return settings

    def _find_Max_Tempplate_name(self):
        from Service.SQL import execute_command

        command = 'SELECT MAX(TemplateName) AS Name  FROM MeterTemplates'
        result = execute_command(command)
        result = result[0].get('Name')
        if result is None:
            result = 'Adding_name_'
        else:
            result = str(result) + '_'
        return result
# //---------------------------------------------------------------------------------------------------------------
#                       класс ДЛЯ ФОРМИРОВАНИЯ поля id ДЯЛ GET\DELETE запроса
# //---------------------------------------------------------------------------------------------------------------

class GenerateNamesMeterTemplates:
    """
    Класс для формирования поля Names

    """
    names = []

    def __init__(self, names=0, settings=[{"name": '1'}]):
        """
        Конструктор

        :param ids:
        :param settings:

        """
        # сначала получаем все names что есть
        all_names = set()
        for i in settings:
            all_names.add(i.get('names'))

        all_names = list(all_names)

        # ЕСЛИ у нас int
        if (type(names) == int) and (names > 0):

            # чтоб не выстрелить себе в ногу
            if names > len(all_names):
                names = len(all_names)

            # ТЕПЕРЬ - ставим нужные names из сгенерированных
            from random import randint
            idx = set()
            while len(idx) < names:
                idx.add(all_names[randint(0, (len(all_names) - 1))])
            idx = list(idx)

        # ЕСЛИ У НАС СПИСОК - Проверяем - все ли айдишники есть
        elif (type(names) == list) or (type(names) == tuple) or (type(names) == set):
            # Теперь перебираем все names
            names_list = []
            for name in names:
                if name in all_names:
                    names_list.append(name)

        else:
            names = []

        self.names = names
