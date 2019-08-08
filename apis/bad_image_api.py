from __future__ import division, absolute_import, print_function

from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields
from flask import jsonify

from service.bad_image_service import get_image_prediction

api = Namespace(name='bad image', description='apis for filtering bad images')

# The JSON Model for the data being sent by the user
text_msg_model = api.model("text_msg_model", {
    "urls": fields.String("urls splitted by |")
})


@api.route("/bad_image")
class BadImage(Resource):
    """Resource
        The embedding generator
    """

    @api.doc('Receive a string of urls splitted by |')
    @api.expect(text_msg_model)
    def post(self):
        payload = api.payload
        urls = payload['urls']
        url_list = str(urls).split('|')

        result_prediction_list = get_image_prediction(url_list)
        print("\n\n\n", result_prediction_list.shape, "\n\n\n")
        return jsonify({'predictions': result_prediction_list.tolist()})
