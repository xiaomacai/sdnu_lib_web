# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config():
    SECRET_KEY = os.getenv('SECRET_KEY' or 'EO#34AS25sfaASJE#@$3@#4')
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {
    'developement': Config,

    'default': Config
}
