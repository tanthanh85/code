
from ncclient import manager, xml_
import sys


 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import sbx_n9kv_ao as device

 # create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    get_info = """
    <filter>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <serial/>
      </System>
    </filter>
    """



    with manager.connect(host = device["address"],
                          port = device["netconf_port"],
                          username = device["username"],
                          password = device["password"],
                          hostkey_verify = False) as m:

         # Collect the NETCONF response
        netconf_response = m.get(get_info)

        
        print(netconf_response)


if __name__ == '__main__':
     sys.exit(main())