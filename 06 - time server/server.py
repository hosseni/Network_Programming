from socket import *
from datetime import *

s = socket(AF_INET, SOCK_STREAM)
s.bind((gethostname(), 7000))
s.listen(5)

dateAsString = str(datetime.now())

x=dateAsString.encode()
while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} is established")
    clt.send(x)
