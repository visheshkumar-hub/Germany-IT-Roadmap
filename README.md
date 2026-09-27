# 🇩🇪 Germany IT Mission | Vishesh Kumar

### M.Tech (Computer Networks) | Networking & Linux | Python & AWS Learner | Future IT Support Engineer 🇩🇪

I have a background in Information Technology and Computer Networks.

I am building practical IT skills through hands-on labs, troubleshooting, projects, documentation, and continuous learning as part of my long-term **Mission Germany**.

---

## 👨‍💻 About Me

* 🎓 B.Tech in Information Technology
* 🎓 M.Tech in Computer Networks
* 🌐 Networking & IT Infrastructure
* 🐧 Linux / Ubuntu
* 🔧 Cisco Packet Tracer
* 🐍 Python for IT automation and networking
* ☁️ AWS Cloud fundamentals
* 🔐 Network security fundamentals
* 🔀 Git & GitHub
* 🇩🇪 Long-term goal: IT career in Germany

My current focus is on building **practical, job-oriented IT skills** rather than only collecting certificates.

---

# 🛠️ Core Skills

## 🌐 Networking

* TCP/IP
* OSI Model
* IPv4 Addressing
* Subnetting
* Binary & IP calculations
* MAC Address
* ARP
* Switching fundamentals
* VLANs
* VLAN Configuration
* Trunking
* 802.1Q
* Inter-VLAN Routing
* Router-on-a-Stick
* Static Routing
* Routing Tables
* Access Control Lists (ACL)
* NAT / PAT
* NAT Translation
* DHCP fundamentals
* DNS fundamentals
* Basic DHCP/DNS troubleshooting
* Network Connectivity Testing
* Network Troubleshooting

### Cisco Practice

* Cisco Routers
* Cisco Switches
* Interface configuration
* VLAN configuration
* Trunk configuration
* Router-on-a-Stick
* ACL configuration
* NAT/PAT concepts
* Routing verification
* Connectivity testing using `ping`
* Troubleshooting with verification commands

---

## 🐧 Linux

### Ubuntu / Linux Fundamentals

* Ubuntu Linux
* Linux Command Line
* Files & Directories
* File Management
* Permissions
* `chmod`
* Users & Groups
* `useradd`
* `passwd`
* `usermod`
* `groups`
* `whoami`
* `id`
* File Ownership
* `chown`
* Processes
* `ps`
* `top`
* `kill`
* Services
* `systemctl`
* Basic Linux Networking
* System Monitoring
* Basic Shell Scripting

---

## 🐍 Python

### Python Fundamentals

* Variables
* Conditions
* Loops
* Functions
* Parameters & Arguments
* Return Values
* File Handling
* Text / CSV File Processing
* Basic Automation
* `os`
* `socket`
* Network Connectivity Checks
* Basic IT troubleshooting automation

Python is currently being developed as a practical tool for **IT support, system monitoring, networking and automation**.

---

## ☁️ AWS / Cloud

### AWS Fundamentals

* Cloud Computing Concepts
* AWS Fundamentals
* Amazon EC2
* EC2 Instances
* AMI
* Instance Types
* Key Pairs
* Security Groups
* VPC Fundamentals
* Subnets
* Route Tables
* Internet Gateway
* Basic AWS Networking
* Cloud Architecture Concepts
* AWS Infrastructure Troubleshooting Concepts

> AWS architecture in the current projects is primarily **conceptual / learning-based** unless explicitly marked as deployed.

---

## 🔐 Security Fundamentals

* Network ACL concepts
* Cisco ACL
* Linux File Permissions
* File Ownership
* AWS Security Groups
* NAT/PAT security concepts
* Basic Network Access Control
* Authentication & Authorization concepts
* Least Privilege concept
* Basic network security troubleshooting

---

## 🖥️ IT Support & Troubleshooting

I am developing a structured troubleshooting approach:

**Detect → Collect Evidence → Investigate → Identify Root Cause → Fix → Verify → Document**

Practical troubleshooting areas include:

* Network connectivity
* VLAN communication
* Routing
* ACL restrictions
* NAT/PAT
* Linux system checks
* Processes and services
* Server connectivity
* Python connectivity testing
* AWS infrastructure concepts

---

# 🏆 Practical Networking Projects

## Mini Project 1 — Basic Network Foundation

### Objective

Build and verify a basic network.

### Work Completed

* Router
* Switch
* PCs
* IP Address Configuration
* Default Gateway
* Basic Connectivity Testing
* Ping Verification

---

## Mini Project 2 — Company Department Network

### Scenario

A company network with separate departments.

### Departments

* HR
* IT

### Work Completed

* VLAN 10 — HR
* VLAN 20 — IT
* VLAN creation
* Switch port assignment
* Router & Switch configuration
* Connectivity testing
* VLAN troubleshooting
* `show vlan brief`

---

## Mini Project 3 — Office IT Infrastructure

### Scenario

Design an office network with multiple departments.

### Infrastructure

* Cisco Router 2911
* Cisco 2960 Switches
* 6 PCs
* Server

