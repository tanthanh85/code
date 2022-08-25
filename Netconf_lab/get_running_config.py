from connection_info import connection_info
from ncclient import manager
from pprint import pprint


device = manager.connect(**connection_info)


conf = device.get_config(source='running').data_xml

pprint(conf)