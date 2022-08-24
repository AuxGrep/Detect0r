#JUST TEMPORARY SCRIPT 2 DETECT HIDDEN WIFI ATTACKS 
#written By_ Hezron

import time
import subprocess
from scapy.all import *
import time,datetime
import os
import pkg_resources
import sys
from banner import banner

clean = "clear"
required = {'scapy', 'gTTS'} #kama huna hii package install manual pip3 install scapy or sudo apt-get install python3-scapy
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    
os.system(clean)
time.sleep(2)
intr = input("Enter monitor mode interface: ")
print()
Dfilter1 = "'wlan type mgt and (subtype deauth or subtype disassoc)'"
time.sleep(3)
	#subprocess.call('sudo wireshark -i ' + intr + ' -k ' + ' -f ' + Dfilter1 + ' & ', shell=True)
def process_packet(packet):
    if packet.haslayer(Dot11Deauth):
        print(' [ ' +  str(datetime.datetime.now())+ ' ] '+  ' Powerful Deauthentication Attack Detected Against Mac Address: ' +   											str(packet.addr2).swapcase())
sniff(iface="" + intr, prn=process_packet, store=False, count=0) 
