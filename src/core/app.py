"""_summary_"""
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return 'Hello, World!'
from application.extensions.extensions import ExpressionExtensions


ExpressionExtensions.transform_expression(
    "asdf >= false AND qwer = true OR rtyu = 689 AND lkjj = 9898")
