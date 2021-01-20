# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:43:33 2018

@author: Gerard
"""

import socket

s = socket.socket()
#host = socket.gethostname()
#print("Hostname: " + str(host))
port = 12345
print("Port: " + str(port))
s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    #c.close()                # Close the connection