#!/usr/bin/python3
# encoding eintragen

import socket

# Achtung: Bei der Verwendung von Link-Local-Adressen muss immer die ID des
#          Netzwerkinterfaces mit angegeben werden!
HOST = 'fe80::9281:e37:5e8c:c826%enp3s0'
PORT = 50007

# Verbindungsdaten ermitteln
info = socket.getaddrinfo(HOST, PORT, socket.AF_INET6, socket.SOCK_STREAM)
(family, socktype, proto, cname, sockaddr) = info[0]

with socket.socket(family, socktype, proto) as s:
    s.connect(sockaddr)
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received: {0}'.format(data))

