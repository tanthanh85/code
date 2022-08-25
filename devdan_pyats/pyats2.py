from pyats import aetest
from genie.utils import Dq
from pyats.topology import loader
tb = loader.load('testbed.yaml')
import logging

logger = logging.getLogger(__name__)

#Common setup section
class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self,steps, testbed):
        for host in testbed.devices:
            device = testbed.devices[host]
            self.parent.parameters.update(device=device)
            with steps.start(f'Connect to {host}'):
                device.connect()


#Test section
class FirstTestCase(aetest.Testcase):
    @aetest.setup
    def setup(self,testbed,device):
        if device.connected:
            self.passed('Successfully connected to {device.name}')
        else:
            self.failed('Could not connect to {device.name}')
    @aetest.test
    def verify_ios_version(self,steps,device):
        with steps.start('Checking IOS version') as step:
            try:
                self.version = device.parse('show version')
                ios_check = Dq(self.version).contains('17.6.1').get_values('version')
                if ios_check:
                    step.passed(f'{device.name} runs the proper IOS version')
                else:
                    step.failed(f'{device.name} runs non-standard IOS version')
            except Exception as e:
                step.failed('Something went wrong {str(e)}')
#Cleanup section
class CommonCleanup(aetest.CommonCleanup):
    aetest.subsection
    def disconnect(self, steps,device):
        steps.start('Disconnecting {device.name}')
        device.disconnect()


# if __name__ == '__main__':
#     logging.getLogger(__name__).setLevel(logging.DEBUG)
#     logging.getLogger('pyats.aetest').setLevel(logging.DEBUG)
    
#     aetest.main(testable='./pyats2.py',testbed=tb)