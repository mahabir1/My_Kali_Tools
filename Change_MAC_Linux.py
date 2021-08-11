import subprocess

interface = input("Enter the interface you want to change: ")
new_mac = input("Enter the new mac address you want to assign: ")

subprocess.run(["ifconfig",interface,"down"])
print("Changing the mac address :)")
if(interface == "eth0"):
    subprocess.run(["ifconfig",interface,"hw","ether",new_mac])
else:
    subprocess.run(["ifconfig",interface,"wlan",new_mac])
print("MAC address changed.")
subprocess.run(["ifconfig",interface,"up"])
