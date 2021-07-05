# Здесь - выясняем что записалось по факту


class DataBaseWasRecording:
    """
    Класс что нужен для того чтоб узнать что изменилось в в БД

    поулчает разница
    """

    database_was_recording = []

    def __init__(self,
                 # БД до записи
                 database_before,
                 # БД после записи
                 database_after
                 ):

        self.database_was_recording = self.get_discrepancy(database_before=database_before,
                                                           database_after=database_after)

    def get_discrepancy(self, database_before, database_after):

        from copy import deepcopy

        database_was_recording = deepcopy(database_after)

        # Теперь вычетаем все то что было в БД ДО

        for element_before in database_before:

            idx = element_before.get('id')
            if idx is not None:
                for element_after in database_after:
                    if element_after.get('id') == idx:
                        # удаляем его
                        database_was_recording.remove(element_after)

        return database_was_recording
