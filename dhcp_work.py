from scapy.all import *


# p = sniff(iface="Wi-Fi", filter="udp and ( port 67 or port 68 )")
# p.summary()

# print(help(sniff))


def callback(pkt):
	
	return pkt[BOOTP].chaddr.hex(':')[:17]


sniff(prn=callback, filter="udp and (port 67 or 68)", store=0)


