import socket


def main():
    ip = '192.168.1.100'
    port = 3306

    s = socket.socket()
    s.connect((ip,port))
    s.send("hh".encode())
    banner = s.recv(1024)
    s.close()
    print("banner is {}".format(banner))


    pass


if __name__ == '__main__':
    main()