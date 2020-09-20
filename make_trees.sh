#!/bin/bash

pyang --format tree --path yang_big --lax-quote-checks \
  yang_big/vendor/cisco/xe/16111/Cisco-IOS-XE-dhcp.yang \
  > data_ref/xe_16111_dhcp.txt

