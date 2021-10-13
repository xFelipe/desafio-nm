from celery import Celery
from PIL import Image, UnidentifiedImageError
import logging
import os
from shutil import copyfile

BROKER_USER = os.environ.get('BROKER_USER') or 'guest'
BROKER_HOST = os.environ.get('BROKER_HOST') or 'localhost'

IMAGES_FOLDER = os.environ.get('IMAGES_PATH') or 'images'
RECEIVED_IMAGES_FOLDER = os.path.join(IMAGES_FOLDER, 'received_images')
RESIZED_IMAGES_FOLDER = os.path.join(IMAGES_FOLDER, 'resized_images')
IMAGES_WITH_ERROR_FOLDER = os.path.join(IMAGES_FOLDER, 'error_images')

logging.getLogger().setLevel(logging.INFO)

app = Celery('tasks', broker=f'pyamqp://{BROKER_USER}@{BROKER_HOST}//')


@app.task()
def resize_image(file_name: str, new_width: int, new_height: int):
    """Read a received image, put it resized in a resized images folder and
    delete the origial non-resized image.
    """
    logging.info({
        'file_name': file_name,
        'new_width': new_width,
        'new_height': new_height
    })

    os.makedirs(RESIZED_IMAGES_FOLDER, exist_ok=True)
    os.makedirs(IMAGES_WITH_ERROR_FOLDER, exist_ok=True)

    try:
        image = Image.open(os.path.join(RECEIVED_IMAGES_FOLDER, file_name))
    except UnidentifiedImageError as e:
        logging.error(e)
        copyfile(
            os.path.join(RECEIVED_IMAGES_FOLDER, file_name),
            os.path.join(IMAGES_WITH_ERROR_FOLDER, file_name)
        )
        return

    resized_image = image.resize((new_width, new_height))
    resized_image.save(os.path.join(RESIZED_IMAGES_FOLDER, file_name))
    logging.info(
        f'Image "{file_name}" was resized to {new_width}x{new_height}'
    )
