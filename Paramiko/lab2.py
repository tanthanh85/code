from connection_info import connection_info
from paramiko.client import SSHClient, AutoAddPolicy
import time

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
try:
    client.connect(**connection_info)
    print("Connected successfully")
    CMD = "show ip interface brief" # You can issue any command you want

    stdin, stdout, stderr = client.exec_command(CMD)
    output = stdout.readlines()
    for line in output:
        print(line.strip())

except Exception:
    print ("Failed to connect")
finally:
    time.sleep(3)
    client.close()


