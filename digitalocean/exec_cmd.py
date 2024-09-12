import paramiko
import digitalocean

# 替换这两项
token = "xxxxxxxxxxxxxxxx"
private_key_path = "/root/.ssh/id_rsa"

def execute_ssh_command_with_key(host, command, port=22, username="root", private_key_path=private_key_path, passphrase=None):
    try:
        print(f"尝试连接服务器{host}...")
        # 创建SSH客户端
        ssh = paramiko.SSHClient()
        # 自动添加主机到known_hosts文件中
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 加载私钥
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path, password=passphrase)
        # 连接到服务器
        ssh.connect(hostname=host, port=port, username=username, pkey=private_key)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令输出
        # output = stdout.read().decode('utf-8')
        # error = stderr.read().decode('utf-8')
        # # 关闭连接
        # ssh.close()
        # if error:
        #     print(f"Error: {error}")
        # return output

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def start_all_service():
    manager = digitalocean.Manager(token=token)
    droplets = manager.get_all_droplets()
    for droplet in droplets:
        ip_addr = droplet.ip_address
        execute_ssh_command_with_key(host=ip_addr, command=f"docker-compose up -d")
        print(f"{ip_addr}：命令已下发...")

if __name__ == '__main__':
    start_all_service()