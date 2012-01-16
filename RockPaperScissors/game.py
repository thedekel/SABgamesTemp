import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("thedekel.net",1337))
s.setblocking(0)

state = 1
queue = ""
curr_msg = ""
reading = False
		
s.send("ping")

while 1:
	try:
		temp = s.recv(1)
		if temp == "*":
			reading = True
			queue = ""
		elif temp == "&":
			reading = False
			curr_msg = queue[:]
			print curr_msg	
		elif reading:
			queue += temp
	except:
		pass	
	if state == "0":
		break
	state = raw_input("Yes? ")

	
s.shutdown(socket.SHUT_RDWR)
s.close()


