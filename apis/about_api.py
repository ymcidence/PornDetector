from __future__ import division, absolute_import, print_function

from flask_restplus import Namespace
from flask_restplus import Resource
from flask import jsonify


api = Namespace(name='about', description='about this module')


@api.route('/')
class AboutModule(Resource):
    """Resource
        User Login
    """
    @api.doc('About this module')
    def get(self):
        return jsonify({'message' : 'You are a bad image!!!!!'})

