#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2018/8/21 下午10:46'

#info:


"""
import socket

target_host = '127.0.0.1'
target_port = 8001

#建立一个socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#发送数据
client.sendto('AABBCCDDEE', target_host, target_port)


# 接受数据
data, addr = client.recvfrom(4096)


print data
