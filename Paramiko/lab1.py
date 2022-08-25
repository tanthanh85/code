from connection_info import connection_info
from paramiko.client import SSHClient, AutoAddPolicy

client = SSHClient()

client.load_system_host_keys()
try:
    client.connect(**connection_info)
    print("Connected successfully")
except Exception:
    print ("Failed to connect")
finally:
    client.close()