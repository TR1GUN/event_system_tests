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

    ]


# @pytest.fixture()
def Generate_POST_JSON():
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = SchedulerJSON(generate=i.get('generate'),
                             mon=i.get('mon'),
                             day=i.get('day'),
                             hour=i.get('hour'),
                             min=i.get('min'),
                             ).POST(
                                    custom_settings=i.get('custom_settings')
        )
        test_set.append(JSON)
    return test_set


def Generate_PUT_JSON():
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = SchedulerJSON(generate=i.get('generate'),
                             mon=i.get('mon'),
                             day=i.get('day'),
                             hour=i.get('hour'),
                             min=i.get('min'),
                             ).PUT(
                                    custom_settings=i.get('custom_settings')
        )
        test_set.append(JSON)
    return test_set


def Generate_GET_JSON():
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = SchedulerJSON(generate=i.get('generate'),
                             mon=i.get('mon'),
                             day=i.get('day'),
                             hour=i.get('hour'),
                             min=i.get('min'),
                             ).GET(

                                    ids=i.get('select_ids'),
                                    custom_settings=i.get('custom_settings'),
                                    Record_Values=i.get('Record_Values')
                                   )
        test_set.append(JSON)
    return test_set


def Generate_DELETE_JSON():
    from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = SchedulerJSON(generate=i.get('generate'),
                             mon=i.get('mon'),
                             day=i.get('day'),
                             hour=i.get('hour'),
                             min=i.get('min'),
                             ).DELETE(
                                        ids=i.get('select_ids'),
                                        custom_settings=i.get('custom_settings'),
                                        Record_Values=i.get('Record_Values')
        )
        test_set.append(JSON)
    return test_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON", Generate_POST_JSON())
def test_Scheduler_POST(type_connect, JSON):
    from Event_System_Tests.Scheduler import Scheduler
    print(JSON)
    result = Scheduler(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_PUT_JSON())
def test_Scheduler_PUT(type_connect, JSON):
    from Event_System_Tests.Scheduler import Scheduler
    print(JSON)
    result = Scheduler(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_GET_JSON())
def test_Scheduler_GET(type_connect, JSON):
    from Event_System_Tests.Scheduler import Scheduler
    print(JSON)
    result = Scheduler(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_DELETE_JSON())
def test_Scheduler_DELETE(type_connect, JSON):
    from Event_System_Tests.Scheduler import Scheduler
    print(JSON)
    result = Scheduler(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
