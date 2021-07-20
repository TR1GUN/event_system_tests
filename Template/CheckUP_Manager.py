# Здесь сделаем класс сравнения


class CheckUp:
    """
    Итак - это наш класс для сравнения , здесь сравниваем JSON ответа, с предполагаемым ответом
    """
    Key_value_inequality = 'Неравенство значений Ключа'
    Key_value_in_JSON = 'Значение ключа в  JSON ответа'
    Key_value_in_DataBase = 'Значение ключа в БД'

    def _checkup(self, data_base: list, JSON: list):

        """

        Основной метод сравнения

        :param data_base:
        :param JSON:
        :return:
        """
        from copy import deepcopy

        data_base_left = deepcopy(data_base)

        error = []
        # ТЕПЕРЬ ПЕРЕБИРАЕМ JSON
        for element_JSON_dict in JSON:
            # Первое что ищем - это айдишник
            idx = element_JSON_dict.get('id')
            # Теперь этот айдишник ищем в БД
            for element_Data_Base_dict in data_base:
                # Теперь - при совпадении айдишников - сравниваем поэлементно
                if idx == element_Data_Base_dict.get('id'):
                    result = self._checkup_by_keys_element_dict(JSON_dict=element_JSON_dict,
                                                                DataBase_dict=element_Data_Base_dict)
                    error = error + result
                    data_base_left.pop(data_base_left.index(element_Data_Base_dict))

        if len(data_base_left) > 0:
            result = \
                [{
                    'В БД есть лишние записи': data_base_left
                }]
            error = error + result

        return error

    def _checkup_by_keys_element_dict(self, JSON_dict: dict, DataBase_dict):

        """
        Итак - здесь сравниваем элементы по ключам

        :param JSON_dict:
        :param DataBase_dict:
        :return:

        """
        # Сборщики ошибок
        error = []
        error_keys = []
        # Сначала проверяем значения JSON
        for keys in JSON_dict:
            # отбрасываем ключ pattern
            if keys not in []:
                # Теперь сравниваем значения
                JSON_value = JSON_dict.get(keys)
                DataBase_value = DataBase_dict.get(keys)

                # Теперь проверяем их равнество

                if (type(JSON_value) == float) and (type(DataBase_value) == float):
                    epsilon = 5.96e-08
                    if abs(JSON_value / DataBase_value - 1) > epsilon:
                        # Генерируем строку ошибки
                        error_string = self._add_error_strings_keys_value(keys=keys,
                                                                          JSON_value=JSON_value,
                                                                          DataBase_value=DataBase_value)

                        # Добавляем это в ошибку , и добавляем наш ключ
                        error.append(error_string)
                        error_keys.append(keys)

                else:
                    if JSON_value != DataBase_value:
                        # Генерируем строку ошибки
                        error_string = self._add_error_strings_keys_value(keys=keys,
                                                                          JSON_value=JSON_value,
                                                                          DataBase_value=DataBase_value)

                        # Добавляем это в ошибку , и добавляем наш ключ
                        error.append(error_string)
                        error_keys.append(keys)

        # ------------ ТЕПЕРЬ ПЕРЕБИРАЕМ БД ------------->
        for keys in DataBase_dict:
            # отбрасываем ключ pattern
            if keys not in []:
                if keys not in error_keys:
                    # Теперь сравниваем значения
                    # answer_value = answer_element.get(keys)
                    # normal_value = normal_element.get(keys)
                    # Теперь сравниваем значения
                    JSON_value = JSON_dict.get(keys)
                    DataBase_value = DataBase_dict.get(keys)
                    # Теперь проверяем их равнество

                    if (type(DataBase_value) == float) or (type(JSON_value) == float):
                        epsilon = 5.96e-08
                        if abs(JSON_value / DataBase_value - 1) > epsilon:
                            # Генерируем строку ошибки
                            error_string = self._add_error_strings_keys_value(keys=keys,
                                                                              JSON_value=JSON_value,
                                                                              DataBase_value=DataBase_value)

                            # Добавляем это в ошибку , и добавляем наш ключ
                            error.append(error_string)
                            error_keys.append(keys)

                    else:
                        if DataBase_value != JSON_value:
                            # Генерируем строку ошибки
                            error_string = self._add_error_strings_keys_value(keys=keys,
                                                                              JSON_value=JSON_value,
                                                                              DataBase_value=DataBase_value)

                            # Добавляем это в ошибку , и добавляем наш ключ
                            error.append(error_string)
                            error_keys.append(keys)
        return error

    def _add_error_strings_keys_value(self, keys, JSON_value, DataBase_value):

        """
        Формируем строку ошибки - Это важно
        :param keys:
        :param JSON_value:
        :param DataBase_value:
        :return:
        """

        error_string = \
            {
                self.Key_value_inequality: str(keys),
                self.Key_value_in_JSON: JSON_value,
                self.Key_value_in_DataBase: DataBase_value
            }

        return error_string


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class CheckUpGET(CheckUp):
    """
    Здесь проводим наш любимый сравнивать БД и JSON

    """
    Key_value_inequality = 'Неравенство значений Ключа'
    Key_value_in_JSON = 'Значение ключа в  JSON ответа'
    Key_value_in_DataBase = 'Значение ключа в БД'

    error = []

    def __init__(self, data_base: list, JSON: list):
        # Получаем -
        self.error = self._checkup(data_base=data_base, JSON=JSON)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class CheckUpPUT(CheckUp):
    """
    Здесь проводим наш любимый сравнивать БД и JSON

    """
    Key_value_inequality = 'Неравенство значений Ключа'
    Key_value_in_JSON = 'Значение ключа в  JSON ответа'
    Key_value_in_DataBase = 'Значение ключа в БД'

    error = []

    def __init__(self, data_base: list, JSON: list):
        # Получаем -
        self.error = self._checkup(data_base=data_base, JSON=JSON)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class CheckUpPOST(CheckUp):
    """
    Здесь проводим наш любимый сравнивать БД и JSON

    """
    Key_value_inequality = 'Неравенство значений Ключа'
    Key_value_in_JSON = 'Значение ключа в  JSON ответа'
    Key_value_in_DataBase = 'Значение ключа в БД'

    error = []

    def __init__(self, data_base: list, JSON: list):
        # Получаем -
        self.error = self._checkup(data_base=data_base, JSON=JSON)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class CheckUpDELETE(CheckUp):
    """
    Здесь проводим наш любимый сравнивать БД и JSON

    """
    Key_value_inequality = 'Неравенство значений Ключа'
    Key_value_in_JSON = 'Значение ключа в  JSON ответа'
    Key_value_in_DataBase = 'Значение ключа в БД'

    error = []

    _error_str = 'ОШИБКА'

    def __init__(self,
                 # БД что была ДО
                 database_before: list,
                 # БД что была ПОСЛЕ
                 database_after: list,
                 # сам JSON
                 JSON: dict):
        """
        для метода DELETE делаем другой способ проверки
        :param database_before: БД что была ДО
        :param database_after: БД что была ПОСЛЕ
        :param JSON: сам JSON
        """

        self.error = []
        # Получаем -
        ids_list = JSON.get('ids')
        # ЕСЛИ МЫ УДАЛЯЕМ ВСЕ - ТО БД долдна быть псоле пустая
        if ids_list is None:
            if len(database_after) > 0:
                self.error = [{
                    self._error_str: 'ИЗ БД НЕ ВСЕ УДАЛЕННО',
                    'все должно было удалиться ,но  остались записи ': database_after,

                }]

        else:

            from Template.Template_DataBase_Was_Recording import DataBaseWasRecording

            # Получаем что мы удалили
            data_base_was_deleted = DataBaseWasRecording(database_before=database_after,
                                                         database_after=database_before).database_was_recording

            self.error = self._checkup(data_base_was_deleted=data_base_was_deleted, JSON=JSON)

    def _checkup(self, data_base_was_deleted: list, JSON: dict):
        """
        Здесь переопределяем наши методы

        :param data_base_was_deleted: - то что удалено
        :param JSON: то что должно было быть удаленно
        :return:
        """
        error = []

        ids = JSON.get('ids')

        from copy import deepcopy
        all_list = deepcopy(ids)

        # Итак - Берем
        for idx in ids:

            for element in data_base_was_deleted:

                if element.get('id') == idx:
                    # Удаляем его
                    all_list.remove(idx)

        # Если что то не удалилось - пишем ощибку
        if len(all_list) > 0:
            error_str = {
                self._error_str: 'ИЗ БД НЕ ВСЕ УДАЛЕННО',
                'Остались ID': all_list,
                'Должно было удалиться': data_base_was_deleted
            }

            error.append(error_str)

        return error
