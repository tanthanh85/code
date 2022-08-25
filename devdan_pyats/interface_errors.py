import logging
from pyats import aetest
from unicon.core.errors import *
from genie.testbed import load



logger = logging.getLogger(__name__)




class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self,testbed):
        
        testbed = load(testbed)
        self.parent.parameters.update(testbed=testbed)
    @aetest.subsection
    def connect(self,testbed):
        assert testbed, "no testbed is provided"
        try:
            testbed.connect()
        except (TimeoutError, ConnectionError) as e:
            logger.error('Unable to connec to all devices')
class InterfaceError(aetest.Testcase):
    @aetest.setup
    def setup(self,testbed):
        '''learn and share interface details'''
        self.learnt_interfaces = {}
        for device_name,device in testbed.devices.items():
            self.learnt_interfaces[device_name]=device.learn('interface').info
            logger.info('***********&&&&&&&&&&&&&&&&&&'*100)
            logger.info(dir(device.learn('interface')))
        #     with open('logging.json','a+') as f:
        #         f.write(str(dir(device.learn('interface'))))
    
        # with open('learnt_interface.json','w') as f:
        #     f.write(str(self.learnt_interfaces))



    @aetest.test
    def Test(self,steps):
        self.counter_error_keys = ("in_crc_errors", "in_errors", "out_errors")
        for device_name, interfaces in self.learnt_interfaces.items():
            with steps.start(
                f"Looking for Interface Errors on {device_name}", continue_=True
            ) as device_step:
                # Loop over every interface that was learnt
                for interface_name, interface in interfaces.items():
                    with device_step.start(f'Looking for interface errors on {device_name}', continue_=True) as interface_step:
                        if "counters" in interface.keys():
                            for counter in self.counter_error_keys:
                                if counter in interface["counters"].keys():
                                    if interface["counters"][counter] > 0:
                                        interface_step.failed(
                                            f'Device {device_name} Interface {interface_name} has a count of {interface["counters"][counter]} for {counter}'
                                        )
                                else:
                                    # if the counter not supported, log that it wasn't checked
                                    logger.info(
                                        f"Device {device_name} Interface {interface_name} missing {counter}"
                                    )
                        else:
                            # If the interface has no counters, mark as skipped
                            interface_step.skipped(
                                f"Device {device_name} Interface {interface_name} missing counters")


class Cleanup(aetest.CommonCleanup):
    @aetest.subsection
    def subsection_cleanup_one(self,testbed):
        testbed.disconnect()


if __name__ == "__main__":
    # for stand-alone execution
    import argparse
    from pyats import topology

    # from genie.conf import Genie

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument(
        "--testbed",
        dest="testbed",
        help="testbed YAML file",
        type=topology.loader.load,
        # type=Genie.init,
        default='testbed.yaml',
    )

    # do the parsing
    args = parser.parse_known_args()[0]

    aetest.main(testbed=args.testbed)


