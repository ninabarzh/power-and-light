from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1

pkt = IP(dst="192.168.20.50") / TCP(dport=20000, flags="S")
resp = sr1(pkt, timeout=2, verbose=False)

print(resp)


