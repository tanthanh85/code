from connection_info import connection_info
from ncclient import manager

device = manager.connect(**connection_info)


for cap in device.server_capabilities:
    if "http://openconfig.net/yang/" in cap:
        print(cap)

