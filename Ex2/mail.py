from socket import *

client_msgs = []
msg_index = 0
def client_send_and_recv(index):
    clientSocket.send(client_msgs[index])
    recv = clientSocket.recv(1024)
    print recv
    if recv[:3] != '250':
        print '250 reply not received from server'

def client_msgs_handler(msg):
    client_msgs.append(msg)
    client_send_and_recv(msg_index)
    msg_index += 1

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost' # possibly something like smtp.stud.ntnu.no
clientSocket = socket(AF_INET, SOCK_STREAM)
# Create socket called clientSocket and establish a TCP connection with mailserver
mailport = 25 # 25 may be server side, so this could be wrong
clientSocket.connect((mailserver, mailport))

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
#heloCommand = 'HELO Alice\r\n'

client_msg_handler('HELO Alice\r\n')

#client_msgs.append(heloCommand)
#client_send_and_recv(msg_index)
#msg_index += 1


#clientSocket.send(heloCommand)
#recv1 = clientSocket.recv(1024)
#print recv1
#if recv1[:3] != '250':
#	print '250 reply not received from server.'

client_msg_handler("MAIL FROM: <krinorm@stud.ntnu.no>\r\n")
#from_mail = "MAIL FROM: <krinorm@stud.ntnu.no>\r\n"

#clientSocket.send(from_mail)




# Send MAIL FROM command and print server response.
# Fill in start

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

# Fill in end

# Send DATA command and print server response.
# Fill in start

# Fill in end

# Send message data.
# Fill in start

# Fill in end
# Message ends with a single period.
# Fill in start

# Fill in end

# Send QUIT command and get server response.
# Fill in start

# Fill in end
