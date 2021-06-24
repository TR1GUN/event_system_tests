



from Connect.Template_Setup import Setup


api = 'event_db_api'
# JSON = """{"method":"put", "table":"Scheduler", "settings":[{"id":4,"mon":1, "day":2, "hour":3, "min":4}, {"id":2, "mon":255, "day":255, "hour":255, "min":10}]}"""

JSON = """{"method":"get", "table":"Scheduler"}"""

from Construct.Scheduler.Construct_JSON_Scheduler import SchedulerJSON


JSON = SchedulerJSON().POST()
# JSON = SchedulerJSON().DELETE()
setup = Setup(JSON=JSON, API=api, type_connect='virtualbox')

print(setup.answer_JSON)