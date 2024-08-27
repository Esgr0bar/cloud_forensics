import subprocess
from scapy.all import sniff, wrpcap

class PacketCapture:
    def capture_packets(self, iface, output_file):
        packets = sniff(iface=iface, timeout=60)
        wrpcap(output_file, packets)
        return f"Packets captured and saved to {output_file}"

    def analyze_packets(self, pcap_file):
        # Analyze packets using TShark
        analysis_output = f"{pcap_file}_analysis.txt"
        subprocess.run([
            "tshark", "-r", pcap_file, "-q", "-z", f"io,stat,0", ">", analysis_output
        ], shell=True)
        return f"Packet analysis completed. Output saved to {analysis_output}"
