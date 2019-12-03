"""
The flask application package.
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import ElectronicEconomic.views
import ElectronicEconomic.apis
