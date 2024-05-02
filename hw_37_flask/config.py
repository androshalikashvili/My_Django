import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin_root:Admin_1234@localhost:3307/it_step37"
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.urandom(32)