from pyats.topology import loader
from genie.utils import Dq as DQ

from pprint import pprint
tb = loader.load('testbed.yaml')

print(tb.devices)

for name in tb.devices:

    R1 = tb.devices[name]
    R1.connect()
    parsed_output = R1.parse('show version')
    standard_os = '17.6.1a'

    ios_check = DQ(parsed_output).contains(standard_os).get_values('version')

    if ios_check:
        print(f'{R1} IOS Check passed!')
    else:
        print(f'{R1} IOS Check failed!')

    R1.disconnect()