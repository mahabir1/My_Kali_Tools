from scapy.all import Ether, ARP, srp
if __name__ == "__main__":
    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)
    ip_range = "Your IP range"    #Example: 192.168.1.1/24
    arp_layer = ARP(pdst = ip_range)
    packet = ether_layer / arp_layer
    ans, unans = srp(packet, iface = "Wi-Fi", timeout=2)
    print(ans)
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)
