cd /d C:\Program Files\Wireshark
tshark -i 9 -a duration:10 -z icmp,srt,ip.src=="10.1.120.113"
command > lukket.txt