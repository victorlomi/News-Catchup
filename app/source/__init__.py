from flask import Blueprint

# create blueprint for the components in this module
# to connect to app instance.
bp = Blueprint('source', __name__)

# import modules to include package members.
from app.source import routes
