# 🇩🇪 Mini Project 5 — Company IT Infrastructure v2

## 🎯 Objective

Build and document an integrated company IT infrastructure combining networking, security, Linux, Python, AWS concepts, troubleshooting, and IT communication.

This project was designed as an integration project after completing the previous networking and infrastructure modules.

---

## 🏢 Company Network

The company contains three departments:

* HR
* IT
* Accounts

A server is also included in the internal network.

---

## 🏗️ Network Topology

```text id="w7n5xu"
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

---

## 🌐 VLAN Design

| VLAN    | Department | Network         | Gateway      |
| ------- | ---------- | --------------- | ------------ |
| VLAN 10 | HR         | 192.168.10.0/24 | 192.168.10.1 |
| VLAN 20 | IT         | 192.168.20.0/24 | 192.168.20.1 |
| VLAN 30 | Accounts   | 192.168.30.0/24 | 192.168.30.1 |

---

## 🔐 Security Policy

An ACL-based security policy was designed for internal communication.

| Traffic             | Policy  |
| ------------------- | ------- |
| HR → IT             | Blocked |
| IT → HR             | Blocked |
| HR → Server         | Allowed |
| IT → Server         | Allowed |
| Accounts → Server   | Allowed |
| Internal → Internet | Allowed |

### Important

If an HR device cannot ping an IT device because of the configured ACL policy, that failure is **expected behaviour**, not necessarily a network fault.

This was an important troubleshooting lesson: first determine whether the observed behaviour matches the intended security policy.

---

## 🖥️ Linux Administration Practice

Linux commands were used for basic system administration and troubleshooting.

```bash id="m4ut7x"
whoami
id
groups
ps aux
systemctl --type=service
ip addr
ping -c 4 192.168.20.1
```

These commands were used to inspect:

* Current user
* User and group information
* Running processes
* Services
* Network configuration
* Connectivity

---

## 🐍 Python Connectivity Check

A simple Python socket-based connectivity check was practiced.

```python id="x7j3f4"
import socket

host = "example.com"
port = 80

try:
    socket.create_connection((host, port), timeout=5)
    print("Server/Port is reachable")
except:
    print("Server/Port is not reachable")
```

The same concept can be used to test common service ports such as:

```text id="g8ckbw"
80   → HTTP
443  → HTTPS
22   → SSH
```

This introduced practical network automation and service connectivity checking.

---

## ☁️ AWS Conceptual Architecture

The company infrastructure was mapped to AWS concepts:

```text id="r1p5e2"
AWS
 │
 └── VPC
      │
      └── Subnet
           │
           └── EC2
                │
                └── Security Group
                     │
                     └── Application
```

### Concept Mapping

| IT Infrastructure     | AWS Concept          |
| --------------------- | -------------------- |
| Private cloud network | VPC                  |
| Network segment       | Subnet               |
| Cloud server          | EC2                  |
| Instance firewall     | Security Group       |
| Application           | Application workload |

This was a **conceptual architecture exercise**, not a claim of production AWS deployment.

---

## 🔍 Network Verification

Cisco IOS verification commands practiced during the project included:

```text id="3xy7w4"
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

These commands were used to verify:

* VLAN configuration
* Trunk status
* Router interfaces
* Network configuration

---

## 🛠️ Troubleshooting Scenarios

### Scenario A — PC Cannot Reach Gateway

Example:

```text id="6sj4kt"
PC1
IP: 192.168.10.10
Gateway: 192.168.10.1
```

Possible causes considered:

1. Incorrect IP address
2. Incorrect subnet mask
3. Incorrect default gateway
4. Switch port/VLAN problem
5. Router interface problem

---

### Scenario B — HR Cannot Reach IT

The first step is to determine whether the failure is intentional.

Because the project ACL policy blocks:

```text id="x1f0db"
HR → IT
```

the failed ping may represent **correct security behaviour**.

This reinforced the importance of checking security policies before treating a failed connection as a technical fault.

---

### Scenario C — EC2 Running but Application Is Not Reachable

Possible checks:

1. EC2 instance status
2. Security Group rules
3. Network configuration
4. Application/service status
5. Listening port
6. Route/network connectivity

---

### Scenario D — Linux Server Is Slow

A basic troubleshooting sequence:

```text id="q9h4sc"
Check processes
      ↓
Check memory
      ↓
Check disk usage
      ↓
Check services
      ↓
Check network
      ↓
Identify root cause
      ↓
Apply fix
      ↓
Verify
```

---

## 🧠 Troubleshooting Method

The general troubleshooting approach used throughout the project was:

```text id="u9x0xq"
Detect
  ↓
Collect Evidence
  ↓
Investigate
  ↓
Identify Root Cause
  ↓
Fix
  ↓
Verify
  ↓
Document
```

This approach is intended to prevent random configuration changes and encourage evidence-based troubleshooting.

---

## 🇬🇧 IT Communication Practice

The following interview-style question was practiced:

**Question: How would you troubleshoot a network connectivity problem?**

A structured answer should include:

1. Check physical connectivity.
2. Verify IP configuration.
3. Test the default gateway.
4. Test other network destinations.
5. Check VLAN, routing, firewall, or ACL configuration.
6. Identify the root cause.
7. Apply the fix and verify connectivity.

---

## 🇩🇪 German IT Vocabulary Practice

Technical German vocabulary practiced with the project included:

| English         | German      |
| --------------- | ----------- |
| Network         | Netzwerk    |
| IP address      | IP-Adresse  |
| Server          | Server      |
| Firewall        | Firewall    |
| Troubleshooting | Fehlersuche |
| Router          | Router      |
| Switch          | Switch      |
| User            | Benutzer    |
| Security        | Sicherheit  |

---

## 📚 Skills Integrated

### Networking

* VLAN
* Inter-VLAN Routing
* Routing
* ACL
* NAT/PAT
* Troubleshooting

### Linux

* Users and groups
* Processes
* Services
* Networking commands
* System troubleshooting

### Python

* Functions
* Socket connectivity
* Basic automation concepts

### AWS

* VPC
* Subnet
* EC2
* Security Group
* Cloud architecture concepts

### Security

* ACL
* Access control
* Network segmentation
* Security policy verification

### Communication

* IT troubleshooting explanation
* English IT vocabulary
* German IT vocabulary

---

## 🏁 Project Outcome

Mini Project 5 integrated multiple technologies into one practical company IT infrastructure scenario.

The project strengthened the ability to:

* Design a segmented network
* Apply security rules
* Verify configurations
* Troubleshoot connectivity
* Use Linux for system investigation
* Use Python for basic connectivity checking
* Map infrastructure concepts to AWS
* Explain technical problems in English
* Practice IT vocabulary in German
* Document technical work professionally

---

## 🇩🇪 Mission Germany

This project is part of **Mission Germany**, a long-term practical IT career transition journey.

The learning philosophy is:

> **Learn → Practice → Troubleshoot → Explain → Document → Assess → Repeat**

The goal is to develop practical, job-relevant IT skills for a future career in Germany.
