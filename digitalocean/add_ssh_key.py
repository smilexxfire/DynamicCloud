# -*- coding: UTF-8 -*-
'''
@Project ：DynamicCloud 
@File    ：add_ssh_key.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/13 1:05 
@Comment ： 将ssh key公钥加入digitalocean
'''
from digitalocean import SSHKey


if __name__ == '__main__':
    token = "secretspecialuniquesnowflake"  # 替换成你的
    ssh_key_path = "C:\\Users\\xxx\\.ssh\\id_rsa.pub"   # 替换成你的

    user_ssh_key = open(ssh_key_path).read()
    key = SSHKey(token=token,
                 name='uniquehostname',
                 public_key=user_ssh_key)
    key.create()