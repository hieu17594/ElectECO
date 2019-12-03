from flask_restful import Resource, reqparse

class Languages(Resource):
    languages = [
            {"Language": "ENG"},
            {"Language": "VN"}
        ]
    def get(self):
        return self.languages
