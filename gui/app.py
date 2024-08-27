import tkinter as tk
from tkinter import filedialog, messagebox
from forensics.cloud_handler import CloudHandler
from forensics.memory_dump import MemoryDump
from forensics.packet_capture import PacketCapture
from forensics.report_generator import ReportGenerator

class CyberForensicsApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cyber Forensics Toolkit")
        self.cloud_handler = CloudHandler()
        self.memory_dump = MemoryDump()
        self.packet_capture = PacketCapture()
        self.report_generator = ReportGenerator()

    def run(self):
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Cloud Snapshot Button
        snapshot_button = tk.Button(self.window, text="Create Cloud Snapshot", command=self.create_snapshot)
        snapshot_button.pack()

        # Memory Dump Button
        dump_button = tk.Button(self.window, text="Capture Memory Dump", command=self.capture_memory_dump)
        dump_button.pack()

        # Packet Capture Button
        capture_button = tk.Button(self.window, text="Capture Network Packets", command=self.capture_packets)
        capture_button.pack()

        # Generate Report Button
        report_button = tk.Button(self.window, text="Generate Report", command=self.generate_report)
        report_button.pack()

    def create_snapshot(self):
        instance_id = self.ask_for_input("Enter Cloud Instance ID:")
        snapshot_id = self.cloud_handler.create_snapshot(instance_id)
        messagebox.showinfo("Snapshot Created", f"Snapshot ID: {snapshot_id}")

    def capture_memory_dump(self):
        output_path = filedialog.asksaveasfilename(defaultextension=".lime")
        result = self.memory_dump.capture_memory_dump(output_path)
        messagebox.showinfo("Memory Dump", result)

    def capture_packets(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".pcap")
        iface = self.ask_for_input("Enter Network Interface:")
        result = self.packet_capture.capture_packets(iface, output_file)
        messagebox.showinfo("Packet Capture", result)

    def generate_report(self):
        findings = ["Snapshot created", "Memory dump captured", "Packets captured"]
        report_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        self.report_generator.generate_report(findings, report_path)
        messagebox.showinfo("Report Generated", f"Report saved to {report_path}")

    def ask_for_input(self, prompt):
        return tk.simpledialog.askstring("Input", prompt)

