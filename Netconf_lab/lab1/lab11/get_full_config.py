from io import UnsupportedOperation
from ncclient import manager
import sys


 # Add parent directory to path to allow importing common vars
#  sys.path.append("..") # noqa
from device_info import csr1k as device # noqa

 # create a main() method
def main():

        with manager.connect(host = device["address"],
            port = device["netconf_port"],
            username = device["username"],
            password = device["password"],
            hostkey_verify = False) as m:

            # Collect the NETCONF response
            netconf_response = m.get_config('running')
            with open("%s.xml" % device["address"], 'w') as f:
                f.write(netconf_response.data_xml)
            # Parse the XML and print the data


if __name__ == '__main__':
     sys.exit(main())