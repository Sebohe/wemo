#!/usr/bin/env python3
import requests
from wemo_devices import WemoDevice
import sys
import os
from time import sleep

def detectCellPhone():
    
    host = '192.168.1.149'

    while True:
        response = os.system('ping -c 1 ' + host)
        print (response)
        sleep(1)
        if response == False:
            break
   
    return True  
    

if __name__ == "__main__":
   
    assert(len(sys.argv) <= 3)
    myWemo = WemoDevice(sys.argv[1])
    if sys.argv[-1] == "on":
        myWemo.on()
        exit()

    if sys.argv[-1] == "off":
        myWemo.off()
        exit()

    if sys.argv[-1] == "detect":
        detectCellPhone()
        myWemo.on()
        exit() 
     
    myWemo.toggle()
