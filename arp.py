from scapy.all import *
from time import sleep


pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.96.3.37")
loop = True

while loop:

	resp = srp(pkt, iface="Wi-Fi", timeout=1, verbose=False)

	if len(resp[0]) != 0:
		a = str(resp[0][0].answer[ARP].hwsrc)
		print(a)
		loop = False
	sleep(1)



# try:
# 	a = str(resp[0][0].answer[ARP].hwsrc)
# 	print(a)

# except:
# 	pass

# print(len(resp[0]))



