class Config:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/silly_wash'
    SECRET_KEY = 'this is a secret key'