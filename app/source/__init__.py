from flask import Blueprint

bp = Blueprint('source', __name__)

from app.source import routes
