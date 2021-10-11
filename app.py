import os
from datetime import datetime
from flask import Flask, request
from tasks import resize_image

RECEIVED_IMAGES_FOLDER = 'received_images'


app = Flask(__name__)

@app.route('/send-image', methods=['POST'])
def send_image():
    if not os.path.isdir(RECEIVED_IMAGES_FOLDER):
        os.mkdir(RECEIVED_IMAGES_FOLDER)

    file = request.files['image']
    new_file_name = datetime.now().strftime('%y_%m_%d__%H_%M_%S-') + file.filename
    new_file_path = os.path.join(RECEIVED_IMAGES_FOLDER,new_file_name)
    with open(new_file_path, 'wb') as new_file:
        new_file.write(file.read())

    resize_image.delay(new_file_name, 384, 384)

    return {'message': 'Task sent'}, 200


if __name__ == '__main__':
    app.run(debug=True)
