from flask_restful import Resource, reqparse

class Products(Resource):
    products = [
            {
                'name': "sensor 1",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 2",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 3",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 4",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 5",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 6",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 1",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 2",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 3",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 4",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 5",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 6",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 1",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 2",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 3",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 4",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 5",
                'price': "10.000",
                'link': "#"
            },
            {
                'name': "sensor 6",
                'price': "10.000",
                'link': "#"
            },
        ]
    def get(self):
        return self.products
