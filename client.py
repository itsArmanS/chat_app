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
        if return_message == "OK":
            print(f"Added user {sender}!")

            while True:
                print("Please enter @user followed by your <message>")
        
                client_message = input("->")
                print(client_message)
                client_socket.send(client_message.encode("utf-8"))

                response = client_socket.recv(1024).decode("utf-8")

                if response == "WRONG":
                    print("Wrong format. Please use @user followed by your message")
                elif response == "OFFLINE":
                    print("User if offline, please try again later.")
                elif response == "SENT":
                    print("Sent!")




check_name(username)


