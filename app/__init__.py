from flask import Flask
from config import Config

# VIDEO_ROOT = '/unreliable/DATASETS/bdd-data-v1/videos/train-parts/'
VIDEO_ROOT = '/home/ivan/Downloads/europilot_data/'

app = Flask(__name__)
app._static_folder = VIDEO_ROOT
app.config.from_object(Config)

from app import routes