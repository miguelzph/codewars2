import os
import mysql.connector

# classe DB baseada no https://stackoverflow.com/questions/55833375/database-connection-function-for-python

class DB(object):
    def __init__(self):
        server_host = os.environ['db_server_host']
        port = os.environ['db_port']
        database = os.environ['db_database']
        user = os.environ['db_user']
        password = os.environ['db_password']
        
        self.conn = mysql.connector.connect(user=user, password=password,
                                              host=server_host,
                                              database=database, port=port)

    def __del__(self):
        self.conn.close()

    def query(self, sql, params=None, commit=False):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            if commit:
                self.conn.commit()
            return {'fetchall': cursor.fetchall(), 'description': cursor.description}