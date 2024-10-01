from flask import Flask
from flask_restful import Api

from resources import VotersInformation, VoterRegistration, VoterAuthentication, M1

app = Flask(__name__)
api = Api(app)

api.add_resource(VotersInformation, '/api/voters/info')
api.add_resource(VoterRegistration, '/api/voters/registration')
api.add_resource(VoterAuthentication, '/api/voters/authentication')
api.add_resource(M1, '/api/votes/M1')

if __name__ == '__main__':
    app.run(debug=True)
