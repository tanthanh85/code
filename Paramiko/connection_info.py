import getpass
connection_info = {
      'hostname': '192.168.50.61',
      'port': 22,
      'username': 'admin',
      'password': getpass.getpass(prompt="Password: "),
      'look_for_keys': False, 
      'allow_agent': False
}