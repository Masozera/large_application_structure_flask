# is where the application instance is defined

import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')  # The script begins by creating an application. The configuration is taken from theenvironment variable FLASK_CONFIG if it’s defined, or else the default configuration is used
migrate = Migrate(app, db)

@app.shell_context_processor
    def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
    def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)