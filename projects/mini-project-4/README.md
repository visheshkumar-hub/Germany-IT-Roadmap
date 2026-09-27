# 🇩🇪 Mini Project 4 — Secure Company IT Network

## 🎯 Objective

Build a more secure company IT network by combining VLANs, access control, NAT/PAT, Linux system monitoring, Python automation, and AWS cloud concepts.

The project focused on:

* Network segmentation
* Access Control Lists (ACL)
* NAT/PAT
* Linux system checking
* Python automation
* AWS architecture mapping
* Troubleshooting
* IT documentation

---

## 🏢 Network Design

The company network contains two main departments:

* Management
* IT

---

## 🌐 VLAN Design

| VLAN    | Department | Network         | Gateway      |
| ------- | ---------- | --------------- | ------------ |
| VLAN 10 | Management | 192.168.10.0/24 | 192.168.10.1 |
| VLAN 20 | IT         | 192.168.20.0/24 | 192.168.20.1 |

---

## 🔐 Access Control List (ACL)

An ACL was used to control communication between network segments.

The project included testing traffic that should be:

* Allowed
* Blocked
* Verified through connectivity testing

The purpose was to understand how ACL rules can enforce network security policies.

---

## 🌍 NAT/PAT

NAT/PAT was practiced to understand how private internal addresses can communicate with an external network using address translation.

NAT translations were verified during the practical work.

---

## 🐧 Linux System Check

A Linux system-check script was created to collect basic system information.

```bash
#!/bin/bash

echo "===== System Check ====="

hostname
whoami
df -h
free -h
hostname -I
```

### Information Checked

* Hostname
* Current user
* Disk usage
* Memory usage
* IP address

---

## 🐍 Python IT Tool

Python was used to practice basic IT automation concepts.

Example:

```python
ips = [
    "192.168.10.10",
    "192.168.10.11",
    "192.168.20.10",
    "192.168.20.11"
]

for ip in ips:
    print("Checking:", ip)
```

This introduced the idea of using Python for repetitive IT and network-related tasks.

---

## ☁️ AWS Architecture Mapping

AWS concepts were mapped to the company's network infrastructure.

| Company Infrastructure  | AWS Concept    |
| ----------------------- | -------------- |
| Private company network | VPC            |
| Department network      | Subnet         |
| Server                  | EC2            |
| Instance firewall       | Security Group |
| Network-level filtering | NACL           |

### Conceptual Architecture

```text
AWS
 │
 └── VPC
      │
      ├── Subnet
      │    └── EC2
      │         └── Security Group
      │
      └── Network-level filtering
             └── NACL
```

This was a **conceptual AWS architecture exercise**, not a claim of production deployment.

---

## 🛠️ Troubleshooting Scenarios

The project included practical troubleshooting scenarios.

### Scenario 1 — PC Cannot Reach Gateway

Possible checks:

1. IP address
2. Subnet mask
3. Default gateway
4. Switch port
5. Router interface status

### Scenario 2 — Department Communication Fails

Possible checks:

1. VLAN configuration
2. Trunk
3. Router subinterface
4. Gateway
5. ACL rules

### Scenario 3 — Linux Server Is Slow

Possible checks:

1. CPU/processes
2. Memory
3. Disk usage
4. Network connectivity
5. Running services

---

## 🔍 Network Verification

Cisco verification commands included:

```text
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

Linux commands practiced included:

```bash
whoami
id
groups
ps aux
systemctl --type=service
ip addr
ping -c 4 192.168.20.1
```

---

## 📚 Skills Practiced

* VLANs
* Inter-VLAN Routing
* ACL
* NAT/PAT
* Linux administration basics
* Linux system monitoring
* Python basics
* IT automation concepts
* AWS VPC concepts
* EC2
* Security Groups
* NACL
* Troubleshooting
* Technical documentation

---

## 🏁 Project Outcome

This project connected networking, security, Linux, Python, and cloud concepts into one practical IT infrastructure exercise.

It provided experience in thinking about an IT environment as an integrated system rather than as separate technologies.

---

## 🇩🇪 Mission Germany

This project is part of my **Mission Germany** practical IT journey.

The focus is on developing practical infrastructure, security, automation, troubleshooting, and cloud knowledge for a future IT career in Germany.
