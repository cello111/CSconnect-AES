import threading

from serverclass import Server

print("-----欢迎使用服务端程序！服务启动中...")

server = Server()
server.link_one_client()


"""
while True:
	# 这里使用多线程可以避免服务器阻塞在一个客户端上
    t = threading.Thread(target=server.link_one_client)
    t.start()
"""
