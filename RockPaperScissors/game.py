import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("thedekel.net",1337))
s.setblocking(0)

state = 1
queue = ""
curr_msg = ""
reading = False
		
while 1:
	try:
		temp = s.recv(1)
		if temp == "*":
			reading = True
			queue = ""
		elif temp == "&":
			reading = False
			curr_msg = queue[:]
		elif reading:
			queue += temp
	except:
		pass	
	if state == 0:
		break
	elif state == 1:
		idnum = 0000 # gotten from ui
		try:
			s.send("login," + str(idnum))
		except:
			pass
		


	
s.shutdown(socket.SHUT_RDWR)
s.close()


