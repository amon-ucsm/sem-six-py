from socket import *

serverName = 'localhost'
serverPort = 3001

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(str.encode(message), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(bytes.decode(modifiedMessage))
clientSocket.close()