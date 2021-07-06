import socket
hostname = socket.gethostname()
ddr = socket.gethostbyname(hostname)
print("My IP Address is : " + ddr)
