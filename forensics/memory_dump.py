import subprocess
import os

class MemoryDump:
    def capture_memory_dump(self, output_path, target='linux'):
        if target.lower() == 'linux':
            # Install necessary tools and capture memory dump using LiME
            subprocess.run(["sudo", "apt-get", "install", "-y", "linux-headers-$(uname -r)", "gcc", "make"])
            subprocess.run(["git", "clone", "https://github.com/504ensicsLabs/LiME.git"])
            os.chdir("LiME/src")
            subprocess.run(["make"])
            subprocess.run([
                "sudo", "insmod", f"lime-$(uname -r).ko", f"path={output_path}", "format=lime"
            ])
            os.chdir("../../")
        elif target.lower() == 'windows':
            # Capture memory dump on Windows using WinPmem
            if not os.path.exists("WinPmem.exe"):
                raise FileNotFoundError("WinPmem.exe not found. Please ensure it is in the working directory.")
            subprocess.run(["WinPmem.exe", "--output", output_path])
        else:
            raise ValueError("Unsupported target OS. Please use 'linux' or 'windows'.")
        
        return f"Memory dump saved to {output_path}"

    def analyze_dump(self, dump_file, profile='Win7SP1x64'):
        # Analyze the memory dump using Volatility
        analysis_output = f"{dump_file}_analysis.txt"
        subprocess.run([
            "volatility", "-f", dump_file, "--profile", profile, "pslist", ">", analysis_output
        ], shell=True)
        return f"Memory analysis completed. Output saved to {analysis_output}"
