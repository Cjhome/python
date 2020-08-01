import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))
server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()
    # print(x)
    data = client_socket.recv(1025).decode('utf8')

    # 响应头+内容 返回内容之前，需要先设置响应头
    # 设置一个响应头就换一行
    # 所有的响应头设置完成以后，再换行
    client_socket.send('HTTP/1.1 200 OK'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))
    client_socket.send('Hello Word'.encode('utf8'))
    print(data)
