import socket
import rsa
import pickle
import time
import hashlib
from errorclass import AuthenticationError
from myaes import MYAES
import datetime


# 使用图灵机器人的自动回复功能
from tlrobot import get_reply

class Server:

    # 用来标记同时连接的客户端的数量
    number = 0

    # 默认的最大等待数量为5
    # 默认使用本机的ip地址和8080端口
    def __init__(self, backlog=5, addr=('localhost', 8080)):
        # 默认使用AF_INET协议族，即ipv4地址和端口号的组合以及tcp协议
        self.serverSocket = socket.socket()
        # 绑定监听的ip地址和端口号
        self.serverSocket.bind(addr)
        # 开始等待
        self.serverSocket.listen(backlog)

    # 该函数需要并行处理
    def link_one_client(self):
        # 获取客户端对象和客户端地址
        clientSocket, addr = self.serverSocket.accept()

        # 客户端数量加1
        Server.number = Server.number + 1
        # 标记当前客户端编号
        now_number = Server.number

        # 打印
        print("-----和客户端{0}建立连接\n-----目标主机地址为：{1}".format(now_number, addr))
        # 接受客户端传递的公钥
        # 这里可以加一个哈希函数检验公钥的正确性！
        # 运用pickle进行反序列化
        publicKeyPK, pubKeySha256 = pickle.loads(clientSocket.recv(1024))
        if hashlib.sha256(publicKeyPK).hexdigest() != pubKeySha256:
            raise AuthenticationError("-----密钥被篡改！")
        else:
            publicKey = pickle.loads(publicKeyPK)
            print("-----已接受公钥")

        # 下面是用公钥加密对称密钥并传递的过程
        # 产生用于对称加密的密钥

        # 初始化加密对象
        aes = MYAES()
        print("-----正在生成AES密钥")
        sym_key = aes.newkey()
        #sym_key = Random.new().read(AES.block_size)  # 随机生成密钥  # aes数据分组长度为128 bit
        #sym_key = Random.new().read(16)


        # 用pickle进行序列化用来进行网络传输
        # 对密钥进行hash保证其准确性
        en_sym_key = rsa.encrypt(pickle.dumps(sym_key), publicKey)
        en_sym_key_sha256 = hashlib.sha256(en_sym_key).hexdigest()
        print("-----正在加密传送密钥")
        clientSocket.send(pickle.dumps((en_sym_key,en_sym_key_sha256)))

        # 这里可以添加密钥交换成功的函数



        # 下面使用对称密钥进行加密对话的过程
        while True:
            time.sleep(0.3)

            en_recvData = clientSocket.recv(1024)
            recvData = aes.myaes_decrypt(en_recvData, sym_key)
            print('接收到客户端传来的消息：' + recvData)

            if recvData == 'time':
                sendData = str(datetime.datetime.now())

            else:
                sendData = input("输入你要回应的消息：")
                if(sendData == 'quit'):
                    clientSocket.close()
                    break
                
            en_sendData = aes.myaes_encrypt(sendData, sym_key)
            clientSocket.send(bytes(en_sendData))
            print("-----消息发送成功，等待回应...")








            """
            # 调用图灵机器人
            sendData = get_reply(recvData)
            # 对消息进行加密
            en_sendData = aes.myaes_encrypt(sendData)
            clientSocket.send(en_sendData)
            """



