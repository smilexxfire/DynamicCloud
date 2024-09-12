# -*- coding: UTF-8 -*-
'''
@Project ：DynamicCloud 
@File    ：delete_all.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/13 1:31 
@Comment ： 
'''
import digitalocean

token = "xxxxxxxxxxxxxxx"   # 替换你的
def delete_all():
    manager = digitalocean.Manager(token=token)
    droplets = manager.get_all_droplets()
    for droplet in droplets:
        droplet.destroy()

if __name__ == '__main__':
    delete_all()