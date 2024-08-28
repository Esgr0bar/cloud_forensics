# cloud_forensics IN DEV

## Overview
This repository provides a Python-based toolkit for performing cyber forensic investigations, particularly focusing on cloud environments like AWS, Azure, and GCP.

## Features
- **Cloud VM Snapshots**: Automatically create and manage snapshots of cloud VMs.
- **Memory Dump Analysis**: Capture and analyze memory dumps from various OS environments.
- **Packet Capture & Analysis**: Utilize Scapy for detailed network packet analysis.
- **Tool Integration**: Seamlessly integrate with Wireshark, MISP, and other security tools.
- **Cloud-Agnostic**: Easily switch between different cloud providers.

## Getting Started
### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  
### Running the Application:
Dependencies: Ensure that the required tools (TShark, Volatility, LiME, etc.) are installed and accessible from the system's PATH.
 
 ```bash
sudo apt-get install tshark volatility
```

### Start the Application:

```bash
python main.py
```
  
### Further Development:
- **Automation**: Add CI/CD pipelines for automated testing and deployment using GitHub Actions.
- **Advanced Analytics**: Incorporate AI/ML techniques for anomaly detection in captured data.
- **Customizable Dashboard**: Develop a web-based dashboard using Flask or Django for real-time monitoring and analysis.
