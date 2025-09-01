from app import app

import shutil 
import os

def initialise_db():
    shutil.rmtree(app.config['CREATOR_IMAGE_FOLDER'])
    os.makedirs(app.config['CREATOR_IMAGE_FOLDER'])

    return

@app.shell_context_processor
def make_shell_context():
    return{
        'app':app,
        'initialise_db':initialise_db
    }