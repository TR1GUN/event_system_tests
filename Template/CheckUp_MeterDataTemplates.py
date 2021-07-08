# Здесь расположим класс сравнения - ЭТО ОЧЕНЬ ВАЖНАЯ ХРЕНЬ

class CheckUp:
    """
    Итак - это наш класс для сравнения , здесь сравниваем JSON ответа, с предполагаемым ответом
    """
    diff_value_inequality = 'Есть расхождения значений '
    Key_value_in_JSON = 'Значение ключа в  JSON'
    Key_value_in_DataBase = 'Значение ключа в БД'

    # Добавляем ключ id
    key_id = 'name'
    key_list = 'types'

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
            idx = element_JSON_dict.get(self.key_id)
            # Теперь этот айдишник ищем в БД
            for element_Data_Base_dict in data_base:
                # Теперь - при совпадении айдишников - сравниваем поэлементно
                if idx == element_Data_Base_dict.get(self.key_id):
                    # Итак - если у нас все хорошо - сравниваем -
                    element_JSON = element_JSON_dict.get(self.key_list)
                    element_Data_Base = element_Data_Base_dict.get(self.key_list)

                    result = self._check_up_list_elements(list_JSON=element_JSON,
                                                        list_data_base=element_Data_Base)
                    error = error + result
                    # Удлаяем элемент массива - Если такой айдишник есть
                    data_base_left.pop(data_base_left.index(element_Data_Base_dict))

        if len(data_base_left) > 0:
            result = \
                [{
                    'В БД есть лишние записи': data_base_left
                }]
            error = error + result

        return error

    def _check_up_list_elements(self, list_data_base, list_JSON):
        """
        Сюда пихаем два списка - Это очень важно
        :return:

        """
        # Если значений нет - То делаем пустой список - это важно
        if list_data_base is None:
            list_data_base = []
        if list_JSON is None:
            list_JSON = []
        error = []
        list_data_base_set = set(list_data_base)
        list_JSON_set = set(list_JSON)

        diff_JSON = list(list_JSON_set - list_data_base_set)
        diff_data_base = list(list_data_base_set - list_JSON_set)

        if len(diff_JSON) > 0:
            error.append(self._add_error_strings_keys_value(diff_value=diff_JSON,
                                                            JSON_value=list_JSON_set,
                                                            DataBase_value=list_data_base_set))

        if len(diff_data_base) > 0:
            error.append(self._add_error_strings_keys_value(diff_value=diff_data_base,
                                                            JSON_value=list_JSON_set,
                                                            DataBase_value=list_data_base_set))

        return error

    def _add_error_strings_keys_value(self, diff_value, JSON_value, DataBase_value):

        """
        Формируем строку ошибки - Это важно
        :param keys:
        :param JSON_value:
        :param DataBase_value:
        :return:
        """

        error_string = \
            {
                self.diff_value_inequality: diff_value,
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
