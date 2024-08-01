from flask import request
from flask_restful import Resource

from db import *
from deg_config import iden_num_len


class VotersInformation(Resource):
    def get(self):
        """Get voters information
        GET: {"firstname": "Ivan", "lastname":"Ivanov"}
        RESPONSE: {"id": 1, "iden_num_len": 10}
        """

        if request.get_data():
            request_json = request.get_json()
            firstname = request_json.get('firstname')
            lastname = request_json.get('lastname')
            data = get_voter_id_by_name(firstname, lastname)
            data.setdefault("iden_num_len", iden_num_len)
        else:
            data = get_all_voters()

        return (data, 200) if data else ({'warning': 'Voter not exist'}, 404)


class Voter(Resource):
    """test"""
    def get(self, voter_id):
        firstname, lastname = get_voter_name_by_id(voter_id)
        return ({'firstname': firstname, 'lastname': lastname}, 200) if firstname and lastname \
            else ({'warning': 'Voter not exist'}, 404)

    def post(self, voter_id):
        if request.get_data():
            data = request.get_json()
            rec_voter_id = data.get('voter_id')
            masked_iden_num = data.get('masked_iden_num')


class VoterRegistration(Resource):
    def get(self):
        """Checking the voter's existence in database
        GET: {"firstname": "Ivan", "lastname":"Ivanov"}
        RESPONSE: {"exist": true}"""

        if request.get_data():
            request_json = request.get_json()
            firstname = request_json.get('firstname')
            lastname = request_json.get('lastname')

            return {"exist": voter_exists(firstname, lastname)}, 200
        else:
            return {"warning": "bad request"}, 404

    def post(self):
        """Voter registration: adding to database
        POST: {"firstname": "Ivan1", "lastname":"Ivanov1", "pass":"password123"}
        RESPONSE: {"successful": true}"""

        if request.get_data():
            request_json = request.get_json()
            firstname = request_json.get('firstname')
            lastname = request_json.get('lastname')
            password = request_json.get('password')

            voter_registration(firstname, lastname, password)
            return {"successful": "true"}, 200
        else:
            return {"warning": "bad request"}, 404


class VoterAuthentication(Resource):
    def get(self):
        """Checking voter's credentials
        GET {"firstname": "Ivan1", "lastname":"Ivanov1", "pass":"password123"}
        RESPONSE: {"successful": true}"""

        if request.get_data():
            request_json = request.get_json()
            firstname = request_json.get('firstname')
            lastname = request_json.get('lastname')
            password = request_json.get('password')

            return {"successful": voter_authentication(firstname, lastname, password)}, 200
        else:
            return {"warning": "bad request"}, 404
