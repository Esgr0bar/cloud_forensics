from setuptools import setup, find_packages

setup(
    name="cyber_forensics_toolkit",
    version="1.0.0",
    description="A Python toolkit for cyber forensics across multiple cloud platforms.",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "azure-identity",
        "azure-mgmt-compute",
        "google-cloud-compute",
        "scapy",
        "volatility3",
        "reportlab",
        "tkinter"
    ],
    entry_points={
        'console_scripts': [
            'cyber_forensics_toolkit=main:main',
        ],
    },
    python_requires='>=3.8',
)
