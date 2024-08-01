from flask import Flask
from flask_restful import Api

from resources import VotersInformation, Voter, VoterRegistration, VoterAuthentication

app = Flask(__name__)
api = Api(app)

api.add_resource(VotersInformation, '/api/voters/info')
api.add_resource(Voter, '/api/voters/<int:voter_id>/masked-iden-num')
api.add_resource(VoterRegistration, '/api/voters/registration')
api.add_resource(VoterAuthentication, '/api/voters/authetication')

if __name__ == '__main__':
    app.run(debug=True)
