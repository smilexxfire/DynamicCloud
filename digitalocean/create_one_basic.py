# -*- coding: UTF-8 -*-
'''
@Project ：DynamicCloud 
@File    ：create_one_basic.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/13 1:17 
@Comment ： 创建一台机器
'''
import digitalocean

token = "secretspecialuniquesnowflake"  # 替换成你的

if __name__ == '__main__':
    manager = digitalocean.Manager(token=token)
    keys = manager.get_all_sshkeys()
    droplet = digitalocean.Droplet(token=token,
                                   name="Demo",
                                   region='sgp1',  # 这里选的新加坡，按需替换
                                   image="ubuntu-20-04-x64",  # Ubuntu 20.04 x64
                                   size_slug='s-1vcpu-512mb-10gb',  # 512MB RAM, 1 vCPU
                                   ssh_keys=keys,
                                   backups=True)
    droplet.create()