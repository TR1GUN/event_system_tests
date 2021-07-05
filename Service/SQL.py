# Здесь расположим функции для работы с БД

# --------------------------------------------------------------------------------------------------------------------
#                                     Функция для работы с БД через расшаренную папку
# --------------------------------------------------------------------------------------------------------------------
# Вспомогательная функция

def dict_factory(cursor, row):
    """
    Вспомогательная функция для получения значений из таблицы ввиде dict
    ОЧЕНЬ УДОБНО ,ага

    Принимает - а хз как это обьяснить

    возвращает - даные запроса но только ввиде Dict
    :param cursor:
    :param row:
    :return:
    """
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict


def execute_command_to_shared_data_base(command: str):
    """
    Функция для расшаренной БД локально

    Используется Библиотека SQLite
    :param command:
    :return:
    """
    import sqlite3
    from Service.ConfigParser import dbpath
    conn = sqlite3.connect(dbpath)
    # print(dbpath)
    # print(command)

    conn.row_factory = dict_factory
    c = conn.cursor()


    c.execute(command)
    # print(command)
    # c.executemany(command)

    conn.commit()
    table = c.fetchall()
    c.close()
    return table


# --------------------------------------------------------------------------------------------------------------------

def execute_command(command: str):
    """
    сама функция для работы с БД

    :param command:
    :return:
    """

    result = execute_command_to_shared_data_base(command)

    return result
