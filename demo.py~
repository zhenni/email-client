#!/usr/bin/python

import Tkinter
from Tkinter import *
from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP
import base64
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#GUI
root = Tkinter.Tk()
root.title("Mail Client Demo")
scnWidth,scnHeight = root.maxsize()
root.update()
curWidth = 800
curHeight = 600
FONT = 'Helvetica'
pos = '%dx%d+%d+%d'%(curWidth, curHeight, (scnWidth-curWidth)/2, (scnHeight-curHeight)/2)
root.geometry(pos)
Tkinter.Label(root, text='Mail Client Demo',font=FONT+' -30 bold').grid(row=0, sticky='w')

#Frame
frame_sel = Frame(root, width=400)
frame_send = Frame(root)
frame_recv = Frame(root)
frame_sel.grid(row=1, sticky='w')


def get_frame_recv():
	frame_recv.grid(row=2)
	frame_send.grid_forget()
	return

def get_frame_send():
	frame_send.grid(row=2)
	frame_recv.grid_forget()
	return

#select send or recieve
Button(frame_sel, text="recieve", command = get_frame_recv).grid(row=0, column=0)
Button(frame_sel, text="send", command = get_frame_send).grid(row=0, column=1)

#send frame
Label(frame_send, text='Sender Email: ').grid(row=0, column=0, sticky='w')
Label(frame_send, text='@').grid(row=0, column=2, sticky='w')
Label(frame_send, text='Sender Password: ').grid(row=1, column=0, sticky='w')
Label(frame_send, text='Receiver Email: ').grid(row=2, column=0, sticky='w')
Label(frame_send, text='Subject: ').grid(row=3, column=0, sticky='w')
Label(frame_send, text='Mail text: ').grid(row=4, column=0, sticky='nw')

sender_username = StringVar()
sender_email_server = StringVar()
entry_sender_username = Entry(frame_send, width=12, textvariable = sender_username)
entry_sender_email_server = Entry(frame_send, width=12, textvariable = sender_email_server)

entry_sender_username.grid(row=0, column=1, sticky='w')
entry_sender_email_server.grid(row=0, column=3, sticky='w')

sender_password = StringVar()
entry_sender_password = Entry(frame_send, width=27, textvariable = sender_password)
entry_sender_password.grid(row=1, column=1, columnspan=3, sticky='w')
entry_sender_password["show"] = "*"

reciever_email = StringVar()
entry_receiver_email = Entry(frame_send, width=27, textvariable = reciever_email)
entry_receiver_email.grid(row=2, column=1, columnspan=3, sticky='w')

subject = StringVar()
entry_subject = Entry(frame_send, width=27, textvariable = subject)
entry_subject.grid(row=3, column=1, columnspan=3, sticky='w')

entry_mail_text = Text(frame_send, width=31)
entry_mail_text.grid(row=4, column=1, columnspan=3, rowspan=2, sticky='w')


########################################## SEND via SMTP ################################################3
def send():
	MAIL_SERVER = sender_email_server.get()
	SMTP_HOST = ("smtp."+MAIL_SERVER, 25)
	USER_NAME = sender_username.get()
	PASS_WORD = sender_password.get()
	USER_NAME_BASE64 = base64.encodestring(USER_NAME)
	PASS_WORD_BASE64 = base64.encodestring(PASS_WORD)
	SENDER = USER_NAME+"@"+MAIL_SERVER
	RECEIVER = reciever_email.get()
	SUBJECT = subject.get()
	MAIL_TEXT = entry_mail_text.get("1.0", END)
	
	s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
	s.connect(SMTP_HOST)
	print s.recv(1024)
	s.setblocking(1)
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
	s.close()
	return
####################################################################################################

Button(frame_send, text="Submit", command = send).grid(row=6, column=0, columnspan=4)


#recieve frame
frame_recv_user = Frame(frame_recv)
frame_recv_user.grid(row=0, column=1, columnspan=3, sticky='w') 
Label(frame_recv, text='Email: ').grid(row=0, column=0, sticky='w')
Label(frame_recv_user, text='@').grid(row=0, column=2, sticky='w')
Label(frame_recv, text='Password: ').grid(row=1, column=0, sticky='w')

username = StringVar()
email_server = StringVar()
entry_username = Entry(frame_recv_user, width=12, textvariable = username)
entry_email_server = Entry(frame_recv_user, width=12, textvariable = email_server)

entry_username.grid(row=0, column=1, sticky='w')
entry_email_server.grid(row=0, column=3, sticky='w')

password = StringVar()
entry_password = Entry(frame_recv, width=27, textvariable = password)
entry_password.grid(row=1, column=1, columnspan=3, sticky='w')
entry_password["show"] = "*"

mail_num_range = StringVar()
label_mail_num_range=Label(frame_recv, textvariable=mail_num_range)
label_mail_num_range.grid(row=3, column=0, columnspan=4, sticky='w')
label_mail_num_range.grid_forget()

entry_mail_text = Text(frame_recv, width=100)

##parser and printer

def print_info(msg, indent=0):
    ans = ''

    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>\n' % (name, addr)
            ans +='%s%s: %s' % ('  ' * indent, header, value)
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            ans+='\n%spart %s' % ('  ' * indent, n)
            ans+='%s--------------------' % ('  ' * indent)
            ans+=print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            ans+='\n%sText: %s\n' % ('  ' * indent, content)
        else:
            ans+='\n%sAttachment: %s' % ('  ' * indent, content_type)
    return ans

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


################################# RECEIVE via POP3 #############################################

def recieve():
	s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
	label_mail_num_range.grid(row=3, column=0, columnspan=5, sticky='w')

	MAIL_SERVER = email_server.get()
	POP3_HOST = ("pop."+MAIL_SERVER, 110)
	USER_NAME = username.get()
	PASS_WORD = password.get()

	s.connect(POP3_HOST)
	print s.recv(1024)
	s.setblocking(1)
	s.sendall("USER "+USER_NAME+"\r\n")
	print s.recv(1024)
	s.sendall("PASS "+PASS_WORD+"\r\n")
	login_recv = s.recv(1024)
	print login_recv
	num = re.findall(r'(\w*[0-9]+)\w*',login_recv)
	mail_num = int(num[0])
	mail_num_range.set("There are "+str(mail_num)+" emails.")
	
	retr_index = str(mail_num)
	print retr_index
	s.sendall("RETR "+retr_index+"\r\n")
	msg = ""
	while True:
		t= s.recv(1024)
		msg += t
		if t[-3:] == ".\r\n": break
	msg_to_parse = msg[msg.find("\n")+1:-3]
	msg_final = Parser().parsestr(msg_to_parse)
	mail_msg = print_info(msg_final)

	

	entry_mail_text.grid(row=4, column=1, columnspan=3, rowspan=2, sticky='w')
	entry_mail_text.insert(1.0, mail_msg)
	
	

	return
################################################################################################

Button(frame_recv, text="Submit", command = recieve).grid(row=2, column=0, columnspan=4)


#GUI
root.mainloop()

