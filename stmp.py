import smtplib
try:
    handle = smtplib.SMTP('smtp.163.com', 25)
    handle.login('zhenni94@163.com','zhenni19940528')
    msg = "To:zhenni94@163.com\r\nFrom:zhenni94@163.com\r\nSubject:The first email~ \r\n\r\nhello ^_^~\r\n"
    handle.sendmail('zhenni94@163.com','zhenni94@163.com', msg)
    handle.close()
except Exception,e:
    print e
