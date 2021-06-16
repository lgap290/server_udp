import logging
import socket
import requests

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

# UDP_IP_ADDRESS = "157.245.249.100"
# UDP_PORT_NO = 6789
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

for data in udp_server(UDP_IP_ADDRESS, UDP_PORT_NO):
    log.debug("Message received: %r" % (data,))
    data_antena = data.split(',')
    response = requests.post("http://localhost:8000/api/consume", data = {
        "id":data_antena[0],
        "date":data_antena[1],
        "consume":data_antena[2],
    })
    log.debug("Message save: %r" % (response,))
    

