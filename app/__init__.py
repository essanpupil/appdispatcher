from flask import Flask, Response, render_template


def create_app(template_dir):
    app = Flask(__name__, template_folder=template_dir)

    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/<object_name>/area/<int:length>/<int:width>/', 'area', area)

    return app


def home():
    return render_template('index.html')


def area(object_name, length, width):
    if object_name == 'triangle':
        area = 0.5 * length * width
    else:
        area = length * width
    response_area = "Area of {} with length {} and width {} is: {}".format(
        object_name, length, width, area)
    return Response(response_area)
