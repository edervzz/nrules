"""_summary_"""
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return 'Hello, World!'
from application.validators.expression_validator import ExpressionValidator

validator = ExpressionValidator()
validator.validate(
    "asdf >= false AND qwer = \"Vikings\" OR rtyu = 689 AND lkjj = 9898")
