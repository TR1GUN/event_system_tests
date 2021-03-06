# Здесь расположим класс конструктор для поля Settings
# Если мы не подали нужного значения


class ConstructSettings:
    """
    Итак - Это Конструктор для обработки корректности данных

    Проверяем что подаваемое поле Settings имеет вид [{ default_name_1:default_value_1,
                                                            default_name_2 : [default_value_2, default_value_2] },
                                                            ,{default_name_1:default_value_1}]

    """

    Settings = []

    def __init__(self, Settings, default_name_1, default_name_2, ):

        """
        Итак - Это Конструктор для обработки корректности данных

        Проверяем что подаваемое поле Settings имеет вид [{ default_name_1:default_value_1,
                                                            default_name_2 : [default_value_2, default_value_2] },
                                                            ,{default_name_1:default_value_1}]

        :param default_name_1:
        :param default_value_1:
        :param default_name_2:
        :param default_value_2:
        """
        print(Settings)
        # Перебираем каждый элемент
        for element in range(len(Settings)):
            # ПРОВЕРЯЕМ КОРЕКТНОСТЬ ПОЛЕЙ
            # Проверяем первое поля массива
            if type(Settings[element]) == dict:

                # Если нет первого поля - добавляем его
                if Settings[element].get(default_name_1) is None:
                    Settings[element][default_name_1] = "added_non-existent_name_" + str(element)
                # ЕСЛИ ВТОРОЕ ПОЛЕ НЕ СПИСОК - УДАЛЯЕМ ЕГО ВЗАД
                if type(Settings[element].get(default_name_2)) not in [list, None]:
                    Settings[element].pop(default_name_2)
            # Иначе заменяем его шаблонным
            else:
                Settings[element] = {default_name_1: "auto_added_name_" + str(element)}

        # Возвращаем
        self.Settings = Settings
