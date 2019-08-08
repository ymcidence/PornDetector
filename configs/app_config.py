from __future__ import division, absolute_import, print_function
import logging.config
import os

PROJECT_DIR_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
SRC_DIR_ROOT = PROJECT_DIR_ROOT


class ConfigSettings(object):
    """ Config constants used in this app"""

    # app meta data
    APP_TITLE = 'BAD IMAGE'
    APP_VERSION = '1.0'
    APP_DESCRIPTION = 'A restplust API service'

    # get dev/test/prod running mode
    EXECUTION_ENV = os.getenv('PERSONA_EXECUTION_ENV', 'dev')

    # running environment configs, choose one
    if EXECUTION_ENV == 'prod':
        DEBUG = False
    else:
        DEBUG = True

    # the port number used by the http server
    HTTP_PORT_NUMBER = '6000'


######################## Logger ########################
# The .conf locates at the same folder with this file

logging_conf_path = os.path.normpath(SRC_DIR_ROOT + '/configs/logging.conf')

logging.config.fileConfig(logging_conf_path)

# The logger name here should be contained in the logging.conf
log = logging.getLogger("api_server")
