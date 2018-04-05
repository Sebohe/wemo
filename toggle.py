import requests
import re
from wemo_devices import WemoDevice

if __name__ == "__main__":

    #The ip needs to be hardcoded for now.
    myWemo = WemoDevice('')
    print(myWemo.friendlyName)
    myWemo.toggle()
    #myWemo.defineName("light")
    print(myWemo.friendlyName)
