from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP
import base64

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
MAIL_SERVER = "163.com"
SMTP_HOST = ("smtp."+MAIL_SERVER, 25)
USER_NAME = "zhenni94"
PASS_WORD = "zhenni19940528"
USER_NAME_BASE64 = base64.encodestring(USER_NAME)
PASS_WORD_BASE64 = base64.encodestring(PASS_WORD)
SENDER = USER_NAME+"@"+MAIL_SERVER
RECEIVER = "zhenni94@163.com"
SUBJECT = "Test message"
MAIL_TEXT = "First message."

print USER_NAME
print PASS_WORD

s.connect(SMTP_HOST)
print s.recv(1024)
#s.setblocking(1)
s.settimeout(2)
s.sendall("HELO smtp."+MAIL_SERVER+"\r\n")
print s.recv(1024)

s.sendall("AUTH LOGIN\r\n")
print s.recv(1024)

s.sendall(USER_NAME_BASE64)
print s.recv(1024)
s.sendall(PASS_WORD_BASE64)
print s.recv(1024)

s.sendall("MAIL from: <"+SENDER+">"+"\r\n")
print s.recv(1024)

s.sendall("RCPT to: <"+RECEIVER+">\r\n")
print s.recv(1024)

s.sendall("DATA\r\n")
print s.recv(1024)

s.sendall("From: "+SENDER+"\r\n")
s.sendall("To: "+RECEIVER+"\r\n")
s.sendall("Subject: "+SUBJECT+"\r\n")
s.sendall("\r\n")
s.sendall(MAIL_TEXT+"\r\n")
s.sendall(".\r\n")
print s.recv(1024)

s.sendall("QUIT\r\n")
print s.recv(1024)


