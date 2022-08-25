from genie.testbed import load
from pprint import pprint


tb = load('testbed.yaml')

device = tb.devices['R1']

device.connect()

output = device.learn('interface')

pprint(output.info)