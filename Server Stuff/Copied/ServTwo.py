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

defpos = [0, 0, 0]
preval = [0, 0, 0]
def servomove(motor, servinput):
    val = pickle.loads(c.recv(1024))
    if(defpos[servinput] == 0):
        defpos[servinput] = val[servinput]
    servoinps = (defpos[servinput] - val[servinput]) * 13
    print(val)
    print(servoinps)
    print(preval[servinput])
    print("+=-=-=-=-=-=-=-=-=+")
    if(servoinps != preval[servinput]):
        pwm.set_pwm(motor, 0, servoinps)
        preval[servinput] = servoinps
    return

pwm.set_pwm_freq(60)
s.listen(5)
defpos1 = 0
preval1 = 0
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    while True:
        servomove(14, 0)  
        servomove(15, 1)
	#c.send('Thank you for connecting')
c.close()                # Close the connection
