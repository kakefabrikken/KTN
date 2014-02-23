#import socket module 
from socket import *
try:
    serverSocket = socket(AF_INET, SOCK_STREAM)
except socket,error:
    print 'Failed to create socket'
    sys.exit()
print 'socket created'

host = serverSocket.gethostname()
port = 80 # possibly uneccessary
serverSocket.bind( host, port )

serverSocket.listen(5) # argument is backlog, 0-5, specifying max number of queued connections

#Prepare a server socket

while True: 
    #Establish the connection 
    print 'Ready to serve...'
    connectionSocket, addr = #Fill in start #Fill in end 
    try: 
        message = "GET / HTTP / 1.1 " # possibly a little more here 
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = #Fill in start #Fill in end 
        #Send one HTTP header line into socket 
        #Fill in start 
        #Fill in end 
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found
        #print '404 Not Found'
        #Fill in start 
        #Fill in end 
        #Close client socket 
        #Fill in start 
        #Fill in end
        print 'Gah'
serverSocket.close() 
