import pyaudio
import socket
import sys
from datetime import datetime
import time
from threading import Thread

host = '127.0.0.1'
port = 1337

def sendTime():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    while True:
        now = datetime.now()
        sA = (now.minute * 60) + now.second + now.microsecond / 1000000
        udp.sendto(str(sA).encode(), (host, port))
        time.sleep(0.01)
    udp.close()

def recvTime():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("127.0.0.1", 1337))
    while True:
        sA, _ = udp.recvfrom(512)
        Ts = Thread(target = calcDiff, args=(sA,))
        Ts.setDaemon(True)
        Ts.start()
        

def calcDiff(sA):
    sA = sA.decode()
    now = datetime.now()
    sB = (now.minute * 60) + now.second + now.microsecond / 1000000
    dt = float(sB) - float(sA)
    print('DT: %s' % str(dt))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify either server or client')
        sys.exit(0)
    print(sys.argv[1])
    if sys.argv[1] == 'INPUT':
        sendTime()
    else:
        recvTime()