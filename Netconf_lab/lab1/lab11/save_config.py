
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
    save_config = """

        <copy_running_config_src xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <startup-config/>
        </copy_running_config_src>

    """



    with manager.connect(host = device["address"],
                          port = device["netconf_port"],
                          username = device["username"],
                          password = device["password"],
                          hostkey_verify = False) as m:

         # Collect the NETCONF response
        netconf_response = m.dispatch(xml_.to_ele(save_config))

        
        print(netconf_response.ok)


if __name__ == '__main__':
     sys.exit(main())