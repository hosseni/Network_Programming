from socket import *
try :
    s = socket (AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.bind ((host, port))
    s.listen (5)
    print ("Waiting for connection")
    client, add = s.accept()
    print("connection from : ", client )
    while True:
        recv_data = client.recv (2048)
        print("Client : ", recv_data.decode ('utf-8'))
        sent_data = input ("Server : ")
        client.send (sent_data.encode('utf-8'))
    s.close    
except KeyboardInterrupt :
    print ("chat terminatted ...")