""" Create a new workflow """
from flask import Blueprint


hello_bp = Blueprint("Hello", __name__)


@hello_bp.get("/hello")
def hello_endpoint():
    """ New Workflow Endpoint """
    return 'Hello, World!', 200
