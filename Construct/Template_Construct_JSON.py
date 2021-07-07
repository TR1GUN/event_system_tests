# Здесь расположим наш шаблон для конструирования JSON от которого будем наследоваться

class TemplateJSON:

    """
    Итак - класс ролдитель для всех таблиц

    """
    Generate_data = {}

    JSON = {"table": "Table"}

    def RecordData(self):

        """
        Этот метод Записывает То что мы сгенерировали в конструкторе класса
        :return:
        """

        from Template.Template_DataBase_by_JSON import DataBase

        record_JSON = {'settings': self.Generate_data}
        record_JSON.update(self.JSON)
        record = DataBase().INSERT(JSON=record_JSON)