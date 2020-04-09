import socket
from datetime import datetime
s=socket.socket()
print("Socket successfully created")
port=9002

s.bind(('0.0.0.0', port))
s.listen(5)
c, addr = s.accept()
print('Got connection from', addr)
c.send(str.encode('Thank you for connecting'))
ts=datetime.now()
while True:
    c, addr = s.accept()
    data=c.recv(16)
    stringdata = data.decode('utf-8')
    if stringdata == "Jump" and (datetime.now()-ts).total_seconds() > 1:
        print("Jumped")
        ts=datetime.now()

    c.close()