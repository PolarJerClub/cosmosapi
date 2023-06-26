import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY as we find ourselves in
# Allow outside files/folders to be added to the project from the base directory

class Config():
    """
        Set config variables for the flask app
        using environment variables where available other
        create the config variables if not already not
    
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess this, yoink'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off database updates from sqlalchemy