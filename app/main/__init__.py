# It is important to note that the modules views and errors are imported at the bottom of the app/main/__init__.py script to avoid errors due to circular dependencies

from flask import Blueprint
main = Blueprint('main', __name__)   # The constructor for this class takes two required arguments: the blueprint name and the module or package where the blueprint is located
from . import views, errors          # Importing these modules causes the routes and error handlers to be associated with the blueprint



