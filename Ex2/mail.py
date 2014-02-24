from socket import *

client_msgs = []
msg_index = 0
def client_send(index):
    clientSocket.send(client_msgs[index])
def client_recv(flag):
    recv = clientSocket.recv(1024)
    print recv
    if flag:
        if recv[:3] != '250':
            print '250 reply not received from server'

def client_send_and_recv(index, flag):
    client_send(index)
    client_recv(flag)

def client_msgs_handler(msg, flag):
    client_msgs.append(msg)
    client_send_and_recv(msg_index)
    msg_index += 1



# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost' # possibly something like smtp.stud.ntnu.no

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
mailport = 25 # 25 may be server side, so this could be wrong
clientSocket.connect((mailserver, mailport))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
#heloCommand = 'HELO Alice\r\n'
client_msg_handler('HELO Alice\r\n',1)

#client_msgs.append(heloCommand)
#client_send_and_recv(msg_index)
#msg_index += 1


#clientSocket.send(heloCommand)
#recv1 = clientSocket.recv(1024)
#print recv1
#if recv1[:3] != '250':
#	print '250 reply not received from server.'


# Send MAIL FROM command and print server response.
client_msg_handler("MAIL FROM: <krinorm@stud.ntnu.no>\r\n",1)


# Send RCPT TO command and print server response.
client_msg_handler("RCPT TO <krinorm@stud.ntnu.no>\r\n",1)


# Send DATA command and print server response.
client_msg_handler("DATA",0)

# Send message data.
client_msg_handler('\r\n I love computer networks!',0)

# Message ends with a single period.
client_msg_handler('\r\n.\r\n',0)

# Send QUIT command and get server response.
client_msg_handler("QUIT",0)
