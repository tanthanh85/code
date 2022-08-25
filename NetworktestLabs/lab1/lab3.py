from pyats.topology import loader

testbed = loader.load('testbed.yaml')

testbed.devices

R1 = testbed.devices['R1']
R2 = testbed.devices['R2']
SW1 = testbed.devices['SW1']

links = []
for link in R1.find_links(R2):
    links.append(link)

print(len(links))

# R1.connect()

# print(R1.execute('show version'))