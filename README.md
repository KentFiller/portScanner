# Port Scanner

## Description

This repository documents my journey in practicing cybersecurity concepts through the development of a Python port scanner. The project aims to gain experience in network security by creating a tool capable of scanning for open ports on a given IP address. Port scanning is a common technique used in cybersecurity to identify potential vulnerabilities in networked systems.

## Languages and Utilities Used

- Made using Python

## Environments Used

- VSCode

## How It Works

The Python port scanner uses the `socket` module to create a socket and attempt to connect to a specified IP address and port. Here's how it works:

1. **Socket Creation**: The script creates a TCP socket using the `socket.socket()` function from the `socket` module.

2. **Input**: The user is prompted to enter the IP address and port they want to scan.

3. **Port Scanning**: The script attempts to connect to the specified IP address and port using the `connect_ex()` function. If the connection is successful, the port is considered open; otherwise, it is considered closed.

4. **Output**: The script prints whether the port is open or closed based on the result of the connection attempt.

## Steps Taken

1. **Specify IP and Port**: Enter the IP address and port number you want to scan when prompted by the script.

2. **Run the Script**: Execute the Python script and follow the on-screen prompts to initiate the port scanning process.

## Example

```python
Enter the IP you want to scan: 137.74.187.104
Enter the Port you want to scan: 443
The Port is Open
```

## Potential Misuse by Threat Actors

While this port scanning tool is intended for educational purposes and ethical use, it's essential to consider potential misuse scenarios by threat actors:

- **Reconnaissance**: Threat actors can use (more sophisticated) port scanning tools like the one here to identify open ports on target systems as part of reconnaissance activities for potential cyber attacks.

- **Vulnerability Assessment**: By scanning for open ports, threat actors can assess the security posture of target systems and identify potential weak points that could be exploited.

- **Exploitation**: Once open ports are identified, threat actors are going to attempt to exploit known vulnerabilities connected with specific services running on those ports, making them gain unauthorized access or disrupt system functionality.

## Disclaimer

The main objective of this project is to deepen my understanding of cybersecurity concepts, particularly, im trying my hand at getting inside the mindset of an attacker, and port scanning is one of the tools they use. 
I also wish to gain real world practical experience in the field by implementing this tool in Python, reinforcing theoretical knowledge with practical application.
An important thing to note is that this tool is intended for educational purposes only. I do not endorse or encourage unauthorized access or malicious activities. Always ensure that port scanning activities are conducted ethically and with proper authorization.

