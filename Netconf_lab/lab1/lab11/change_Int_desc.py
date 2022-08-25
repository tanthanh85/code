from ncclient import manager
import sys
from lxml import etree


# Add parent directory to path to allow importing common vars
# sys.path.append("..") # noqa
from device_info import sbx_n9kv_ao as device # noqa

# Loopback Info - Change the details for your interface
loopback = {"id": "99", "ip": "10.99.99.1/24"}

# create a main() method
def main():
    """
    Main method that adds loopback interfaces and configures an IP address
    """

    change_desc = """
    <config>
      <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
          <name>eth1/1</name>
          <config>
            <description>Configured by OpenConfig YANG.....!!!!s</description>
          </config>
        </interface>
      </interfaces>
    </config>
    
    
    """

    with manager.connect(host = device["address"],
                         port = device["netconf_port"],
                         username = device["username"],
                         password = device["password"],
                         hostkey_verify = False) as m:

        
        
        netconf_response = m.edit_config(target='running', config=change_desc)

        save_config = """
        
        
        """


        # Parse the XML response
        print(netconf_response.ok)


if __name__ == '__main__':
    sys.exit(main())