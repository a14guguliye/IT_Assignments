import socket 
#configuring the server port 
serverPort=1234
#configuring the socket to UDP 
clientsocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sending the file name to the server 
message="qulu.txt"
clientsocket.sendto(message.encode(), (socket.gethostname(), 1234))

#getting the file composition from the server 
messageandserveraddress=clientsocket.recvfrom(2048)
#decoding it 
print(messageandserveraddress[0].decode())
#closing everything 
clientsocket.close()