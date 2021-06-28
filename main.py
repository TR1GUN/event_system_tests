
from Connect.Template_Setup import Setup


api = 'event_db_api'
# JSON = """{"method":"put", "table":"Scheduler", "settings":[{"id":4,"mon":1, "day":2, "hour":3, "min":4}, {"id":2, "mon":255, "day":255, "hour":255, "min":10}]}"""

JSON = """{"method":"get", "table":"Scheduler"}"""

# from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON


# JSON = SchedulerJSON().POST()
# JSON = SchedulerJSON().DELETE()

JSON = """{"method":"put", "table":"MeterTemplates","settings":[{"name":"vasya", "meters":[1,2,4]}, {"name":"pupkin", "meters":[1,2,4]}]}"""
JSON = """{"method":"put", "table":"MeterDataTemplates","settings":[{"name":"Дурное", "types":["one","two"]}, {"name":"влияние"}]}"""
# JSON = """{"method":"put", "table":"MeterDataTemplates","settings":[{"name":"vasya", "types":["one","two"]}, {"name":"pupkin"}]}"""
setup = Setup(JSON=JSON, API=api, type_connect='virtualbox')

print(setup.answer_JSON)