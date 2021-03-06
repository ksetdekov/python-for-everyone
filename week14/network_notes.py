import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create endpoint, not yet connected
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # to bytes
mysock.send(cmd)

while True:
    data = mysock.recv(5000)
    if len(data) < 1:
        break
    print(data.decode())  # gets if ASCI of UTF-8 automatically - to Unicode
mysock.close()
