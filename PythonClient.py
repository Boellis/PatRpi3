import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''#socket.gethostname()
port = 20601
s.connect((host,port))
#r  = "stocks,tesla"
r = "stocks, tesla"
s.send(r.encode())

data = ''
data = s.recv(1024).decode()
print(data)
s.close()
print("Ran")
