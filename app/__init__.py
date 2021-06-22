#This constructor imports most of the flask extensions

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


# becausethere is no application instance to initialize the extensions with
# it creates them uninitialized by passing no arguments into their constructors.
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()





def create_app(config_name): # The create_app() function is the application factory, which takes as an argument the name of a configuration to use for the application.
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # The configuration settings stored in one of the classes defined in confg.py can be imported directly into the application using the from_object() method available in Flask’s app.config configuration object
    config[config_name].init_app(app)           #  The configuration object is selected by name from the config dictionary
    
    # Once an application is created and configured, the extensions can be initialized. Calling init_app() on the exten‐sions that were created earlier completes their initialization.
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here

    from .main import main as main_blueprint #The blueprint is registered with the application inside the create_app() factory function
    app.register_blueprint(main_blueprint)

    return app



