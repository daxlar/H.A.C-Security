import socket
import time
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
#UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock

#serverSock.bind(("", UDP_PORT_NO))

print("im about to start the infinite loop")
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
print(hostIP)
serverSock.bind((hostIP, UDP_PORT_NO))
while True:
    data, addr = serverSock.recvfrom(2048)
    current_value = int.from_bytes(data, byteorder='big')

    print(current_value)
