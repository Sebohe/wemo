import requests
import re


class WemoDevice:

    def __init__(self, ip, port='49153'):

        try:
            self.ip = str(ip)
        except:
            #TODO raise error handling
            pass
        self.port = port
        self.setupXML = requests.get('http://'+self.ip+':'+self.port+'/setup.xml')
        self.friendlyName = (re.search('<friendlyName>(.+?)</friendlyName>', self.setupXML.text)).group(1)
        self.currentState = (re.search('<binaryState>(.+?)</binaryState>', self.setupXML.text)).group(1)
        self.macAddress = (re.search('<macAddress>(.+?)</macAddress>', self.setupXML.text)).group(1)
        self.serialNumber = (re.search('<serialNumber>(.+?)</serialNumber>', self.setupXML.text)).group(1)

        #Constants that could probably be moved into functions
        self.xmlencoding = '<?xml version="1.0" encoding="utf-8"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'

        self.headersON_OFF = {'Accept': '',
                            'Content-type': 'text/xml; charset="utf-8"',
                            'SOAPACTION': '"urn:Belkin:service:basicevent:1#SetBinaryState"'}
        self.headersGetState = {'Accept': '',
                            'Content-type': 'text/xml; charset="utf-8"',
                            'SOAPACTION': '"urn:Belkin:service:basicevent:1#GetBinaryState"'}
        self.headersSetFriendlyName = {'Accept': '',
                                    'Content-type': 'text/xml; charset="utf-8"',
                                    'SOAPACTION': '"urn:Belkin:service:basicevent:1#ChangeFriendlyName"'}

    def on(self):
        url = 'http://'+self.ip+':'+self.port+'/upnp/control/basicevent1'
        data=self.xmlencoding+'<s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>1</BinaryState></u:SetBinaryState></s:Body></s:Envelope>'
        request = requests.post(url=url, headers=self.headersON_OFF, data=data)

    def off(self):
        url = 'http://'+self.ip+':'+self.port+'/upnp/control/basicevent1'
        data=self.xmlencoding+'<s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>0</BinaryState></u:SetBinaryState></s:Body></s:Envelope>'
        request = requests.post(url=url, headers=self.headersON_OFF, data=data)

    def getState(self):
        url = 'http://'+self.ip+':'+self.port+'/upnp/control/basicevent1'
        data = self.xmlencoding+'<s:Body><u:GetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"><BinaryState>1</BinaryState></u:GetBinaryState></s:Body></s:Envelope>'
        request = requests.post(url=url, headers=self.headersGetState, data=data)
        if (re.search('<BinaryState>(.+?)</BinaryState>', request.text)).group(1)=='1':
            return ('1')
        else:
            return ('0')

    def toggle(self):

        if self.getState()=='1':
            self.off()
        else:
            self.on()

    def defineName(self, newName):
        url='http://'+self.ip+':'+self.port+'/upnp/control/basicevent1'
        data = self.xmlencoding+'<s:Body><u:ChangeFriendlyName xmlns:u="urn:Belkin:service:basicevent:1"><FriendlyName>'+newName+'</FriendlyName></u:ChangeFriendlyName></s:Body></s:Envelope>'
        request = requests.post(url=url,headers=self.headersSetFriendlyName,data=data)

        if request.status_code == 200:
            self.friendlyName = newName
        else:
            self.raiseAlarm()


    #This function generates an alarm in the scenario
    #of the wemo device not communicating
    #this needs a decorator with requests.post and request.get
    def raiseAlarm(self):
        print ("Couldn't find wemo "+self.friendlyName)

class DiscoverWemos:

    def __init__(self):
        #nmap scan only showed ports 53/tcp and 59153/udp as the open ports
        ports={'59153'}
        pass

    def upnpSearch(self):
        pass
