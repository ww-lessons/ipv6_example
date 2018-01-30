#!/usr/bin/python3
#

import socket

# Quelle: https://docs.python.org/3/library/socket.html#example

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    con, addr = s.accept()
    with con:
        print("Aufgerufen von {0}".format(addr))
        while True:
            data = con.recv(1024)
            if not data: break
            con.sendall(data)
