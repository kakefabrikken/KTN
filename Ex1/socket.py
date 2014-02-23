from socket import *
try:
    serverSocket = socket(AF_INET, SOCK_STREAM) # TCP
except socket.error:
    print ("Failed to create socket")
    sys.exit()
print ('socket created')

host = gethostbyname(gethostname())
port = 80 # possibly uneccessary
serverSocket.bind( (host, port) )

serverSocket.listen(1) # argument is backlog, 0-5, specifying max number of queued connections

while True: 
    #Establish the connection 
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print ('Got connection from ', addr)
    try:
        # receive data
        incoming_message = serverSocket.recv(1024) # possibly a little more here 

        # process data
        filename = incoming_message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read() 
        #Send one HTTP header line into socket

        awesome_msg = ''
        connectionSocket(awesome_msg)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found
        failuremsg = ''
        connectionSocket.send(failuremsg)
        connectionSocket.close()

serverSocket.close() 
