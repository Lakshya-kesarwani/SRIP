from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import faculty_routes, intern_routes, coordinator_routes, auth_routes, home_routes