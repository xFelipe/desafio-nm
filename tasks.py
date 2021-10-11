from celery import Celery
import logging


broker_host = 'localhost'

logging.getLogger().setLevel(logging.INFO)
app = Celery('tasks', broker=f'pyamqp://guest@{broker_host}//')


@app.task
def resize_image(image_path: str, new_width: int, new_height: int):
    """Read a received image, put it resized in a resized images folder and
    delete the origial non-resized image.
    """
    logging.info(f'Image "{image_path}" was resized to {new_width}x{new_height}')