### VLAN Design

* VLAN 10 — HR
* VLAN 20 — IT
* VLAN 30 — Accounts

### Technologies Practiced

* VLANs
* Trunking
* 802.1Q
* Router-on-a-Stick
* Inter-VLAN Routing
* IP Addressing
* Connectivity Testing
* Network Troubleshooting

### Verification

* `show vlan brief`
* `show ip interface brief`
* Ping testing

---

# 🔐 Mini Project 4 — Secure Company IT Network

### Scenario

Build a small company network with basic security controls.

### Technologies

* Cisco Networking
* VLANs
* ACL
* NAT/PAT
* Linux
* Python
* AWS Architecture
* Network Security

### Security Design

* Department-level network separation
* ACL-based traffic control
* NAT/PAT
* Linux permissions
* AWS Security Group concepts
* Network-level access control

### Linux System Check

```bash
#!/bin/bash

echo "===== System Check ====="

hostname
whoami
df -h
free -h
hostname -I
```

### Python Networking Practice

Python was used to understand basic connectivity testing and network-oriented automation concepts.

---

# 🚀 Mini Project 5 — Company IT Infrastructure v2

### Objective

Integrate networking, Linux, Python, AWS concepts, security and troubleshooting into one practical company IT infrastructure project.

### Network Design

```text
                    INTERNET
                       |
                    ROUTER
                       |
                    SWITCH
              _________|_________
             |         |         |
          VLAN 10   VLAN 20   VLAN 30
             |         |         |
            HR         IT      Accounts
             |         |         |
            PCs       PCs       PCs
                       |
                    SERVER
```

### VLAN Plan

| VLAN | Department | Network         | Gateway      |
| ---- | ---------- | --------------- | ------------ |
| 10   | HR         | 192.168.10.0/24 | 192.168.10.1 |
| 20   | IT         | 192.168.20.0/24 | 192.168.20.1 |
| 30   | Accounts   | 192.168.30.0/24 | 192.168.30.1 |

### Security Policy

* HR → IT: Blocked
* IT → HR: Blocked
* HR → Server: Allowed
* IT → Server: Allowed
* Accounts → Server: Allowed
* Internal → Internet: Allowed

### Linux Practice

* Users & Groups
* Processes
* Services
* IP Address
* Connectivity Testing
* System Monitoring

### Python Practice

* Socket connectivity
* Port testing
* Basic network health checking
* IT automation concepts

Example ports tested:

* 22 — SSH
* 80 — HTTP
* 443 — HTTPS

### AWS Architecture

```text
AWS
 |
VPC
 |
Subnet
 |
EC2
 |
Security Group
 |
Application
```

This project helped connect traditional networking concepts with cloud infrastructure concepts.

---

# 🧰 Tools & Technologies

### Networking

* Cisco Packet Tracer
* Cisco Routers
* Cisco Switches

### Operating Systems

* Ubuntu Linux

### Programming

* Python
* Bash

### Cloud

* AWS

### Version Control

* Git
* GitHub

---

# 📚 Current Learning Roadmap

My structured IT learning roadmap covers:

* 🌐 Networking
* 🐧 Linux
* 🖥️ IT Support
* 🐍 Python
* ☁️ AWS / Cloud
* 🔐 Cybersecurity Fundamentals
* 🔀 Git & GitHub
* ⚙️ DevOps Foundations
* 🗄️ SQL
* 🇬🇧 English IT Communication
* 🇩🇪 German Language

The roadmap is focused on:

**Learn → Practice → Troubleshoot → Explain → Document → Assess → Improve**

---

# 🇩🇪 Mission Germany

My long-term goal is to become **job-ready for an IT Support, Network Support, IT Infrastructure, or related technical role in Germany**.

I am building toward this goal through:

* Practical networking labs
* Linux administration
* Python automation
* Cloud fundamentals
* Security fundamentals
* Troubleshooting
* Realistic IT projects
* GitHub documentation
* English IT communication
* German language learning

### Core Principle

> **Skills + Practical Work + Projects + Troubleshooting + Communication + German = Job Readiness**

---

# 📈 Current Focus

### Strong Foundation

* Networking fundamentals
* VLANs
* Inter-VLAN Routing
* Router-on-a-Stick
* ACL
* NAT/PAT
* Basic troubleshooting

### Developing

* Linux Administration
* Python
* AWS / Cloud
* Security
* IT Support
* Git & GitHub

### Building Next

* Advanced Linux Administration
* AWS VPC & Cloud Networking
* IAM
* Python Automation
* Advanced Troubleshooting
* Real-world Infrastructure Projects

---

# 🎯 My Learning Philosophy

I believe in **learning by doing**.

For every major topic, I try to follow:

**Learn → Lab → Troubleshoot → Build → Document → Improve**

My goal is not simply to know concepts, but to understand how they work in a practical IT environment.

---

## ⭐ Thanks for visiting my profile!

### Future IT Support Engineer | Networking | Linux | Cloud | Germany 🇩🇪
