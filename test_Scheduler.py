# Здесь напишем тестовые функции для Scheduler
import pytest

# ----------------------------------------------------------------------------------------------------->
# ----------------------------------------------------------------------------------------------------->
JSON_data_set = \
    [
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': 1,
            # Наличие месяца в генерации
            'mon': True,
            # Наличие дня в генерации
            'day': True,
            # Наличие часа в генерации
            'hour': True,
            # Значение минут в генерации
            'min': None,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': 5,
            # Наличие месяца в генерации
            'mon': False,
            # Наличие дня в генерации
            'day': False,
            # Наличие часа в генерации
            'hour': False,
            # Значение минут в генерации
            'min': 12,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': 20,
            # Наличие месяца в генерации
            'mon': False,
            # Наличие дня в генерации
            'day': False,
            # Наличие часа в генерации
            'hour': True,
            # Значение минут в генерации
            'min': None,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': 30,
            # Наличие месяца в генерации
            'mon': False,
            # Наличие дня в генерации
            'day': True,
            # Наличие часа в генерации
            'hour': True,
            # Значение минут в генерации
            'min': None,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': [1000, 1001, 1002],
            # Наличие месяца в генерации
            'mon': False,
            # Наличие дня в генерации
            'day': False,
            # Наличие часа в генерации
            'hour': False,
            # Значение минут в генерации
            'min': True,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': [1000, 1001, 1002],
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            # Генерация количества ID , Либо Список ID , Либо готовый Settings
            'generate': 100,
            # Наличие месяца в генерации
            'mon': True,
            # Наличие дня в генерации
            'day': True,
            # Наличие часа в генерации
            'hour': True,
            # Значение минут в генерации
            'min': None,
            # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },

        # Нагрузка
        # {
        #     # Генерация количества ID , Либо Список ID , Либо готовый Settings
        #     'generate': 300,
        #     # Наличие месяца в генерации
        #     'mon': True,
        #     # Наличие дня в генерации
        #     'day': True,
        #     # Наличие часа в генерации
        #     'hour': True,
        #     # Значение минут в генерации
        #     'min': 1,
        #     # айдишники которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
        #     'select_ids': 299,
        #     # Записываем или нет полученные значения
        #     'Record_Values': True,
        #     # Свои значения - Не проверяются
        #     'custom_settings': None
        # },

    ]

# ----------------------------------------------------------------------------------------------------->
def DeleteScheduler():
    from time import sleep
    from Template.DataBase.DataBase_Delete import DataBaseDELETE

    # Сначала чистим нашу БД
    Delete = DataBaseDELETE({"table": "Scheduler"})
    # спим
    sleep(2)

# ----------------------------------------------------------------------------------------------------->

# @pytest.fixture()
def Generate_POST_JSON():
    # from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = SchedulerJSON(generate=i.get('generate'),
    #                          mon=i.get('mon'),
    #                          day=i.get('day'),
    #                          hour=i.get('hour'),
    #                          min=i.get('min'),
    #                          ).POST(
    #                                 custom_settings=i.get('custom_settings')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_PUT_JSON():
    # from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = SchedulerJSON(generate=i.get('generate'),
    #                          mon=i.get('mon'),
    #                          day=i.get('day'),
    #                          hour=i.get('hour'),
    #                          min=i.get('min'),
    #                          ).PUT(
    #                                 custom_settings=i.get('custom_settings')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_GET_JSON():
    # from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = SchedulerJSON(generate=i.get('generate'),
    #                          mon=i.get('mon'),
    #                          day=i.get('day'),
    #                          hour=i.get('hour'),
    #                          min=i.get('min'),
    #                          ).GET(
    #
    #                                 ids=i.get('select_ids'),
    #                                 custom_settings=i.get('custom_settings'),
    #                                 Record_Values=i.get('Record_Values')
    #                                )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_DELETE_JSON():
    # from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = SchedulerJSON(generate=i.get('generate'),
    #                          mon=i.get('mon'),
    #                          day=i.get('day'),
    #                          hour=i.get('hour'),
    #                          min=i.get('min'),
    #                          ).DELETE(
    #                                     ids=i.get('select_ids'),
    #                                     custom_settings=i.get('custom_settings'),
    #                                     Record_Values=i.get('Record_Values')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON_param", Generate_POST_JSON())
def test_Scheduler_POST(type_connect, JSON_param):
    from Event_System_Tests.Scheduler import Scheduler

    # - Удаляем всю БД
    DeleteScheduler()

    # по параметрам генерируем JSON
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    # -->
    JSON = SchedulerJSON(generate=JSON_param.get('generate'),
                         mon=JSON_param.get('mon'),
                         day=JSON_param.get('day'),
                         hour=JSON_param.get('hour'),
                         min=JSON_param.get('min'),
                         ).POST(
        custom_settings=JSON_param.get('custom_settings')
    )
    # -->

    result = Scheduler(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_PUT_JSON())
def test_Scheduler_PUT(type_connect, JSON_param):
    from Event_System_Tests.Scheduler import Scheduler


    # - Удаляем всю БД
    DeleteScheduler()

    # по параметрам генерируем JSON
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    # -->
    JSON = SchedulerJSON(generate=JSON_param.get('generate'),
                         mon=JSON_param.get('mon'),
                         day=JSON_param.get('day'),
                         hour=JSON_param.get('hour'),
                         min=JSON_param.get('min'),
                         ).PUT(
        custom_settings=JSON_param.get('custom_settings')
    )
    # -->
    result = Scheduler(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_GET_JSON())
def test_Scheduler_GET(type_connect, JSON_param):
    from Event_System_Tests.Scheduler import Scheduler


    # - Удаляем всю БД
    DeleteScheduler()

    # по параметрам генерируем JSON
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    # -->
    JSON = SchedulerJSON(generate=JSON_param.get('generate'),
                         mon=JSON_param.get('mon'),
                         day=JSON_param.get('day'),
                         hour=JSON_param.get('hour'),
                         min=JSON_param.get('min'),
                         ).GET(

        ids=JSON_param.get('select_ids'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
    )
    # -->

    print(JSON)
    result = Scheduler(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_DELETE_JSON())
def test_Scheduler_DELETE(type_connect, JSON_param):

    # - Удаляем всю БД
    DeleteScheduler()

    # по параметрам генерируем JSON
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
    # -->
    JSON = SchedulerJSON(generate=JSON_param.get('generate'),
                         mon=JSON_param.get('mon'),
                         day=JSON_param.get('day'),
                         hour=JSON_param.get('hour'),
                         min=JSON_param.get('min'),
                         ).DELETE(
        ids=JSON_param.get('select_ids'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
    )
    # -->

    from Event_System_Tests.Scheduler import Scheduler
    print(JSON)
    result = Scheduler(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
