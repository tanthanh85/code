import csv
from genie.conf import Genie



def write_to_CSV(filename,data):

    report_fields = ["Interface", "MAC address"]

    with open(filename, "w")  as f:
        writer = csv.DictWriter(f,report_fields)
        writer.writeheader()
        for interface, details in data.items():
                try:
                    writer.writerow(
                        {"Interface": interface, 
                        "MAC address": details['mac_address']}
                    )
                except KeyError:
                                    writer.writerow(
                        {"Interface": interface, 
                        "MAC address": "Not available"}
                    )


testbed = Genie.init("testbed.yaml")


for name,device in testbed.devices.items():
    device.connect()
    if device.type == 'nxos':
        data=device.parse("show interface")
        filename=name+"_interface_mac"
        write_to_CSV(filename=filename,data=data)
    else:
        data=device.parse("show interfaces")
        filename=name+"_interface_mac"
        write_to_CSV(filename=filename,data=data)      
