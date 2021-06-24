import socket
import time
from Config_Parser_Connect import targetimage






def tcpinout(json):

    sock = socket.socket()
    sock.settimeout(5)
    sock.connect(targetimage)
    # оправляем пакет
    sock.sendall(json)
    # получаем пакет
    sock.shutdown(socket.SHUT_WR)
    # немного ждем перед чтением всех данных. по возможности сделать умнее
    time.sleep(1)
    data = sock.recv(100000)
    if not data:
        # избегаем RST.
        # https://stackoverflow.com/questions/42611333/why-is-there-tcp-rst-packet-after-sending-a-string-and-closing-a-socket
        sock.close()
    return data
