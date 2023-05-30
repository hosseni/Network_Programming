from socket import *
s = socket(AF_INET, SOCK_STREAM)
#  7000 is for port number
s.connect((gethostname(), 7000))
#  1024 is for byte
message = s.recv(1024)
print(message.decode("utf-8"))