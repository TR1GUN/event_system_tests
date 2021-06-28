class GenerateSettings:
    """
    В этом классе генерируем поле Settings для JSON MeterDataTemplates

    """

    settings = []

    def __init__(self, name, types, unique_types):
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
                settings = ConstructSettings(Settings=name, default_name_1='name', default_name_2='types')

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

        name = GenerateFieldName(name=name).settings

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
                setting["types"] = types

        else:
            for setting in settings:
                setting["types"] = ["test"]

        return settings
