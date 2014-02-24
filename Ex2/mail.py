from socket import *

def client_send(message):
    clientSocket.send(message)

def client_recv(flag):
    recv = clientSocket.recv(1024)
    print recv
    if flag != -1:
        if recv[:3] != str(flag):
            print str(flag) + ' reply not received from server'

def  client_conn(msg,flag):
    client_send(msg)
    client_recv(flag)

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.stud.ntnu.no'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
mailport = 25
clientSocket.connect((mailserver, mailport))

client_recv(220)

# Send HELO command and print server response.
client_conn('HELO Alice\r\n',250)

# Send MAIL FROM command and print server response.
client_conn('MAIL FROM: Kristian\r\n', 250)

# Send RCPT TO command and print server response.
client_conn('RCPT TO: <krinorm@stud.ntnu.no>\r\n', 250)

# Send DATA command and print server response.
client_conn('DATA\r\n', 354)

# Send message data.
client_send('From: "Kristian"\r\n')
client_send('To: "Andreas"\r\n')
client_send('Date: Now\r\n')
client_send('Subject: test\r\n')
client_send('\r\nI love computer networks!\r\n')

# Message ends with a single period.
client_conn('\r\n.\r\n', 250)

# Send QUIT command and get server response.
client_conn('QUIT\r\n', 221)
