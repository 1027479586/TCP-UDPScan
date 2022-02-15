import time
from scapy.all import *
from random import randint



def main():
    ip = '192.168.1.100'
    dport = randint(1,65535)
    packet = IP(dst=ip)/TCP(dport=dport,flags="A")
    res = sr1(packet,timeout=1,verbose=0)
    if res:
        #RST
        if int(res[TCP].flags)==4:
            time.sleep(0.5)
            print(ip+" is up")
        else:
            print(ip+" is down")


    pass








if __name__ == '__main__':
    main()