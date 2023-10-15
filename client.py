import socket
import sys
import time

# creates socket and accept user input and hostname

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 42069

# connects to server
print("This is your IP address: ", ip)
server_host = input("Enter friends IP address: ")
name = input("Enter a Nickname: ")

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
