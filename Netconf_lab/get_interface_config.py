from connection_info import connection_info
from ncclient import manager
from pprint import pprint
import xmltodict


device = manager.connect(**connection_info)
filter = """

      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        </interface>
      </interfaces>

"""


int_data = device.get('subtree',filter=filter)

int_dict=xmltodict.parse(int_data.xml)

pprint(int_dict)