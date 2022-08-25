
from netmiko import ConnectHandler
from jinja2 import Environment,FileSystemLoader


connection_info = {
      'device_type': 'cisco_ios',
      'host': '192.168.50.61',
      'port': 22,
      'username': 'admin',
      'password': 'cisco'
}

loader = FileSystemLoader("templates")
environment = Environment(loader=loader)
tpl = environment.get_template("acl.cnf.tpl")

allowed = [
      "10.10.0.10",
      "10.10.0.11",
      "10.10.0.12"
]

disallowed = [
      "10.10.0.50",
      "10.10.0.62"
]

intf = "GigabitEthernet2"

out = tpl.render(allowed=allowed,disallowed=disallowed,intf=intf)
with open("configuration.conf", "w") as f:
    f.write(out)

with ConnectHandler(**connection_info) as conn:
    conn.send_config_from_file('configuration.conf')