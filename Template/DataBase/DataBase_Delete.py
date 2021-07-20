# Класс для Удаления данных JSON
from Template.Template_SQL_Database import TemplateSQL


class DataBaseDELETE(TemplateSQL):
    command = ' DELETE FROM  '

    def __init__(self, JSON):
        """
        Функция удаления для любой таблицы по JSON

        """

        self.definition_table.get(JSON['table'])(self)

    def _Delete_all_Scheduler(self):
        """
        Здесь удаляем все из таблицы Scheduler
        :return:
        """

        # Итак - составляем команду
        command = self.command + ' Scheduler '

        result = self.execute_command(command=command)

    def _Delete_all_Poller(self):
        """
        Здесь удаляем все из таблицы Poller
        :return:
        """

        # Итак - составляем команду
        command = self.command + ' Poller '

        result = self.execute_command(command=command)

    def _Delete_all_MeterTemplates(self):
        """
        Здесь удаляем все из таблицы MeterTemplates
        :return:
        """

        # Итак - составляем команду
        command = self.command + ' MeterTemplates '

        result = self.execute_command(command=command)

    def _Delete_all_MeterDataTemplates(self):
        """
        Здесь удаляем все из таблицы MeterDataTemplates
        :return:
        """

        # Итак - составляем команду
        command = self.command + ' MeterDataTemplates '

        result = self.execute_command(command=command)

    def _Delete_all_Manager(self):
        """
        Здесь удаляем все из таблицы Manager
        :return:
        """

        # Итак - составляем команду
        command = self.command + ' Manager '

        result = self.execute_command(command=command)

    definition_table = \
        {
            'Manager': _Delete_all_Manager,
            'MeterDataTemplates': _Delete_all_MeterDataTemplates,
            'MeterTemplates': _Delete_all_MeterTemplates,
            'Poller': _Delete_all_Poller,
            'Scheduler': _Delete_all_Scheduler,
        }
