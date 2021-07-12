
class GenerateSettings:
    """
    В этом классе генерируем поле Settings для JSON MeterDataTemplates

    """

    settings = []

    def __init__(self, name: int = 1, types: int = 3, unique_types: bool = True):
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
            settings = self._generation_settings(settings=settings, types=types, unique_types=unique_types)
        # ----->
        # Если имена только список
        elif (type(name) == list) or (type(name) == tuple) or (type(name) == set):
            # ПРОВЕРЯЕМ ЧАСТНЫЙ ВАРИАНТ ЭТОГО- мы подали все верно

            # ЕСЛИ ЭТО СПИСОК ИЗ ИМЕН - оставляем все как есть
            if type(name[0]) == str:
                settings = []
                for i in range(len(name)):
                    settings.append({'name': name[i]})
                settings = self._generation_settings(settings=settings, types=types, unique_types=unique_types)

            elif type(name[0]) == dict:
                from Construct.Template_Construct_Settings import ConstructSettings
                settings = ConstructSettings(Settings=name, default_name_1='name', default_name_2='types').Settings

            else:
                settings = []
        # ----->
        else:
            settings = self._generation_settings(settings=self._generation_name(name=1), types=1, unique_types=True)

        # ----->

        self.settings = settings

    def _generation_name(self, name: int):
        """
        ЗДЕСЬ генерируем Список из имен - ЭТО ОЧЕНЬ ВАЖНО

        :param name:
        :return:
        """

        from Construct.MeterDataTemplates.Template_Generate_Field_Name import GenerateFieldName
        TemplateName = GenerateFieldName
        TemplateName.adding_name = str(self._find_Max_Tempplate_name())

        name = TemplateName(name=name).settings

        return name


    def _generation_types(self, types):
        """

            Генерация списка Types

            :return:
            """
        from Construct.MeterDataTemplates.Template_Generate_Field_Types import GenerateFieldTypes

        types_list = GenerateFieldTypes(types=types).types_list

        return types_list

    def _generation_settings(self, settings, types, unique_types):

        """
        Генерация поля settings

        :param settings:
        :param types:
        :param unique_types:
        :return:
        """

        # ЕСЛИ У НАС ЕСТЬ ЧИСЛО
        if (type(types) == int) and (types > 0):

            # если у нас уникальные для всех типы
            if unique_types:
                for setting in settings:
                    # Генерируем уникальный набор для каждого элемента
                    setting['types'] = self._generation_types(types=types)

            # если у нас не уникальное значение
            else:
                types_list = self._generation_types(types=types)
                for setting in settings:
                    setting['types'] = types_list

        # ЕСЛИ У НАС КАСТРОМНЫЙ СПИСОК
        elif (type(types) == list) or (type(types) == tuple) or (type(types) == set):
            for setting in settings:
                setting["types"] = self._generation_types(types=types)

        else:
            for setting in settings:
                setting["types"] = ["test"]

        return settings

    def _find_Max_Tempplate_name(self):
        from Service.SQL import execute_command

        command = 'SELECT MAX(TemplateName) AS Name  FROM MeterDataTemplates'
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

class GenerateNamesMeterDataTemplates:
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