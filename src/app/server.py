from dotenv import load_dotenv
from os.path import join, dirname
import os
import socket
import sys
import psycopg2


def create_conn():
    # # Create .env file path.
    dotenv_path = join(dirname(__file__), '.env')

    # Load file from the path.
    load_dotenv(dotenv_path)

    host=os.getenv("HOST")
    db_name=os.getenv("DATABASE")
    db_user=os.getenv("DATABASE_USER")
    db_password=os.getenv("DATABASE_PASSWORD")

    conn_string = "host={} dbname={} user={} password={}".format(host,db_name,db_user,db_password)
    return psycopg2.connect(conn_string)

def get_data():
    conn = create_conn()
    cur = conn.cursor()
    cur.execute("select * from greeting limit 1;")
    message = cur.fetchone()[0]

    conn.close()
    return message


HOST, PORT = '', 80

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

{}
""".format(get_data())
    client_connection.sendall(http_response)
    client_connection.close()