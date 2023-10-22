import socket
import sys
def main(argv):
    hostname,port = argv[1],argv[2]
    mysoc = socket.create_connection((hostname,port))
    request = "GET / HTTP/1.1\r\nHost:" + hostname + "\r\n\r\n"
    mysoc.send(bytes(request,'utf-8'))
    print((mysoc.recv(1024)).decode())
    mysoc.close()
    

if __name__ == "__main__":
    main(sys.argv)
