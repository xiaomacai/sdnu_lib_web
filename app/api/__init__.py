from flask import Blueprint

api = Blueprint('api', __name__)

from . import views
__all__ = ['opt_db']