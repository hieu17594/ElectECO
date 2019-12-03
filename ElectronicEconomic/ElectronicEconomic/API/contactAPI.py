from flask_restful import Resource, reqparse

class Contact(Resource):
    contact = {
            "PhoneNumber": "00000000",
            "Email": "EmailValue@gmail.com"
        }
    def get(self):
        return self.contact
