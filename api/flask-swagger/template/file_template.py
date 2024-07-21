import json
from flask import Flask, request, Response
from flask_restplus import Api, Resource
from flask_cors import CORS
from werkzeug.datastructures import FileStorage

# Flask app
app = Flask(__name__)
CORS(app)

api = Api(app, version='1.0', title='Test API', doc='/__swagger__', description='A test API')
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
ns_conf = api.namespace('test', description='Test operations')

upload_parser = ns_conf.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)


# Custom API class
@ns_conf.route("/")
class Test(Resource):
    @staticmethod
    @ns_conf.expect(upload_parser)
    def post():
        result = dict()
        input_file = None

        if request.files:
            input_file = request.files['file']
        elif upload_parser.parse_args():
            input_file = upload_parser.parse_args().pop('file')

        if not input_file:
            raise FileNotFoundError

        # place custom variables and function
        #
        #

        return Response(json.dumps(result, ensure_ascii=False, indent=2).encode('utf-8'),
                        content_type='application/json; charset=utf-8')


# Run api (main)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
