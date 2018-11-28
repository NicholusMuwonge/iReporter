from flask import Flask,make_response



def creat_app():
    app=Flask(__name__)
    return app

from app.routes import app
