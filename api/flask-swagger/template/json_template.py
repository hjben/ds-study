import json
from flask import Flask, request, Response
from flask_restplus import Api, Resource
from flask_cors import CORS


# Flask app
app = Flask(__name__)
CORS(app)

api = Api(app, version='1.0', title='Test API', doc='/__swagger__', description='A test API')
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
ns_conf = api.namespace('test', description='Test operations')

input_parser = ns_conf.parser()
input_parser.add_argument('input_data', type=str, help='input data', location='form')


# Custom API class
@ns_conf.route("")
@ns_conf.param("input_json", "json input")
class Test(Resource):
    @staticmethod
    @ns_conf.expect(input_parser)
    def post():
        result = dict()
        input_json = request.get_json()

        if not input_json:
            input_json = eval(input_parser.parse_args().pop('input_json'))

        # place custom variables and function
        #
        #

        return Response(json.dumps(result, ensure_ascii=False, indent=2).encode('utf-8'),
                        content_type='application/json; charset=utf-8')


# Run api (main)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
