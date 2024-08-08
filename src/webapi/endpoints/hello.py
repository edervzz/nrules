""" Create a new workflow """
from flask import Blueprint


hello_blueprint = Blueprint("Hello", __name__)


@hello_blueprint.get("/hello")
def hello_endpoint():
    """ New Workflow Endpoint """
    return 'Hello, World!', 200
