# 🇩🇪 Mini Project 1 — Basic Network Foundation

## 🎯 Objective

Build and test a basic company network using a Cisco router, switch, and two PCs.

The main objective was to practice:

* IP addressing
* Default gateway
* Router interface configuration
* Basic LAN connectivity
* Ping testing
* Basic network troubleshooting

---

## 🏗️ Network Topology

```text
        Router
       192.168.1.1
            |
          Switch
         /      \
       PC1      PC2
   .10/24      .11/24
```

---

## 🖥️ Devices Used

| Device       | Quantity |
| ------------ | -------: |
| Cisco Router |        1 |
| Cisco Switch |        1 |
| PC           |        2 |

---

## 🌐 IP Addressing

| Device | IP Address   | Subnet Mask   | Default Gateway |
| ------ | ------------ | ------------- | --------------- |
| Router | 192.168.1.1  | 255.255.255.0 | —               |
| PC1    | 192.168.1.10 | 255.255.255.0 | 192.168.1.1     |
| PC2    | 192.168.1.11 | 255.255.255.0 | 192.168.1.1     |

Network: `192.168.1.0/24`

---

## ⚙️ Router Configuration

The router interface was configured with:

```text
IP Address: 192.168.1.1
Subnet Mask: 255.255.255.0
```

The interface was enabled using:

```text
no shutdown
```

---

## 🔍 Verification

The following Cisco commands were used for verification:

```text
show ip interface brief
show running-config
```

These commands were used to verify:

* Interface status
* IP address configuration
* Router configuration

---

## 🧪 Connectivity Testing

Ping tests were performed between:

```text
PC1 → Router
PC2 → Router
PC1 → PC2
```

Successful ping responses confirmed basic LAN connectivity.

---

## 🛠️ Troubleshooting Approach

When connectivity problems occurred, the following checks were considered:

1. Check IP address.
2. Check subnet mask.
3. Check default gateway.
4. Check router interface status.
5. Verify cable/port connectivity.
6. Test using `ping`.
7. Verify router configuration.

---

## 📚 Skills Practiced

* IPv4 addressing
* Subnet mask `/24`
* Default gateway
* Cisco router configuration
* Cisco switch basics
* Ping testing
* Basic network troubleshooting
* Cisco IOS verification commands

---

## 🏁 Project Outcome

This project established the foundation for the later Mission Germany networking projects.

It was followed by more advanced practical work involving:

* VLANs
* Trunking
* Inter-VLAN Routing
* ACL
* NAT/PAT
* Linux
* Python
* AWS

---

## 🇩🇪 Mission Germany

This project is part of my practical IT learning journey under **Mission Germany**, focused on developing job-ready networking, Linux, cloud, automation, troubleshooting, and communication skills for a future IT career in Germany.
