class EventDataAPI:
    """
    Итак - Здесь что делаем - Размещаем Наш КЛАСС родитель для работы с Event_API

    """

    API = 'event_db_api'
    Type_Connect = 'virtualbox'

    def SETUP(self, JSON):
        """
        Основной КЛАСС запуска - Это очень важная хрень как ни крууути
        дап

        :param JSON: Принимает JSON который должны отправить
        :return: Возвращает результат операции
        """

        # импортируем класс для отправки приниятия JSON
        from Connect.Template_Setup import Setup
        import time

        # Замеряем время
        time_start = time.time()

        # Запускаем
        setup = Setup(JSON=JSON, API=self.API, type_connect=self.Type_Connect)
        # Получаем ответ
        answer_JSON = setup.answer_JSON

        # Получаем время
        time_finis = time.time()

        # ----------ПРИНТУЕМ---------------
        print('JSON Обрабабатывался:', time_finis - time_start)
        # Навсякий случай печатаем JSON ответа и что отправляли
        print('JSON\n', JSON)
        print('answer_JSON\n', answer_JSON)
        # ---------------------------------

        return answer_JSON
