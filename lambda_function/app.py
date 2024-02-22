from flask import Flask
from flask_restx import Api

from main import api as calculate_data

application = Flask(__name__)
api = Api(application)


# api.add_namespace(user_namespace, path="/")
api.add_namespace(calculate_data, path="/calculate_data")
# api.add_namespace(tag_namespace, path="/tag")


if __name__ == "__main__":
    application.run(debug=True, port=8080)
