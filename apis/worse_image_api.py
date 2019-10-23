from __future__ import division, absolute_import, print_function
import numpy as np
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields
from flask import jsonify

from service.bad_image_service import get_image_prediction
from service.very_bad_image_service import get_image_prediction as get_image_prediction2

api = Namespace(name='worse image', description='apis for filtering bad images')

# The JSON Model for the data being sent by the user
text_msg_model = api.model("text_msg_model", {
    "urls": fields.String("urls splitted by |")
})


def prob_process(p1, p2):
    r_0 = p1[:, 1]
    r_non = p1[:, 0]
    r_1_3 = p2 * r_non[:, None]
    r = np.concatenate([r_0[:, None], r_1_3], axis=1)
    return r


@api.route("/worse_image/")
class WorseImage(Resource):
    """Resource
        The embedding generator
    """

    @api.doc('Receive a string of urls splitted by |')
    @api.expect(text_msg_model)
    def post(self):
        payload = api.payload
        urls = payload['urls']
        url_list = str(urls).split('|')

        rslt1 = get_image_prediction(url_list, 1)
        rslt2 = get_image_prediction2(url_list)

        probs = prob_process(rslt1, rslt2)
        preds = (np.argmax(probs, 1) < 3).astype(np.int32)

        print("\n\n\n", probs.shape, "\n\n\n")
        return jsonify({'predictions': preds.tolist(), 'probs': probs.tolist()})


def _test():
    name = 'file:///home/ymcidence/Workspace/CodeGeass/PornDetector/2.jpg'
    url_list = [name, name]
    rslt1 = get_image_prediction(url_list, 1)
    rslt2 = get_image_prediction2(url_list)
    probs = prob_process(rslt1, rslt2)
    print(probs)


if __name__ == '__main__':
    _test()
