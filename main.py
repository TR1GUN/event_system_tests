#
# from Connect.Template_Setup import Setup
#
#
# api = 'event_db_api'
# # JSON = """{"method":"put", "table":"Scheduler", "settings":[{"id":4,"mon":1, "day":2, "hour":3, "min":4}, {"id":2, "mon":255, "day":255, "hour":255, "min":10}]}"""
#
# JSON = """{"method":"get", "table":"Scheduler"}"""
#
# # from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON
#
#
# # JSON = SchedulerJSON().POST()
# # JSON = SchedulerJSON().DELETE()
#
# JSON = """{"method":"put", "table":"MeterTemplates","settings":[{"name":"vasya", "meters":[1,2,4]}, {"name":"pupkin", "meters":[1,2,4]}]}"""
# JSON = """{"method":"put", "table":"MeterDataTemplates","settings":[{"name":"Дурное", "types":["one","two"]}, {"name":"влияние"}]}"""
# # JSON = """{"method":"put", "table":"MeterDataTemplates","settings":[{"name":"vasya", "types":["one","two"]}, {"name":"pupkin"}]}"""
#
# JSON = """{"method":"post", "table":"Scheduler", "settings":[{"id":1, "mon":1, "day":2, "hour":4, "min":8}, {"id":1, "mon":4, "day":6, "hour":8, "min":10}]}"""
# setup = Setup(JSON=JSON, API=api, type_connect='virtualbox')
#
# print(setup.answer_JSON)
#



data_base_before = [{'id': 16, 'mon': 7, 'day': 11, 'hour': 23, 'min': 27}, {'id': 20, 'mon': 4, 'day': 25, 'hour': 12, 'min': 3}]
data_base_after = [{'id': 1, 'mon': 255, 'day': 255, 'hour': 255, 'min': 14}, {'id': 2, 'mon': 255, 'day': 255, 'hour': 255, 'min': 14}, {'id': 3, 'mon': 255, 'day': 255, 'hour': 255, 'min': 15}, {'id': 4, 'mon': 255, 'day': 255, 'hour': 255, 'min': 1}, {'id': 5, 'mon': 255, 'day': 255, 'hour': 255, 'min': 24}, {'id': 6, 'mon': 255, 'day': 255, 'hour': 255, 'min': 15}, {'id': 7, 'mon': 255, 'day': 255, 'hour': 255, 'min': 22}, {'id': 8, 'mon': 255, 'day': 255, 'hour': 255, 'min': 25}, {'id': 9, 'mon': 255, 'day': 255, 'hour': 255, 'min': 5}, {'id': 10, 'mon': 255, 'day': 255, 'hour': 255, 'min': 14}, {'id': 11, 'mon': 3, 'day': 7, 'hour': 24, 'min': 8}, {'id': 12, 'mon': 2, 'day': 21, 'hour': 18, 'min': 20}, {'id': 15, 'mon': 2, 'day': 11, 'hour': 5, 'min': 25}, {'id': 17, 'mon': 2, 'day': 30, 'hour': 19, 'min': 29}, {'id': 18, 'mon': 3, 'day': 27, 'hour': 28, 'min': 27}, {'id': 19, 'mon': 2, 'day': 5, 'hour': 4, 'min': 27}]


print(data_base_after - data_base_before)