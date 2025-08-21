import socket
def client_program():
    host = '172.100.1.232'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    try:
        input()
    except NameError:
        pass
    message = input(" -> ")
    
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        
        print('Received from server: ' + data)
        
        message = input(" -> ")
    client_socket.close()
    
client_program() 