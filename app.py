from flask import Flask
from flask_restful import Api

from resources import Voters, Voter

app = Flask(__name__)
api = Api(app)

api.add_resource(Voters, '/api/voters')
api.add_resource(Voter, '/api/voters/<int:voter_id>')

if __name__ == '__main__':
    app.run(debug=True)
