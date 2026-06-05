from flask import Flask, render_template
from scapy.all import sniff, TCP, UDP
import threading

app = Flask(__name__)

stats = {
    "total_packets": 0,
    "tcp_packets": 0,
    "udp_packets": 0,
    "alerts": 0
}

def process_packet(packet):

    stats["total_packets"] += 1

    if TCP in packet:
        stats["tcp_packets"] += 1

    elif UDP in packet:
        stats["udp_packets"] += 1

def start_capture():

    sniff(
        prn=process_packet,
        store=False
    )

capture_thread = threading.Thread(
    target=start_capture,
    daemon=True
)

capture_thread.start()

@app.route("/")
def home():

    return render_template(
        "dashboard.html",
        stats=stats
    )

if __name__ == "__main__":
    app.run(debug=False)
