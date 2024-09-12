# -*- coding: UTF-8 -*-
'''
@Project ：DynamicCloud 
@File    ：create_multi_droplet.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/13 1:27 
@Comment ： 
'''
import digitalocean

snapshot_id = "xxxxxxxxx"    # 输入快照id
number = 9              # 创建的服务器数量
token = "xxxxxxxxxxx"   # 替换你的

def create_droplet(snapshot_id):
    manager = digitalocean.Manager(token=token)
    keys = manager.get_all_sshkeys()
    droplet = digitalocean.Droplet(token=token,
                                   name="Demo",
                                   region='sgp1',  # 这里选的新加坡，按需替换
                                   image=snapshot_id,  # Ubuntu 20.04 x64
                                   size_slug='s-1vcpu-512mb-10gb',  # 512MB RAM, 1 vCPU
                                   ssh_keys=keys,
                                   backups=True)
    droplet.create()

if __name__ == '__main__':
    for _ in range(number):
        print(f"正在创建云服务器{_}...")
        create_droplet(snapshot_id)