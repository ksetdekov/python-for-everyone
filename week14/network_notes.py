import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create endpoint, not yet connected
mysock.connect(('data.pr4e.org', 80))
