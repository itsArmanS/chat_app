import socket
import argparse
import threading

parser = argparse.ArgumentParser(description="C")
parser.add_argument("name", type=str, help="Enter your username")
parser.add_argument("--recepient", type=str, default="bot", help="Enter the user to send messages to")
args = parser.parse_args()

username = args.name
recepient = args.recepient

HOST = '172.20.10.3'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def check_name(sender, receiver):
    client_socket.send(f"{sender}|{receiver}".encode('utf-8'))
    return_message = client_socket.recv(1024).decode("utf-8")

    
    if return_message == "NAME_TAKEN":
        print("Username already in use, please try again.")
    elif return_message == "NOT_FOUND":
        print("Recepient is offline/unavailable")
    elif return_message == "OK":
        print(f"Your username was set to: {sender}")

        while True:
            client_message = input("Enter your message:")
            client_socket.send(f"{client_message}".encode("utf-8"))


check_name(username, recepient)


