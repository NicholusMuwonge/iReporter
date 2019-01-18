from flask import Flask, make_response
from api.routes import mod

def creat_app():
    app=Flask(__name__)
    return app