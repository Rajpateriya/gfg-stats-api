from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS  # Import CORS from flask_cors
from modules.scrap import scrap

app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for your Flask app

class geeksforgeeksAPI(Resource):
    def get(self, username):
        scrapper = scrap(username)
        return scrapper.fetchResponse()

api.add_resource(geeksforgeeksAPI, "/<string:username>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
