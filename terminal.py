import os
import sys

ip = "10.1.120.113"

os.system('''C:\Program Files\Wireshark\tshark -i 9 -a duration:10 -z icmp,srt,ip.src=="{ip}"''')

"cd /d " , "python terminal.py > lukket.txt"