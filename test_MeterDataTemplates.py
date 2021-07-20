# MeterDataTemplates
# Здесь напишем тестовые функции для MeterDataTemplates
import pytest

# ----------------------------------------------------------------------------------------------------->

JSON_data_set = \
    [
        {
            # Либо количество автосгенерирвоанных имен, либо список имен для генерации , либо Полноценный JSON
            'name': 1,
            # либо количество ArchTypes для автогенерации либо список ArchTypes
            'types': 3,
            # Уникальны ли ArchTypes для каждого name
            'unique_types': True,
            # ИМЕНА которые запрашиваем  - Либо сколько, либо какие - 0 запрашиваем все
            'names': 1,
            # Записываем или нет полученные значения
            'Record_Values': True,
            # Свои значения - Не проверяются
            'custom_settings': None,
        },
        {
            'name': 1,
            'types': 3,
            'unique_types': True,
            'custom_settings': None,
            'names': 1,
            'Record_Values': True,
        },
    ]

# ----------------------------------------------------------------------------------------------------->

def DeleteMeterDataTemplates():
    from time import sleep
    from Template.DataBase.DataBase_Delete import DataBaseDELETE

    # Сначала чистим нашу БД
    Delete = DataBaseDELETE({'table': 'MeterDataTemplates'})
    # спим
    sleep(2)
# ----------------------------------------------------------------------------------------------------->

# @pytest.fixture()
def Generate_POST_JSON():
    # from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = MeterDataTemplatesJSON(name=i.get('name'),
    #                                   types=i.get('types'),
    #                                   unique_types=i.get('unique_types')).POST(
    #         custom_settings=i.get('custom_settings')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_PUT_JSON():
    # from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = MeterDataTemplatesJSON(name=i.get('name'),
    #                                   types=i.get('types'),
    #                                   unique_types=i.get('unique_types')).PUT(
    #         custom_settings=i.get('custom_settings')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_GET_JSON():
    # from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = MeterDataTemplatesJSON(name=i.get('name'),
    #                                   types=i.get('types'),
    #                                   unique_types=i.get('unique_types')).GET(
    #         names=i.get('names'),
    #         custom_settings=i.get('custom_settings'),
    #         Record_Values=i.get('Record_Values')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


def Generate_DELETE_JSON():
    # from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON
    #
    # test_set = []
    # for i in JSON_data_set:
    #     JSON = MeterDataTemplatesJSON(name=i.get('name'),
    #                                   types=i.get('types'),
    #                                   unique_types=i.get('unique_types')).DELETE(
    #         names=i.get('names'),
    #         custom_settings=i.get('custom_settings'),
    #         Record_Values=i.get('Record_Values')
    #     )
    #     test_set.append(JSON)
    return JSON_data_set


# ----------------------------------------------------------------------------------------------------->
#                                         Тестовые запуски
# ----------------------------------------------------------------------------------------------------->
# Generate_JSON = Generate_JSON()
@pytest.mark.parametrize("JSON_param", Generate_POST_JSON())
def test_MeterDataTemplates_POST(type_connect, JSON_param):


    # - Удаляем всю БД
    DeleteMeterDataTemplates()
    # по параметрам генерируем JSON
    # -->
    print('------->',JSON_param)
    from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON

    JSON = MeterDataTemplatesJSON(name=JSON_param.get('name'),
                                  types=JSON_param.get('types'),
                                  unique_types=JSON_param.get('unique_types')).POST(
        custom_settings=JSON_param.get('custom_settings')
    )


    from Event_System_Tests.MeterDataTemplates import MeterDataTemplates
    print(JSON)
    result = MeterDataTemplates(Type_Connect=type_connect).POST(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_PUT_JSON())
def test_MeterDataTemplates_PUT(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteMeterDataTemplates()
    # по параметрам генерируем JSON
    # -->

    from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON

    JSON = MeterDataTemplatesJSON(name=JSON_param.get('name'),
                                  types=JSON_param.get('types'),
                                  unique_types=JSON_param.get('unique_types')).PUT(
        custom_settings=JSON_param.get('custom_settings')
    )


    from Event_System_Tests.MeterDataTemplates import MeterDataTemplates
    print(JSON)
    result = MeterDataTemplates(Type_Connect=type_connect).PUT(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_GET_JSON())
def test_MeterDataTemplates_GET(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteMeterDataTemplates()
    # по параметрам генерируем JSON
    # -->
    Record = True
    from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON

    JSON = MeterDataTemplatesJSON(name=JSON_param.get('name'),
                                  types=JSON_param.get('types'),
                                  unique_types=JSON_param.get('unique_types')).GET(
        names=JSON_param.get('names'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
        # Record_Values = Record
    )

    from Event_System_Tests.MeterDataTemplates import MeterDataTemplates

    result = MeterDataTemplates(Type_Connect=type_connect).GET(JSON=JSON)

    assert result == []


@pytest.mark.parametrize("JSON_param", Generate_DELETE_JSON())
def test_MeterDataTemplates_DELETE(type_connect, JSON_param):
    # - Удаляем всю БД
    DeleteMeterDataTemplates()
    # по параметрам генерируем JSON
    # -->

    from Construct.MeterDataTemplates.Construct_JSON_MeterDataTemplates import MeterDataTemplatesJSON

    JSON = MeterDataTemplatesJSON(name=JSON_param.get('name'),
                                  types=JSON_param.get('types'),
                                  unique_types=JSON_param.get('unique_types')).DELETE(
        names=JSON_param.get('names'),
        custom_settings=JSON_param.get('custom_settings'),
        Record_Values=JSON_param.get('Record_Values')
    )
    # -->

    from Event_System_Tests.MeterDataTemplates import MeterDataTemplates
    print(JSON)
    result = MeterDataTemplates(Type_Connect=type_connect).DELETE(JSON=JSON)

    assert result == []
