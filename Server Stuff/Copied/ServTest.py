import socket
import pickle
import Adafruit_PCA9685

s = socket.socket()
#host = socket.gethostname()
#print("Hostname: " + str(host))
port = 12345
print("Port: " + str(port))
s.bind(('', port))
pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)
s.listen(5)
defpos = 0
preval = 0
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    while True:
	val = pickle.loads(c.recv(1024))
	if(defpos == 0):
	    defpos = val[0]
	print(val)
	servoinp1 = (defpos - val[0]) * 3
	print(servoinp1)
	print(preval)
	print("+=-=-=-=-=-=-=-=-=+")
	if(servoinp1 != preval):
	    pwm.set_pwm(14, 0, servoinp1)

	preval = servoinp1
	#c.send('Thank you for connecting')
c.close()                # Close the connection
