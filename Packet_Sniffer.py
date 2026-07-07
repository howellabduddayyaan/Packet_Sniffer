# ======================
# === Packet Sniffer ===
# ======================

from scapy.all import sniff, IP, TCP, UDP, ICMP

print("\n======================")
print("=== Packet Sniffer ===")
print("======================")

count = 0

def sniff_packet(packet):

    count += 1

    print(f"\nPacket {count}")

    # if IP in packet :