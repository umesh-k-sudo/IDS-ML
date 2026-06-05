from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

print("Monitoring Network...")

sniff(prn=process_packet, store=False)
