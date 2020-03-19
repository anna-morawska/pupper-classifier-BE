import uuid
from flask_restplus import Resource
from google.cloud import storage
from firebase import firebase
from werkzeug.datastructures import FileStorage
from app import api, app, classify_image, my_utils

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

firebase = firebase.FirebaseApplication('https://pupper-classifier.appspot.com/')
client = storage.Client()
bucket = client.get_bucket('pupper-classifier.appspot.com')

def random_file_name(ext, length):
    return  str(uuid.uuid4())[0:length]+"."+ext


@api.route('/upload-image/')
@api.expect(upload_parser)
class Upload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        is_image_valid = my_utils.validate_image(uploaded_file)

        if is_image_valid[0]:
            uploaded_file = uploaded_file.read()
            file_name = random_file_name("jpg", 10)

            image_blob = bucket.blob(file_name)
            image_blob.upload_from_string(
                uploaded_file,
                content_type='image/jpg'
            )
            response = classify_image.classify_image(uploaded_file)

            return {'data': response}, 201
        else:
             return {'message': is_image_valid[1]}, 400

