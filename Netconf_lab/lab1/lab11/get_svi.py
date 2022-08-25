from ncclient import manager
import sys
from lxml import etree

 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import sbx_n9kv_ao as device # noqa

 # create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    svi  = """

      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
          <svi-items>
            <If-list>
              <id/>
              <vlanId/>
              <mac/>
              <mtu/>
              <adminSt/>
            </If-list>
          </svi-items>
        </intf-items>
      </System>

    """

    with manager.connect(host = device["address"],
                          port = device["netconf_port"],
                          username = device["username"],
                          password = device["password"],
                          hostkey_verify = False) as m:

         # Collect the NETCONF response
        netconf_response = m.get(('subtree', svi))
        print(netconf_response)

         # Parse the XML and print the data
        # xml_data = netconf_response.data_ele
        #  systemname =  xml_data.find(".//{http://cisco.com/ns/yang/cisco-nx-os-device}name").text

        #  print("The system name for {} is {}".format(device["address"], systemname))


if __name__ == '__main__':
     sys.exit(main())