import os 
from socket import gethostname 

basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bespoke-lite-for-cd-not-even-used-really'
    BOOTSTRAP_BOOTSWATCH_THEME = 'darkly'
    PLACEHOLDER_IMAGE = 'No-Image-Placeholder.svg'

    if 'live' not in gethostname():
        CREATOR_IMAGE_FOLDER = os.getcwd() + '\\app\\images'
    else:
        CREATOR_IMAGE_FOLDER = os.getcwd() + '/app/images'
