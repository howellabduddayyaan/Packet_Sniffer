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
    

    if IP in packet :
        
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")
        
# _________________________________________________________________________________________________

        if TCP in packet:
            print("Protocol         : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
            
# _________________________________________________________________________________________________

print("\nListening for packets...\n")

sniff(prn = sniff_packet, store = False)

# _________________________________________________________________________________________________