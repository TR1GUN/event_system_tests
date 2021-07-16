# Здесь напишем тестовые функции для Manager
import pytest

# ----------------------------------------------------------------------------------------------------->
JSON_data_set = \
    [
        {
            # Количенство айдишников что мы генерим , либо их с список , либо ПОЛНОЦЕННЫЙ JSON
            'ids': 1,
            # Либо сам тип - str/int либо список из всего этого добра
            'EventType': ["Scheduler"],
            # Либо сам тип - str/int либо список из всего этого добра
            'ActionType': 2,
            # ИМЕНА которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids':0,
            # Записываем или нет полученные значения
            'Record_Values':  True,
            # Свои значения - Не проверяются
            'custom_settings':None
        },
        {
            'ids': 3,
            'EventType': ["Scheduler"],
            'ActionType': 2,
            'Select_id':2
        },
    ]

# ----------------------------------------------------------------------------------------------------->
# @pytest.fixture()
def Generate_POST_JSON():
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
                                                                        ).POST(custom_settings=i.get('custom_settings'))
        test_set.append(JSON)
    return test_set


def Generate_PUT_JSON():
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
                                                                        ).PUT(custom_settings=i.get('custom_settings'))
        test_set.append(JSON)
    return test_set


def Generate_GET_JSON():
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
                           ).GET(ids=i.get('select_id'),
                                Record_Values=i.get('Record_Values'),
                                custom_settings=i.get('custom_settings'))
        test_set.append(JSON)
    return test_set


def Generate_DELETE_JSON():
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON

    test_set = []
    for i in JSON_data_set:
        JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
                           ).DELETE(ids=i.get('select_id'),
                                    Record_Values=i.get('Record_Values'),
                                    custom_settings=i.get('custom_settings'))
        test_set.append(JSON)
    return test_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON", Generate_POST_JSON())
def test_Manager_POST(type_connect, JSON):
    from Event_System_Tests.Manager import Manager
    print(JSON)
    result = Manager(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_PUT_JSON())
def test_Manager_PUT(type_connect, JSON):
    from Event_System_Tests.Manager import Manager
    print(JSON)
    result = Manager(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_GET_JSON())
def test_Manager_GET(type_connect, JSON):
    from Event_System_Tests.Manager import Manager
    print(JSON)
    result = Manager(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_DELETE_JSON())
def test_Manager_DELETE(type_connect, JSON):
    from Event_System_Tests.Manager import Manager
    print(JSON)
    result = Manager(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
