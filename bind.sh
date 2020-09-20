#!/bin/bash

pyang --plugindir \
  "$VIRTUAL_ENV"/lib/python3.7/site-packages/pyangbind/plugin \
  --format pybind interfaces.yang > interfaces.py
