# Здесь расположим парсер наших данных - Это очень важно

import configparser
import os

# ----------------------------------------------------------------------------------------------------------------
# path ='/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
settings = '../settings.ini'
# настройки берем из конфига
parser = configparser.ConfigParser()
parser.read(os.path.join(path, settings))
# ---------------------------------------- Получение информации об ОС ---------------------------------------------
def get_platform():
    """
    Получение информации о системе - Это важно

    :return:
    """

    import platform

    # получаем нашу систему -
    platform_os = platform.system()

    if 'Windows' in platform_os:
        platform_os = 'Windows'
    else:
        platform_os = 'Linux'

    return platform_os
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
#                             САМИ НАСТРОЙКИ
# ------------------------------------------------------------------------------------------------------------------
platform_os = get_platform()

targetimage = (parser[platform_os]['IP_address'], int(parser[platform_os]['IP_port']))
machine_name = parser['Test']['machine_name']
user_login = parser['Test']['user_login']
user_password = parser['Test']['user_password']
address_ssh = parser['Test']['address_ssh']
domain = parser['Test']['domain']