from netmiko import ConnectHandler
from connection_info import connection_info

conn = ConnectHandler(**connection_info)

with ConnectHandler(**connection_info) as conn:
    
    out = conn.send_command('show interfaces', use_genie=True)
    # print(out)

    
for name, details in out.items():
    print(f"{name}")
    print(f"- Status: {details.get('enabled', None)}")