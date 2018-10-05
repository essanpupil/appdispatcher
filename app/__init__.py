from flask import Flask, Response


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/<object_name>/area/<int:length>/<int:width>/', 'area', area)

    return app


def home():
    return "Hello World!"


def area(object_name, length, width):
    if object_name == 'triangle':
        area = 0.5 * length * width
    else:
        area = length * width
    response_area = "Area of {} with length {} and width {} is: {}".format(
        object_name, length, width, area)
    return Response(response_area)
