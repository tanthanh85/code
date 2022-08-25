from ncclient import manager
import sys
from xml.etree.ElementTree import XML, fromstring
 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import csr1k as device # noqa

config_int_gi2 = """
     <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet2</name>
          <description>Configured by Python</description>
          <enabled>true</enabled>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>192.168.200.1</ip>
              <netmask>255.255.255.0</netmask>
            </address>
          </ipv4>
        </interface>
      </interfaces>
    </config>
"""
myxml = fromstring(config_int_gi2)
 # create a main() method
def main():
     """
     Main method that prints netconf capabilities of remote device.
     """
     with manager.connect(host = device["address"],
                          port = device["netconf_port"],
                          username = device["username"],
                          password = device["password"],
                          hostkey_verify = False) as m:
          


          netconf_reply = m.edit_config(myxml,target="running")
          # print(dir(manager))

          print(netconf_reply.ok)


if __name__ == '__main__':
     sys(exit(main()))