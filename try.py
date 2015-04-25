from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
IMAP_HOST = ("imap.163.com", 143)
s.connect(IMAP_HOST)
print s.recv(1024)
s.setblocking(1)
s.sendall("yeah login ymf111111@163.com ymf^is^safe\r\n")
print s.recv(1024)
t = raw_input()
s.sendall("yeah1 select inbox\r\n")
print s.recv(1024)
t = raw_input()
s.sendall("yeah3 search ALL\r\n")
print s.recv(1024)
t = raw_input()
s.sendall("yeah4 NOOP\r\n")
print s.recv(1024)
t = raw_input()
s.sendall("yeah5 fetch 1:3 (ENVELOPE BODY[TEXT])\r\n")
while True:
    t = s.recv(4096)
    print t
    if t[-11:] == "completed\r\n": break
print msg
t = raw_input()
s.sendall("yeah6 STATUS inbox (MESSAGES)\r\n")
print s.recv(4096)
