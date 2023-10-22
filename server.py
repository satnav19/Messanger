import socket
import sys 

def main(argv) :
    file  =" <!DOCTYPE html><html><head><title>Network Security</title></head><body><h1>I cook-a the pizza</h1><p>This is a spicy web-a page.</p></body></html>"
    port = argv[1]
    message = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" 
    message += file
    hostName = 'localhost'
    servSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    servSock.bind((hostName,int(port)))
    servSock.listen(1)
    client,clientAddr = servSock.accept()
    client.recv(0)
    client.sendall(bytes(message,'utf-8'))
    client.close()
if __name__ == "__main__" :
    main(sys.argv)
