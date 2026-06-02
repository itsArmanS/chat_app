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
    name_check = user_socket.recv(1024).decode("utf-8")
   
    if name_check in users:
        user_socket.send("TAKEN".encode("utf-8"))
    else:
        users[name_check] = user_socket
        user_socket.send("OK".encode("utf-8"))
        
        while True:
            incoming_message = user_socket.recv(1024).decode("utf-8")

            if incoming_message.startswith("@"):

                message_parts = incoming_message.split("", 1)
                user_check = message_parts.lstrip("@")
                message_body = message_parts[1] 

                if user_check in users:
                    users[user_check].send(f"{name_check} says: {message_body}".encode("utf-8"))
                    user_socket.send("SENT".encode("utf-8"))
                else:
                    user_socket.send("OFFLINE".encode("utf-8"))
            else:
                user_socket.send("WRONG".encode("utf-8"))
    

while True:
    return_socket, return_address = SERVER.accept() 
    print(f'Connected to {return_address}')
    t1 = threading.Thread(target=messaging_flow, daemon=True, args=(return_socket,))

    t1.start()    