from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP
import re

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)

MAIL_SERVER = "163.com"
POP3_HOST = ("pop."+MAIL_SERVER, 110)
USER_NAME = "zhenni94"
PASS_WORD = "zhenni19940528"

s.connect(POP3_HOST)
print s.recv(1024)
s.setblocking(1)
s.sendall("USER "+USER_NAME+"\r\n")
print s.recv(1024)
s.sendall("PASS "+PASS_WORD+"\r\n")
login_recv = s.recv(1024)
print login_recv
#if login_recv[0:3] == "+OK": print "OK"
num = re.findall(r'(\w*[0-9]+)\w*',login_recv)
mail_num = int(num[0])

retr_index = str(mail_num)
print retr_index
s.sendall("RETR "+retr_index+"\r\n")
msg = ""
while True:
	t= s.recv(1024)
	msg += t
	if t[-3:] == ".\r\n": break

print msg





#s.sendall("LIST\r\n")
#while True:
#	t = s.recv(1024)
#	print t
#	if t[-3:] == ".\r\n": break
s.sendall("QUIT\r\n")
print s.recv(1024)
s.close()


