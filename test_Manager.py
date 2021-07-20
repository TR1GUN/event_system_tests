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
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None
        },
        {
            'ids': 3,
            'EventType': 6,
            'ActionType': 6,
            'select_id': 7,
            'Record_Values': True,
        },
        {
            'ids': 3,
            'EventType': 13,
            'ActionType': ['Poller'],
            'select_id': 2,
            'Record_Values': True,
        },
        {
            'ids': 30,
            'EventType': 3,
            'ActionType': 2,
            'select_id': 2,
            'Record_Values': True,
        },
        {
            'ids': 300,
            'EventType': ["Scheduler"],
            'ActionType': ['Poller'],
            'select_id': 299,
            'Record_Values': True,
        },
        {
            'ids': 3,
            'EventType': 4,
            'ActionType': 2,
            'select_id': 2,
            'Record_Values': True,
        },
    ]


# ----------------------------------------------------------------------------------------------------->
# @pytest.fixture()
def DeleteManager():
    from time import sleep
    from Template.DataBase.DataBase_Delete import DataBaseDELETE

    # Сначала чистим нашу БД
    Delete = DataBaseDELETE({'table': 'Manager'})
    # спим
    sleep(2)


def Generate_POST_JSON():
    # DeleteManager()
    #
    # from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
    #                        ).POST(custom_settings=i.get('custom_settings'))
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_PUT_JSON():
    # DeleteManager()
    #
    # from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
    #                        ).PUT(custom_settings=i.get('custom_settings'))
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_GET_JSON():
    # DeleteManager()
    #
    # from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
    #                        ).GET(ids=i.get('select_id'),
    #                              Record_Values=i.get('Record_Values'),
    #                              custom_settings=i.get('custom_settings'))
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_DELETE_JSON():
    # DeleteManager()
    #
    # from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = ManagerJSON(ids=i.get('ids'), EventType=i.get('EventType'), ActionType=i.get('ActionType')
    #                        ).DELETE(ids=i.get('select_id'),
    #                                 Record_Values=i.get('Record_Values'),
    #                                 custom_settings=i.get('custom_settings'))
    #     test_set.append(JSON)
    return JSON_data_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON_param", Generate_POST_JSON())
def test_Manager_POST(type_connect, JSON_param):

    # - Удаляем всю БД
    DeleteManager()

    # по параметрам генерируем JSON
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    # ->
    JSON = ManagerJSON(ids=JSON_param.get('ids'),
                       EventType=JSON_param.get('EventType'),
                       ActionType=JSON_param.get('ActionType')).POST(
                                                                custom_settings=JSON_param.get('custom_settings'))

    from Event_System_Tests.Manager import Manager

    print(JSON)
    result = Manager(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_PUT_JSON())
def test_Manager_PUT(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteManager()

    # по параметрам генерируем JSON
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    # ->
    JSON = ManagerJSON(ids=JSON_param.get('ids'),
                       EventType=JSON_param.get('EventType'),
                       ActionType=JSON_param.get('ActionType')).PUT(
                                                                    custom_settings=JSON_param.get('custom_settings'))

    from Event_System_Tests.Manager import Manager

    print(JSON)
    result = Manager(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_GET_JSON())
def test_Manager_GET(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteManager()

    # по параметрам генерируем JSON
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    # ->
    JSON = ManagerJSON(ids=JSON_param.get('ids'),
                       EventType=JSON_param.get('EventType'),
                       ActionType=JSON_param.get('ActionType')).GET(ids=JSON_param.get('select_id'),
                                                                    Record_Values=JSON_param.get('Record_Values'),
                                                                    custom_settings=JSON_param.get('custom_settings'))

    from Event_System_Tests.Manager import Manager

    print(JSON)
    result = Manager(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_DELETE_JSON())
def test_Manager_DELETE(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteManager()

    # по параметрам генерируем JSON
    from Construct.Manager.Construct_JSON_Manager import ManagerJSON
    # ->
    print('-----ddd-->', JSON_param)
    JSON = ManagerJSON(ids=JSON_param.get('ids'),
                       EventType=JSON_param.get('EventType'),
                       ActionType=JSON_param.get('ActionType')).DELETE(
                                                                    ids=JSON_param.get('select_id'),
                                                                    Record_Values=JSON_param.get('Record_Values'),
                                                                    custom_settings=JSON_param.get('custom_settings'))

    from Event_System_Tests.Manager import Manager

    print('------->',JSON)
    result = Manager(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
