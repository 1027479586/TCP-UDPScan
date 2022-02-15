from scapy.all import *


def main():
    ip = '192.168.1.100'
    port = 80

    packet = IP(dst=ip)/TCP(sport=123,dport=port,flags="S")     #发送SYN包
    resp = sr1(packet,timeout=20)
    if(str(type(resp))=="<type 'NoneType'>"):
        print("port %s is closed"%(port))
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==0x12):     #返回包TCP层是ack标志位
            send = sr(IP(dst=ip)/TCP(sport=123,dport=port,flags="AR"),timeout=20)   #返回ack的确认
            print("port %s is open"%(port))
        elif(resp.getlayer(TCP).flags==0x14):
            print("port %s is down" % (port))

    pass

if __name__ == '__main__':
    main()