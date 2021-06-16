import socket

UDP_IP_ADDRESS = "143.244.169.167"
# UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "C-02-053,2021-06-12,1018".encode()

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))