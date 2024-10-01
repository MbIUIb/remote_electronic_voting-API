from flask import request
from flask_restful import Resource

from db import *
from deg_config import iden_num_len


class VotersInformation(Resource):
    @staticmethod
    def get():
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


class VoterRegistration(Resource):
    @staticmethod
    def get():
        """Checking the voter's existence in database
        GET: {"firstname": "Ivan", "lastname":"Ivanov"}
        RESPONSE: {"exist": true}"""

        if request.get_data():
            request_json = request.get_json()
            firstname = request_json.get('firstname')
            lastname = request_json.get('lastname')

            return {"exists": voter_exists(firstname, lastname)}, 200
        else:
            return {"warning": "bad request"}, 404

    @staticmethod
    def post():
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
    @staticmethod
    def get():
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


class M1(Resource):
    def get(self):
        if request.get_data():
            request_json = request.get_json()
            n_id = request_json.get('n_id')

            return {"M_1": get_m1_by_n_id(n_id)}, 200
        else:
            return {"successful": "false"}, 404

    def post(self):
        if request.get_data():
            request_json = request.get_json()
            encrypted_iden_num = request_json.get('encrypted_iden_num')
            n_id = request_json.get('n_id')
            external_n_id = request_json.get('external_n_id')

            insert_m1(encrypted_iden_num, n_id, external_n_id)
            return {"successful": "true"}, 200
        else:
            return {"successful": "false"}, 404
