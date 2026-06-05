from scapy.all import sniff, IP, TCP, UDP
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATS_FILE = os.path.join(BASE_DIR, "data", "stats.json")

stats = {
    "total_packets": 0,
    "tcp_packets": 0,
    "udp_packets": 0,
    "alerts": 0
}

def save_stats():

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)

def process_packet(packet):

    stats["total_packets"] += 1

    if TCP in packet:
        stats["tcp_packets"] += 1

    elif UDP in packet:
        stats["udp_packets"] += 1

    if stats["total_packets"] % 50 == 0:
        save_stats()

    if IP in packet:

        print(
            f"Packets: {stats['total_packets']} | "
            f"TCP: {stats['tcp_packets']} | "
            f"UDP: {stats['udp_packets']}"
        )

print("Monitoring Network...")

save_stats()

sniff(
    prn=process_packet,
    store=False
)
