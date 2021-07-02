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
            if keys not in ['pattern']:
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
            # Здесь обрабатываем ключ pattern
            elif keys in ['pattern']:

                # Получаем значения JSON
                JSON_value = JSON_dict.get(keys)
                # собираем значения для pattern
                mon = DataBase_dict.get('mon')
                if mon in [255, None]:
                    mon = '*'
                day = DataBase_dict.get('day')
                if day in [255, None]:
                    day = '*'
                hour = DataBase_dict.get('hour')
                if hour in [255, None]:
                    hour = '*'
                min = DataBase_dict.get('min')
                # if min in [255 , None] :
                #     min = '*'

                # Теперь форимируем наш pattern
                if (hour == '*') and (day == '*') and (mon == '*'):
                    DataBase_value = '* / ' + str(min) + ' * * * *'
                else:
                    DataBase_value = str(min) + " " + str(hour) + " " + str(day) + " " + str(mon) + " *"

                # ТЕПЕРЬ СРАВНИВАЕМ
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
            if keys not in ['pattern']:
                if keys not in error_keys:
                    # Теперь сравниваем значения
                    # answer_value = answer_element.get(keys)
                    # normal_value = normal_element.get(keys)
                    # Теперь сравниваем значения
                    JSON_value = JSON_dict.get(keys)
                    DataBase_value = DataBase_dict.get(keys)
                    # Теперь ставим условность - 255 и None
                    if DataBase_value in [255]:
                        DataBase_value = None
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