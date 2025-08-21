import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000
    # get instance of server socket
    server_socket = socket.socket(socket.ASF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((" ", port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address)) 
    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            
            break
        print("User " + str(address) + "says " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()

server_program()