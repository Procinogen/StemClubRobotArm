import socket
import pickle

s = socket.socket()
port = 12345
print("Port: " + str(port))

s.connect(("192.168.1.188", port))
val = ["foo", 20, True]
data = pickle.dumps(val)
s.send(data)
print s.recv(1024)
s.close
