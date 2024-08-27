import subprocess
import os

class MemoryDump:
    def capture_memory_dump(self, output_path, target='linux'):
        if target == 'linux':
            # Install LiME and capture memory dump
            subprocess.run(["sudo", "apt-get", "install", "-y", "linux-headers-$(uname -r)", "gcc", "make"])
            subprocess.run(["git", "clone", "https://github.com/504ensicsLabs/LiME.git"])
            os.chdir("LiME/src")
            subprocess.run(["make"])
            subprocess.run([
                "sudo", "insmod", f"lime-$(uname -r).ko", f"path={output_path} format=lime"
            ])
            os.chdir("../../")
        elif target == 'windows':
            # Capture memory dump on Windows using WinPmem
            subprocess.run(["WinPmem.exe", "--output", output_path])
        return f"Memory dump saved to {output_path}"

    def analyze_dump(self, dump_file):
        # Analyze the memory dump using Volatility
        analysis_output = f"{dump_file}_analysis.txt"
        subprocess.run([
            "volatility", "-f", dump_file, "--profile=Win7SP1x64", "pslist", ">", analysis_output
        ], shell=True)
        return f"Memory analysis completed. Output saved to {analysis_output}"
