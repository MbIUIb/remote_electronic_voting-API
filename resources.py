from flask import request
from flask_restful import Resource

from db import *
from deg_config import iden_num_len


class Voters(Resource):
    def get(self):
        """Get voters information"""

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
    def get(self, voter_id):
        firstname, lastname = get_voter_name_by_id(voter_id)
        return ({'firstname': firstname, 'lastname': lastname}, 200) if firstname and lastname \
            else ({'warning': 'Voter not exist'}, 404)

    def post(self, voter_id):
        pass
