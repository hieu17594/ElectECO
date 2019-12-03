from flask_restful import Resource, reqparse

class Categories(Resource):
    categories = [
        {
            "category": "Cable & Wires",
            "href": "/product/1",
            "sub_category" :
            [
                {
                    "category": "Cable & Accesseries",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                },
                {
                    "category": "FFC/FFC Connector",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                },
                {
                    "category": "Power Cable",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                }
            ]
        },
        {
            "category": "Sensor",
            "href": "/product/2",
            "sub_category" :
            [
                {
                    "category": "Ambient Light Sensor",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                },
                {
                    "category": "Angle Sensor",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                }
            ]
        },
        {
            "category": "Transistor",
            "href": "/product/2",
            "sub_category" :
            [
                {
                    "category": "Transistor 1",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                },
                {
                    "category": "Transistor 2",
                    "sub_category" :
                    [
                        "Sub 1",
                        "Sub 2",
                        "Sub 3",
                        "Sub 4"
                    ]
                }
            ]
        }
    ]

    def get(self):
        return self.categories
