# DynamicCloud
云服务资源调度平台，为HyperionScan提供动态创建、销毁扫描节点的能力
## 应用场景
使用云服务器动态创建扫描节点，可以动态变换ip，同时根据需求选择服务器数量、归属地等，配合HyperionScan分布式扫描的支持，可以快速高质完成大批量扫描任务
## 使用
### 单机
这里说明单机如何快速部署多个扫描服务：使用docker-compose完成
编写配置文件.env，替换成自己的配置
```shell
rabbitmq_host=xxxxxxxx
rabbitmq_port=5672
rabbitmq_username=admin
rabbitmq_password=xxxxx
mongo_host=xxxxxxxxx
mongo_port=27017
mongo_username=admin
mongo_password=xxxxxxxxx
mongo_database=src
```
编写docker-compose, 按需填入自己需要开启的扫描服务
```yaml
version: '3'
services:
  subdomainscan:
    image: smilexxfire/subdomainscan
    env_file:
    - .env
    restart: always
  oneforallscan:
    image: smilexxfire/oneforall
    env_file:
      - .env
    restart: always
  portscan:
    image: smilexxfire/portscan
    env_file:
      - .env
    restart: always
  sitefind:
    image: smilexxfire/sitefind
    env_file:
      - .env
    restart: always
  dirscan:
    image: smilexxfire/dirscan
    env_file:
      - .env
    restart: always
  vulnscan:
    image: smilexxfire/vulnscan
    env_file:
      - .env
    restart: always
```
运行`docker-compose up -d` 即可启动所有服务
![img.png](https://qiniu.xxf.world/pic/2024/09/13/bb12db1a-ff68-4f11-b157-821e59dee263.png)
此时查看rabbitmq、Connection部分，六个服务对应六个Connection
![](https://qiniu.xxf.world/pic/2024/09/13/db99d722-8b4f-4f48-97cd-af3513ca259e.png)
### digitalocean
借助digitalocean官方提供的API能力，可以通过自己账户的token完成云服务的动态创建和生成

扫描节点支持以最小配置创建： 即s-1vcpu-512mb-10gb，该配置价格为$0.006/hour，非常友好

原理和单机创建一样，首次使用需完成以下步骤以创建快照：
1. 编辑`digitalocean/add_ssh_key.py`并运行，添加自己的ssh key
2. 编辑`digitalocean/create_one_basic.py`并运行，新建一台服务器
3. 通过ssh连接服务器，运行脚本文件以完成docker相关环境安装：`digitalocean/create_one_basic.py`
4. 填入.env文件、docker-compose文件内容，并运行`docker-compose up -d`测试服务正常启动
5. 运行`docker-compose down`关闭服务
6. 通过可视化面板完成快照创建：Take snapshot
7. 快照创建完成后，编辑`digitalocean/create_one_basic.py`并运行，获取到快照id并保存下来

接着通过快照id自动化创建多个云服务器
1. 编辑`digitalocean/create_multi_droplet.py`并运行，即可创建多个服务器
2. 编辑`digitalocean/exec_cmd.py`并运行，下发`docker-compose up -d`指令，完成扫描服务的启动
![](https://qiniu.xxf.world/pic/2024/09/13/87b4fb91-8e15-45fd-af34-9a4b8ed64321.png)
![](https://qiniu.xxf.world/pic/2024/09/13/848a472c-a188-4d0e-97cd-d3b83052f388.png)
这里有两个节点没有连接上，原因是digitalocean部分ip被墙


## TODO
- [x] 支持digitalocean
- [ ] 支持aws