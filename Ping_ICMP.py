from scapy import packet
from scapy.all import IP
from scapy.all import sr1
from scapy.all import ICMP
from scapy.sendrecv import sr

src_IP = "192.168.43.138"
dest_IP = "www.google.com"
ip_layer = IP(
    src = src_IP,
    dst = dest_IP
    )
icmp_req = ICMP(id=100)
packet = ip_layer / icmp_req
response = sr1(packet, iface="Wi-Fi")
print(response.show())
