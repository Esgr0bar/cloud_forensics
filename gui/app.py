import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from forensics.cloud_handler import CloudHandler
from forensics.memory_dump import MemoryDump
from forensics.packet_capture import PacketCapture
from forensics.report_generator import ReportGenerator

class ForensicsCloudApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cloud Forensics Toolkit")
        self.window.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Styling with ttk for a better appearance
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TLabel', font=('Helvetica', 12), padding=10)
        style.configure('TEntry', font=('Helvetica', 12), padding=10)

        # Cloud Provider Selection
        self.cloud_provider_label = ttk.Label(self.window, text="Select Cloud Provider:")
        self.cloud_provider_label.pack()
        self.cloud_provider_var = tk.StringVar()
        self.cloud_provider_combo = ttk.Combobox(self.window, textvariable=self.cloud_provider_var)
        self.cloud_provider_combo['values'] = ('aws', 'azure', 'gcp')
        self.cloud_provider_combo.current(0)
        self.cloud_provider_combo.pack()

        # Instance ID Input
        self.instance_id_label = ttk.Label(self.window, text="Enter Cloud Instance ID:")
        self.instance_id_label.pack()
        self.instance_id_entry = ttk.Entry(self.window, width=40)
        self.instance_id_entry.pack()

        # Network Interface Input
        self.interface_label = ttk.Label(self.window, text="Enter Network Interface (e.g., eth0):")
        self.interface_label.pack()
        self.interface_entry = ttk.Entry(self.window, width=40)
        self.interface_entry.pack()

        # Buttons for actions
        self.snapshot_button = ttk.Button(self.window, text="Create Cloud Snapshot", command=self.create_snapshot)
        self.snapshot_button.pack(pady=10)

        self.dump_button = ttk.Button(self.window, text="Capture Memory Dump", command=self.capture_memory_dump)
        self.dump_button.pack(pady=10)

        self.capture_button = ttk.Button(self.window, text="Capture Network Packets", command=self.capture_packets)
        self.capture_button.pack(pady=10)

        self.report_button = ttk.Button(self.window, text="Generate Report", command=self.generate_report)
        self.report_button.pack(pady=10)

    def create_snapshot(self):
        cloud_provider = self.cloud_provider_var.get()
        instance_id = self.instance_id_entry.get()

        cloud_handler = CloudHandler(cloud_provider=cloud_provider)
        snapshot_id = cloud_handler.create_snapshot(instance_id)
        messagebox.showinfo("Snapshot Created", f"Snapshot ID: {snapshot_id}")

    def capture_memory_dump(self):
        target = self.ask_for_input("Enter Target OS (linux/windows):")
        output_path = filedialog.asksaveasfilename(defaultextension=".lime")
        
        memory_dump = MemoryDump()
        result = memory_dump.capture_memory_dump(output_path, target=target)
        analysis_result = memory_dump.analyze_dump(output_path)
        messagebox.showinfo("Memory Dump", f"{result}\n{analysis_result}")

    def capture_packets(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".pcap")
        iface = self.interface_entry.get()

        packet_capture = PacketCapture()
        result = packet_capture.capture_packets(iface, output_file)
        analysis_result = packet_capture.analyze_packets(output_file)
        messagebox.showinfo("Packet Capture", f"{result}\n{analysis_result}")

    def generate_report(self):
        findings = ["Snapshot created", "Memory dump captured and analyzed", "Packets captured and analyzed"]
        report_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        
        report_generator = ReportGenerator()
        self.report_generator.generate_report(findings, report_path)
        messagebox.showinfo("Report Generated", f"Report saved to {report_path}")

    def ask_for_input(self, prompt):
        return tk.simpledialog.askstring("Input", prompt)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = CyberForensicsApp()
    app.run()
