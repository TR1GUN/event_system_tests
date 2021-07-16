
# Здесь напишем тестовые функции для MeterTemplates
import pytest

# ----------------------------------------------------------------------------------------------------->
JSON_data_set = \
    [
        {
            # Либо количество автосгенерирвоанных имен, либо список имен для генерации , либо Полноценный JSON
            'name':  1,
            # либо количество счетчиков для автогенерации либо список их айдишников
            'meter':  3,
            # Уникален ли набор счетчиков для каждого NAME
            'unique_meter': True ,
            # ИМЕНА которые удалчяемп  - Либо сколько, либо какие - 0 запрашиваем все
            'names': 1,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None,
        },
        {
            'name':  1,
            'meter':  3,
            'unique_meter': True ,
            'custom_settings': None,
            'names': 1,
            'Record_Values': True,
        },
    ]


# @pytest.fixture()
def Generate_POST_JSON():
    from Construct.MeterTemplates.Construct_JSON_MeterTemplates import MeterTemplatesJSON

    test_set = []
    for i in JSON_data_set:
        JSON = MeterTemplatesJSON(name=i.get('name'),
                                  meter=i.get('meter'),
                                  unique_meter=i.get('unique_meter')).POST(
                                                                                custom_settings=i.get('custom_settings')
                                                                               )
        test_set.append(JSON)
    return test_set


def Generate_PUT_JSON():
    from Construct.MeterTemplates.Construct_JSON_MeterTemplates import MeterTemplatesJSON

    test_set = []
    for i in JSON_data_set:
        JSON = MeterTemplatesJSON(name=i.get('name'),
                                  meter=i.get('meter'),
                                  unique_meter=i.get('unique_meter')).PUT(
                                                                              custom_settings=i.get('custom_settings')
                                                                              )
        test_set.append(JSON)
    return test_set


def Generate_GET_JSON():
    from Construct.MeterTemplates.Construct_JSON_MeterTemplates import MeterTemplatesJSON

    test_set = []
    for i in JSON_data_set:
        JSON = MeterTemplatesJSON(name=i.get('name'),
                                  meter=i.get('meter'),
                                  unique_meter=i.get('unique_meter')).GET(
                                                                            names=i.get('names'),
                                                                            custom_settings=i.get('custom_settings'),
                                                                            Record_Values=i.get('Record_Values')
                                                                               )
        test_set.append(JSON)
    return test_set


def Generate_DELETE_JSON():
    from Construct.MeterTemplates.Construct_JSON_MeterTemplates import MeterTemplatesJSON

    test_set = []
    for i in JSON_data_set:
        JSON = MeterTemplatesJSON(name=i.get('name'),
                                  meter=i.get('meter'),
                                  unique_meter=i.get('unique_meter')).DELETE(
                                                                            names=i.get('names'),
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
def test_MeterTemplates_POST(type_connect, JSON):
    from Event_System_Tests.MeterTemplates import MeterTemplates
    print(JSON)
    result = MeterTemplates(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_PUT_JSON())
def test_MeterTemplates_PUT(type_connect, JSON):
    from Event_System_Tests.MeterTemplates import MeterTemplates
    print(JSON)
    result = MeterTemplates(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_GET_JSON())
def test_MeterTemplates_GET(type_connect, JSON):
    from Event_System_Tests.MeterTemplates import MeterTemplates
    print(JSON)
    result = MeterTemplates(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON", Generate_DELETE_JSON())
def test_MeterTemplates_DELETE(type_connect, JSON):
    from Event_System_Tests.MeterTemplates import MeterTemplates
    print(JSON)
    result = MeterTemplates(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
