from scapy.all import *




def main():
    ip='192.168.1.100'
    req,res = sr(IP(dst=ip)/UDP(dport=80))
    for req1,res1 in req:
            print(res1.sprintf("%IP.src% is up"))


    pass



if __name__ == '__main__':
    main()