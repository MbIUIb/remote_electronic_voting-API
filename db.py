import psycopg2
from psycopg2 import Error


def execute_select_request(request: str, values: tuple = ()) -> list:
    """Template for SELECT statement"""

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Qq123456",
                                      host="192.168.0.13",
                                      port="5432",
                                      database="deg_system")

        cursor = connection.cursor()
        cursor.execute(request, values)
        return cursor.fetchall()

    except (Exception, Error) as error:
        print('Error while connecting to PostgreSQL', error)

    finally:
        if connection is not None:
            cursor.close()
            connection.close()


def get_all_voters():
    """Get all voters"""

    request = "SELECT id, firstname, lastname FROM voters"
    data = {}
    for voter in execute_select_request(request):
        data.setdefault(voter[0], {'firstname': voter[1], 'lastname': voter[2]})
    return data


def get_voter_name_by_id(voter_id: int):
    """Get voter name by id from database"""

    request = "SELECT firstname, lastname FROM voters WHERE id=%s"
    data = execute_select_request(request, (voter_id,))
    return (data[0][0], data[0][1]) if data else (None, None)


def get_voter_id_by_name(firstname: str, lastname: str):
    """Get voter id by name from database"""

    request = "SELECT id FROM voters WHERE firstname=%s AND lastname=%s;"
    data = {}
    data.setdefault("id", execute_select_request(request, (firstname, lastname))[0][0])
    return data if data else None
