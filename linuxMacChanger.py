'''
Require command for mac changer
Current Mac:*
**********************************
ifconfig [interface] down
ifconfig [interface] hw ether [mac_address]
ifconfig [interface] up
**************************************'''

import subprocess as sp
from optparse import OptionParser
import re


def changeMac(interface,mac):
    if interface==None or mac==None:
        print('[!] Please give input for Interface and Mac Address')
    elif(isThisMac(mac)):
        cm=getCurrentMac(interface)
        print(f'[*] Your current Mac address:{cm}')
        print(f'[+] Start Changing mac address of interface {interface} into {mac}')
        print("**************************************************************************************")
        sp.call(f'sudo ifconfig {interface} down',shell=True)
        try:
            sp.call(f'sudo ifconfig {interface} hw ether {mac}',shell=True)
        except :
            pass
        sp.call(f'sudo ifconfig {interface} up',shell=True)
        nm=getCurrentMac(interface)
        if cm==nm:
            print(f"[!] Process failed \n[*] your current mac is {cm}")
        else:
            print(f"[+] Your mac has been change successfully.\n[*] Your Current Mac Address: {nm}")

    else:
        print(f'[!] You are a stupid, {mac} is not a valid mac address' )

def isThisMac(mac):
    flag=True
    if len(mac)!=17:
        return False
    else:
        for i in range(0,len(mac)):
            if (i+1)%3==0 and (mac[i]!=':'):
                flag=False
                
        return flag

def getCurrentMac(interface):
    output=sp.check_output(f'ifconfig {interface}',shell=True)
    output=str(output)
    list_of_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output)
    return list_of_mac.group(0)



if __name__ == "__main__":   
    # *******************************start Taking input********************************************************
    parser=OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Name of the interface to change it's MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="Enter New Mac Address")
    (options,argument)=parser.parse_args()
    mac=options.new_mac
    interface=options.interface
    # **********************************END**********************************************************
    changeMac(interface,mac)