import json
from netmiko import ConnectHandler


device = []
with open('devices.json','r') as f:
    devices = json.load(f)

# print(devices)

CMD = "show interfaces"

for device in devices:
    filename = f"{device['name']}.json"
    print(f"Retrieving configuration for {device['name']}")
    with ConnectHandler(**device['connection']) as conn:
        out = conn.send_command(CMD, use_genie=True)
        with open(filename,'w') as f:
            f.write(json.dumps(out))
