import socket
import argparse
import threading

parser = argparse.ArgumentParser(description="C")
parser.add_argument("name", type=str, help="Enter your username")
args = parser.parse_args()

username = args.name

HOST = '172.20.10.3'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def check_name(sender):
    client_socket.send(sender.encode('utf-8'))
    return_message = client_socket.recv(1024).decode("utf-8")

    
    if return_message == "TAKEN":
        print("Username already in use, please try again.")
    else:
        print(f"Added user {sender}!")
        return True

def listen():
   while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        if data == "SENT":
            print("Sent!")
        elif data == "WRONG":
            print("Wrong format: Please enter @<user> followed by your <message>")
        elif data == "OFFLINE":
            print("User is offline. Try again later")
        else:
            print(data)

if not check_name(username):
    exit()

t1 = threading.Thread(target=listen, daemon=True)
t1.start()    

while True:
    client_message = input("->")
    client_socket.send(client_message.encode("utf-8"))