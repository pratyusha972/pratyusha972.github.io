import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "mysecretkey")
    DEBUG = True