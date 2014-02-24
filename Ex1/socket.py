from socket import *
try:
    serverSocket = socket(AF_INET, SOCK_STREAM) # TCP
except socket.error:
    print ("Failed to create socket")
    sys.exit()
print ('socket created')

host = 'localhost' # maybe gethostbyname(gethostname())
port = 80 # possibly uneccessary
serverSocket.bind( (host, 80) )

serverSocket.listen(1) # argument is backlog, 0-5, specifying max number of queued connections

awesome_msg = ("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n")
failuremsg = ("HTTP/1.0 404 Not Found\r\nContent-Type: text/plain\r\n\r\n 404 File Not Found")

while True: 
    #Establish the connection 
    print ('Ready to serve...')
    conn, addr = serverSocket.accept()
    print ('Got connection from ', addr)
    try:
        # receive data
        incoming_message = conn.recv(1024) # possibly a little more here 

        # process data
        filename = incoming_message.split()[1]
        print (filename)
        f = open(filename[1:])
        outputdata = f.read() 

        #Send one HTTP header line into socket
        conn.send(awesome_msg)

        #send data
        for i in range(0, len(outputdata)):
            conn.send(outputdata[i]) 
        conn.close() 
    except IOError: 
        #Send response message for file not found
        conn.send(failuremsg)
        conn.close()

serverSocket.close() 
