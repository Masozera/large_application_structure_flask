import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self): # The setUp() method tries to create an environment for the test that is close to that of a running application
        self.app = create_app('testing') # It first creates an application configured for testing
        self.app_context = self.app.app_context() # and acti‐vates its context
        self.app_context.push()
        db.create_all()   # Then it creates a brand-new database for the tests using FlaskSQLAlchemy’s create_all() method. 

    def tearDown(self):   # The database and the application context are removed in the tearDown() method.
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self): # The first test ensures that the application instance exists. T
        self.assertFalse(current_app is None)
    def test_app_is_testing(self): #  The second test ensures that the application is running under the testing configuration.
        self.assertTrue(current_app.config['TESTING'])

    
