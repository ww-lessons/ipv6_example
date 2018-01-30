#!/usr/bin/python3
#

import socket

# Quelle: https://docs.python.org/3/library/socket.html#example

# Achtung: Bei der Verwendung von Link-Local-Adressen muss immer die ID des
#          Netzwerkinterfaces mit angegeben werden!
HOST = 'fe80::9281:e37:5e8c:c826%enp3s0'
PORT = 50007

# Verbindungsdaten ermitteln
info = socket.getaddrinfo(HOST, PORT, socket.AF_INET6, socket.SOCK_STREAM)
(family, socktype, proto, cname, sockaddr) = info[0]

# Server-Port binden und warten bis Daten eintreffen
with socket.socket(family, socktype, proto) as s:
    s.bind(sockaddr)
    s.listen(1)
    con, addr = s.accept()
    with con:
        print("Aufgerufen von {0}".format(addr))
        while True:
            data = con.recv(1024)
            if not data: break
            con.sendall(data)
