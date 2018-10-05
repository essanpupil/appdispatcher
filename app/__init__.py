from flask import Flask, Response, render_template


def create_app(prefix):
    app = Flask(__name__, template_folder='templates_' + prefix)

    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/<object_name>/area/<int:length>/<int:width>/', 'area', area)

    return app


def home(object_name=None):
    return render_template('index.html')


def area(object_name, length, width):
    if object_name == 'triangle':
        area = 0.5 * length * width
    else:
        area = length * width
    response_area = "Area of {} with length {} and width {} is: {}".format(
        object_name, length, width, area)
    return Response(response_area)


def default_app():
    app = Flask(__name__, template_folder='templates_geometry')

    app.add_url_rule('/<object_name>/', 'home', home)
    app.add_url_rule('/<object_name>/area/<int:length>/<int:width>/', 'area', area)

    return app

this_app = default_app()
