#!/usr/bin/env python3
import requests
from wemo_devices import WemoDevice
import sys

if __name__ == "__main__":
    
    assert(len(sys.argv) <= 3)
    myWemo = WemoDevice(sys.argv[1])
    if sys.argv[-1] == "on":
        myWemo.on()
        exit()

    if sys.argv[-1] == "off":
        myWemo.off()
        exit()
     
    myWemo.toggle()
