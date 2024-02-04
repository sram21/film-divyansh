
from flask import Blueprint

div_film = Blueprint('film', __name__)

from . import routes