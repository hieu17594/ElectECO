from ElectronicEconomic import app
from flask_restful import Resource, reqparse, Api

api = Api(app)

from ElectronicEconomic.API.categoriesAPI import Categories
from ElectronicEconomic.API.languagesAPI import Languages
from ElectronicEconomic.API.contactAPI import Contact
from ElectronicEconomic.API.productsAPI import Products

api.add_resource(Contact, "/api/contact")
api.add_resource(Languages, "/api/languages")
api.add_resource(Categories, "/api/categories")
api.add_resource(Products, "/api/products")
