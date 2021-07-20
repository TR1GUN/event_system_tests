# Здесь напишем тестовые функции для Poller
import pytest

# ----------------------------------------------------------------------------------------------------->
JSON_data_set = \
    [
        {
            # ЛИБО количетво ID , Либо список ID , ЛИБО ПОЛНОЦЕННЫЙ JSON
            'ids': 1,
            # MeterTemplates  - name - ЛИБО количество name, Либо список name
            'metersName': 1,
            # - MeterDataTemplates - name - количество Name , Либо список name
            'archTypesName': 1,
            # Булевый параметр - идет от наибольшего айдишника или нет
            'generate_of_max': True,
            # Количество генерируемых ArchTypes
            'ArchTypes': 2,
            # Количество генерируемых счетчиков
            'CountMeter': 2,
            # ИМЕНА которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'select_ids': 0,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None,
        },

    ]

# ----------------------------------------------------------------------------------------------------->
def DeletePoller():
    from time import sleep
    from Template.DataBase.DataBase_Delete import DataBaseDELETE

    # Сначала чистим нашу БД
    Delete = DataBaseDELETE({"table": "Poller"})
    # спим
    sleep(2)

# ----------------------------------------------------------------------------------------------------->
# @pytest.fixture()
def Generate_POST_JSON():
    # from Construct.Poller.Construct_JSON_Poller import PollerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = PollerJSON(ids=i.get('ids'),
    #                       metersName=i.get('metersName'),
    #                       archTypesName=i.get('archTypesName'),
    #                       generate_of_max=i.get('generate_of_max'),
    #                       ArchTypes=i.get('ArchTypes'),
    #                       CountMeter=i.get('CountMeter')
    #                       ).POST(
    #                             custom_settings=i.get('custom_settings')
    #                             )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_PUT_JSON():
    # from Construct.Poller.Construct_JSON_Poller import PollerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = PollerJSON(ids=i.get('ids'),
    #                       metersName=i.get('metersName'),
    #                       archTypesName=i.get('archTypesName'),
    #                       generate_of_max=i.get('generate_of_max'),
    #                       ArchTypes=i.get('ArchTypes'),
    #                       CountMeter=i.get('CountMeter')
    #                       ).PUT(
    #         custom_settings=i.get('custom_settings')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_GET_JSON():
    # from Construct.Poller.Construct_JSON_Poller import PollerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = PollerJSON(ids=i.get('ids'),
    #                       metersName=i.get('metersName'),
    #                       archTypesName=i.get('archTypesName'),
    #                       generate_of_max=i.get('generate_of_max'),
    #                       ArchTypes=i.get('ArchTypes'),
    #                       CountMeter=i.get('CountMeter')
    #                       ).GET(
    #                         ids=i.get('select_ids'),
    #                         custom_settings=i.get('custom_settings'),
    #                         Record_Values=i.get('Record_Values')
    #                             )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_DELETE_JSON():
    # from Construct.Poller.Construct_JSON_Poller import PollerJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = PollerJSON(ids=i.get('ids'),
    #                       metersName=i.get('metersName'),
    #                       archTypesName=i.get('archTypesName'),
    #                       generate_of_max=i.get('generate_of_max'),
    #                       ArchTypes=i.get('ArchTypes'),
    #                       CountMeter=i.get('CountMeter')
    #                       ).DELETE(
    #                                 ids=i.get('select_ids'),
    #                                 custom_settings=i.get('custom_settings'),
    #                                 Record_Values=i.get('Record_Values')
    #                             )
    #     test_set.append(JSON)
    return JSON_data_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON_param", Generate_POST_JSON())
def test_Poller_POST(type_connect, JSON_param):
    # - Удаляем всю БД
    DeletePoller()

    # по параметрам генерируем JSON
    from Construct.Poller.Construct_JSON_Poller import PollerJSON
    # -->
    JSON = PollerJSON(ids=JSON_param.get('ids'),
                      metersName=JSON_param.get('metersName'),
                      archTypesName=JSON_param.get('archTypesName'),
                      generate_of_max=JSON_param.get('generate_of_max'),
                      ArchTypes=JSON_param.get('ArchTypes'),
                      CountMeter=JSON_param.get('CountMeter')
                      ).POST(
        custom_settings=JSON_param.get('custom_settings')
    )
    # -->

    from Event_System_Tests.Poller import Poller
    print(JSON)
    result = Poller(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_PUT_JSON())
def test_Poller_PUT(type_connect, JSON_param):
    # - Удаляем всю БД
    DeletePoller()

    # по параметрам генерируем JSON
    from Construct.Poller.Construct_JSON_Poller import PollerJSON
    # -->
    JSON = PollerJSON(ids=JSON_param.get('ids'),
                      metersName=JSON_param.get('metersName'),
                      archTypesName=JSON_param.get('archTypesName'),
                      generate_of_max=JSON_param.get('generate_of_max'),
                      ArchTypes=JSON_param.get('ArchTypes'),
                      CountMeter=JSON_param.get('CountMeter')
                      ).PUT(
        custom_settings=JSON_param.get('custom_settings')
    )
    # -->

    from Event_System_Tests.Poller import Poller
    print(JSON)
    result = Poller(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_GET_JSON())
def test_Poller_GET(type_connect, JSON_param):
    # - Удаляем всю БД
    DeletePoller()

    # по параметрам генерируем JSON
    from Construct.Poller.Construct_JSON_Poller import PollerJSON
    # -->
    JSON = PollerJSON(ids=JSON_param.get('ids'),
                      metersName=JSON_param.get('metersName'),
                      archTypesName=JSON_param.get('archTypesName'),
                      generate_of_max=JSON_param.get('generate_of_max'),
                      ArchTypes=JSON_param.get('ArchTypes'),
                      CountMeter=JSON_param.get('CountMeter')
                      ).GET(
        ids=JSON_param.get('select_ids'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
    )
    # -->

    from Event_System_Tests.Poller import Poller
    print(JSON)
    result = Poller(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_DELETE_JSON())
def test_Poller_DELETE(type_connect, JSON_param):
    # - Удаляем всю БД
    DeletePoller()

    # по параметрам генерируем JSON
    from Construct.Poller.Construct_JSON_Poller import PollerJSON
    # -->
    JSON = PollerJSON(ids=JSON_param.get('ids'),
                      metersName=JSON_param.get('metersName'),
                      archTypesName=JSON_param.get('archTypesName'),
                      generate_of_max=JSON_param.get('generate_of_max'),
                      ArchTypes=JSON_param.get('ArchTypes'),
                      CountMeter=JSON_param.get('CountMeter')
                      ).DELETE(
        ids=JSON_param.get('select_ids'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
                                )
    # -->

    from Event_System_Tests.Poller import Poller
    print(JSON)
    result = Poller(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
