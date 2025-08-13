from scapy.all import sniff
from datetime import datetime

# Callback function to process each captured packet
def packet_callback(packet):
    print("=" * 50)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if packet.haslayer("IP"):
        ip_layer = packet.getlayer("IP")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
    else:
        print("Non-IP Packet")

    print(f"Summary: {packet.summary()}")

# Main function
if __name__ == "__main__":
    print("Packet Sniffer Started (Press Ctrl+C to stop)")
    try:
        sniff(prn=packet_callback, store=False)
    except PermissionError:
        print("Permission denied: Please run as administrator/root.")
    except KeyboardInterrupt:
        print("Sniffer stopped by user.")

