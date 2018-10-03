from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/<object_name>/area/<int:length>/<int:width>/')
def area(object_name, length, width):
    if object_name == 'triangle':
        area = 0.5 * length * width
    else:
        area = length * width
    response_area = "Area of {} with length {} and width {} is: {}".format(
        object_name, length, width, area)
    return Response(response_area)
