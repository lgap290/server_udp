import logging
import socket

log = logging.getLogger('udp_server')


def udp_server(host='127.0.0.1', port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    log.info("Listening on udp %s:%s" % (host, port))
    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        yield data


FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

for data in udp_server(UDP_IP_ADDRESS, UDP_PORT_NO):
    log.debug("%r" % (data,))

