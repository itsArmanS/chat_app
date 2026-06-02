import socket
import threading

# host = socket.gethostbyname(socket.gethostname())
#sets the IPv4 address automatically, dynamically

HOST = '172.20.10.3'
PORT = 8888

users = {
}


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AFF_INET is basically IPv4, socket.SOCK_STREAM sets it to look for TCP type connection

SERVER.bind((HOST, PORT))
# binds server, based on set host and port variables

SERVER.listen()

def messaging_flow(user_socket):
    data_check = user_socket.recv(1024).decode("utf-8")
    data_check = data_check.split("|")

    sender = data_check [0]
    receiver = data_check[1]

    if sender in users:
        user_socket.send("NAME_TAKEN".encode("utf-8"))
    elif receiver not in users:
        user_socket.send("NOT_FOUND".encode("utf-8"))
    elif receiver in users:
        user_socket.send("OK".encode("utf-8"))

        users[sender] = user_socket

        while True:
            return_message = user_socket.recv(1024).decode("utf-8")
            users[receiver].send(f"{sender}: {return_message}".encode("utf-8"))
                # user_socket.send(f"Your message was received!".encode("utf-8")) #encode before sending message to client
                # return_socket.close() #ends connectiona
    

while True:
    return_socket, return_address = SERVER.accept() 
    print(f'Connected to {return_address}')
    t1 = threading.Thread(target=messaging_flow, daemon=True, args=(return_socket,))

    t1.start()    