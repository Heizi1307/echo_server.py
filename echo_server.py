#! /usr/bin/python3
'''File Name: echo_server.py
   Author: Longxin Li
   Purpose: This program will accept only one argument,
            which is the port, an integer. Program will
            create a server that can handle many clients
            at the same time. And server will send back
            what client's send.
   CS346'''
from _thread import *
from socket import *


def work(conn):
    while True:
        data = conn.recv(1024).decode()
        while data != "":
            conn.sendall(data.encode())
            data = conn.recv(1024).decode()
        conn.close()


def main(port):
    sock = socket()
    addr = ("0.0.0.0", port)
    sock.bind(addr)
    sock.listen(5)
    while True:
        (conn, conn_addr) = sock.accept()
        start_new_thread(work, (conn,))


if __name__ == "__main__":
    port = 1234
    main(port)
