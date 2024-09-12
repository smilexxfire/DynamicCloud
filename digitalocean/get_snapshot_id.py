# -*- coding: UTF-8 -*-
'''
@Project ：DynamicCloud 
@File    ：get_snapshot_id.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/13 1:25 
@Comment ： 
'''
import digitalocean

token = "xxxxxxxxxxxxxxxxx"  # 替换你的
def get_all_snapshot_id():
    manager = digitalocean.Manager(token=token)
    snapshots = manager.get_all_snapshots()
    for snapshot in snapshots:
        print(snapshot.id)

if __name__ == '__main__':
    get_all_snapshot_id()