import logging
from pyats import aetest
from unicon.core.errors import *

logger = logging.getLogger(__name__)


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self,testbed):
        assert testbed, "Testbed is not provided"
        try:
            testbed.connect()
        except (TimeoutError,ConnectionError):
            logger.error("Unable to connect all devices")

class verify_connected(aetest.Testcase):
    @aetest.test
    def verify_connection(self,testbed,steps):
        for name,device in testbed.devices.items():
            with steps.start(f'Test connection status of {name}', continue_=True) as step:
                if device.connected:
                    logger.info(f'{name} connection status is {device.connected}')
                else:
                    logger.error(f'{name} connection status is {device.connected}')
                    step.failed()

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self,testbed):
        testbed.disconnect()


if __name__=='__main__':
    import argparse
    from pyats import topology

    parser = argparse.ArgumentParser(description='Standalone parser')
    parser.add_argument("--testbed", dest="testbed",type=topology.loader.load,default='testbed.yaml')
    

    args = parser.parse_known_args()[0]
    aetest.main(testbed=args.testbed)


