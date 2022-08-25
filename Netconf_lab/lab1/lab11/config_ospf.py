from ncclient import manager
import sys

 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import sbx_n9kv_ao as device # noqa

rpc = '''
    <config>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <ospf-items>
          <inst-items>
            <Inst-list>
              <name>100</name>
              <adminSt>enabled</adminSt>
              <dom-items>
                <Dom-list>
                  <name>default</name>
                  <rtrId>1.1.1.1</rtrId>
                  <if-items>
                    <If-list>
                      <id>eth1/1</id>
                      <area>0.0.0.0</area>
                      <advertiseSecondaries>true</advertiseSecondaries>
                    </If-list>
                  </if-items>
                </Dom-list>
              </dom-items>
            </Inst-list>
          </inst-items>
        </ospf-items>
      </System>
    </config>
    '''


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
        reply = m.edit_config(rpc, target='running')
        print(reply)

if __name__ == '__main__':
     sys.exit(main())