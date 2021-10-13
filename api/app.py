import os
from datetime import datetime
from flask import Flask, request
from tasks import resize_image

IMAGES_FOLDER = os.environ.get('IMAGES_PATH') or '../images'
RECEIVED_IMAGES_FOLDER = os.path.join(IMAGES_FOLDER, 'received_images')
DATETIME_FORMAT = '%y_%m_%d__%H_%M_%S-'


app = Flask(__name__)

@app.route('/send-image', methods=['POST'])
def send_image():
    os.makedirs(RECEIVED_IMAGES_FOLDER, exist_ok=True)

    file = request.files.get('image')
    if not file:
        return {'message': 'image field is required.'}, 400

    new_file_name = datetime.now().strftime(DATETIME_FORMAT) + file.filename
    new_file_path = os.path.join(RECEIVED_IMAGES_FOLDER, new_file_name)
    with open(new_file_path, 'wb') as new_file:
        new_file.write(file.read())

    resize_image.delay(new_file_name, 384, 384)

    return {'message': 'Task sent', 'file_name': new_file_name}, 200


if __name__ == '__main__':
    app.run(debug=True)
