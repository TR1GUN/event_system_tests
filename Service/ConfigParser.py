# Здесь расположим парсер наших данных - Это очень важно

import configparser
import os
from Service.Service import get_platform
# from Service import get_platform

# получаем нашу систему -
platform_os = get_platform()
# ----------------------------------------------------------------------------
# path ='/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
settings = '../settings.ini'
# настройки берем из конфига
parser = configparser.ConfigParser()
parser.read(os.path.join(path, settings))
# -----------------------------------------------------------------------------
#                             САМИ НАСТРОЙКИ
# -----------------------------------------------------------------------------
dbpath = parser[platform_os]['dbpath']
IP_address = parser[platform_os]['dbpath']
IP_port = parser[platform_os]['dbpath']

machine_name = parser['Test']['machine_name']
user_login = parser['Test']['user_login']
user_password = parser['Test']['user_password']
address_ssh = parser['Test']['address_ssh']
domain = parser['Test']['domain']
