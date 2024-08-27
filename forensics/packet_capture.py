from scapy.all import sniff, wrpcap

class PacketCapture:
    def capture_packets(self, iface, output_file):
        packets = sniff(iface=iface, timeout=60)
        wrpcap(output_file, packets)
        return output_file

    def analyze_packets(self, pcap_file):
        #to do  Use Scapy or Tshark for analysis
        return "Packet Analysis Completed"
