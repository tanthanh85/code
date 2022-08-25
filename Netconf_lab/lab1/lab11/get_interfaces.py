from xml.etree.ElementTree import indent
from ncclient import manager
import sys
from lxml import etree
import xmltodict

from xml.dom import minidom


 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import sbx_n9kv_ao as device

 # create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    hostname = """

                <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                    <name/>
                </System>

    """



    with manager.connect(host = device["address"],
                          port = device["netconf_port"],
                          username = device["username"],
                          password = device["password"],
                          hostkey_verify = False) as m:

         # Collect the NETCONF response
        netconf_response = m.get(('subtree', hostname))

        
        hostname_dict= xmltodict.parse(netconf_response.xml)
        xml_data=etree.fromstring(netconf_response.data_xml)
        xml_tree=etree.ElementTree(xml_data)

        ns = {"ns": "http://cisco.com/ns/yang/cisco-nx-os-device"}

 
        systemname = xml_tree.find("//ns:name",ns).text

        # print(hostname_dict['rpc-reply']['data']['System']['name'])


        print (systemname)
         # Parse the XML and print the data
        # xml_data = netconf_response.data_ele
        #  systemname =  xml_data.find(".//{http://cisco.com/ns/yang/cisco-nx-os-device}name").text

        #  print("The system name for {} is {}".format(device["address"], systemname))


if __name__ == '__main__':
     sys.exit(main())