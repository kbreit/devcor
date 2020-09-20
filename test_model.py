#!/usr/bin/env python

import json
import interfaces

def main():
    ints = interfaces.interfaces()

    eth01 = ints.interface_container.switchport_list.add("Ethernet0/1")
    eth01.enabled = True
    eth01.vlan = 10
    eth02 = ints.interface_container.switchport_list.add("Ethernet0/2")
    eth02.enabled = True
    eth02.vlan = 10
    eth03 = ints.interface_container.switchport_list.add("Ethernet0/3")
    try:
        print("Trying to set bogus VLAN 9999")
        eth03.vlan = 9999
    except ValueError as exc:
        print(exc.args[0]['error-string'])

    lb0 = ints.interface_container.virtual_list.add("Loopback0")
    lb0.enabled = True
    lb0.ip_address = "192.0.2.1"

    lb1 = ints.interface_container.virtual_list.add("Loopback1")

    print(json.dumps(ints.get(), indent=2))

if __name__ == '__main__':
    main()
