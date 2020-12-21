'''
byt2 = (1024).to_bytes(16, byteorder = 'big')
print(byt2)

num1 = int.from_bytes(byt2, byteorder = 'big')
print(num1)


BS = 16
pad = lambda s:  (BS - len(s) % BS) * chr(BS - len(s) % BS) + s
unpad = lambda s: s[ord(s[0]):]
'''
'''
# 填充信息
BS = 16  # 分组数据长度
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

str1 = '012345678901234'
a = pad(str1)
print(a)

b = unpad(a)
print(b)

#print(str1[3:-3]) #截取第一位到第三位的字符
'''
str1 = '123'
str2 = '456'
b1 = b'0123456789ABCDEF'
for i in range(int(len(b1)/4)):
    #print(b1[4*i:4*i+4])
    gadget = b1[4*i:4*i+4]
    print(gadget)