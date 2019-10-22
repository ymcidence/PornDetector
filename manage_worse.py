#!/usr/bin/env python

""" Initialization for the whole app.
    Used Manager to handle the running options
"""
from __future__ import division, absolute_import, print_function

import unittest

from flask import Flask
from flask import Blueprint
from flask_restplus import Api
from flask_script import Manager

from configs.app_config import ConfigSettings
from configs.app_config import log, PROJECT_DIR_ROOT

SRC_DIR_ROOT = PROJECT_DIR_ROOT

#########################################################
# TODO import your new api-modules here
# from apis.about_api import api as about_api_ns
from apis.worse_image_api import api as bad_image_api

######################## Flask Rest API ########################
blueprint = Blueprint('apis', __name__)

api = Api(blueprint,
          title=ConfigSettings.APP_TITLE,
          version=ConfigSettings.APP_VERSION,
          description=ConfigSettings.APP_DESCRIPTION
          )

############# Add your apis namespace here #############
# TODO add your api to the apps
# api.add_namespace(about_api_ns, path='/about')
api.add_namespace(bad_image_api, path='/hehe')

############# Manager commands #############
app = Flask(__name__)

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    log.info('>>>>> Start running server <<<<<< \n')
    app.run(host="0.0.0.0", port=ConfigSettings.HTTP_PORT_NUMBER, debug=ConfigSettings.DEBUG)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover(SRC_DIR_ROOT + '/tests', pattern='tests*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
