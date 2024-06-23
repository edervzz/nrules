""" entry point """
from flask import Flask
from webapi.endpoints.create_rule import new_rule


app = Flask(__name__)

app.register_blueprint(new_rule)


@app.route('/hello')
def hello():
    """ health check """
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()


# from application.validators.expression_validator import ExpressionValidator

# validator = ExpressionValidator()
# validator.validate(
#     "asdf >= false AND qwer = \"Vikings\" OR rtyu = 689 AND lkjj = 9898")
