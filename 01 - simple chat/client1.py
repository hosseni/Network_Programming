from socket import *
try :
    #AF_INET : IPv4,  SOCK_STREAM : TCP
    s = socket (AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.connect ((host, port))
    while True:
        send_data = input ("client : ")
        s.send (send_data.encode('utf-8'))
        recv_data = s.recv(2048)
        print("Server : ", recv_data.decode ('utf-8'))
    s.close()


except KeyboardInterrupt :
    print("chat is terminated")