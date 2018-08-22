#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2018/8/21 下午10:39'

#info:


"""
import socket



target_host = 'www.baidu.com'
target_port = 80


#建立socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#链接客户端
client.connect((target_host, target_port))

#发送数据
client.send("GET / HTTP/1.1\rHost: baidu.com\r\n\r\n")


#接受数据
response = client.recv(4096)

print response