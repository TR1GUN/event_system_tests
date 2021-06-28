# здесь генерируем поле Нейм

class GenerateFieldName:
    """
    Класс для генерации ну

    """

    settings = []

    def __init__(self, name: int = 1):

        if (type(name) != int) or (name < 1):
            name = 1
        settings = []

        adding_name = 'Adding_name_'
        for i in range(name):
            settings.append({"name": adding_name + str(i)})

        self.settings = settings

    def GET_name_list(self):


        from copy import deepcopy

        names = []

        settings = deepcopy(self.settings)

        for setting in settings :
            names.append(setting.get("name"))


        return names