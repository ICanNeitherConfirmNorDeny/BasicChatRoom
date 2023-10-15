import socket
import sys
import time

# creats the sockets and retrives the hosname

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 42069

# binds host and port number

new_socket.bind((host_name, port))
print("Binding successfull...")
print("This is your IP: ", s_ip)

# listens for connections
name = input("Enter a Nickname: ")
new_socket.listen(1)

# accepts incoming connections

conn, add = new_socket.accept()

print("Recieved connection from ", add[0])
print("Connection Established. Connected from:", add[0])

# storing incoming connection data

client = (conn.recv(1024)).decode()
print(client + " had connected.")
conn.send(name.encode())

# delivers messages

while True:
    message = input("Me : ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)

