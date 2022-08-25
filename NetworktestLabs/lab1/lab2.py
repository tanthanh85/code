from pyats.topology import loader

from pprint import pprint


tb = loader.load('testbed.yaml')
learnt ={}

for name, dev in tb.devices.items():
    dev.connect()
    learnt[name] = {}
    learnt[name]['ospf'] = dev.learn('ospf')


pprint(learnt['R1']['ospf'].info)s