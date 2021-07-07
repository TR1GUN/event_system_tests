# Здесь расположим класс родитель

class TemplateSQL:

    def execute_command(self, command):

        """
        Исполняем команду
        :param command:
        :return:
        """

        from Service.SQL import execute_command

        result = execute_command(command=command)

        return result