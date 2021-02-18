import socket

#CONFIGURATION OF THE SERVERPORT 
serverPort=1234
#CONFIGURATION OF THE SERVERSOCKET 
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#GENERATING THE ARTIFICIAL SERVER 
serverSocket.bind((socket.gethostname(),serverPort))

print("server is ready to receive")

#sending the server into listening mode 
while 1:
    #server is gettinbg the client info
    msgandaddress=serverSocket.recvfrom(1024)
    #server is reading the text 
    a=(msgandaddress[0].decode())
    print(a)
    try:
        #server is opening the file 
        f=open(a,mode='r')
        #server is reading the composition of the file 
        filecomposition=f.read()
        #server is sending the composition to the client 
        serverSocket.sendto(filecomposition.encode(),msgandaddress[1])
    except IOError:
        #raiting the error when the file is not found 
        serverSocket.sendto("404 NOT FOUND".encode(),msgandaddress[1])


    
    