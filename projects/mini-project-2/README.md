# 🇩🇪 Mini Project 2 — Company Department Network

## 🎯 Objective

Build a company department network using VLANs and configure communication between different departments.

The project focused on:

* VLAN creation
* VLAN port assignment
* Trunking
* Inter-VLAN communication
* Router-on-a-Stick
* Connectivity testing
* Network troubleshooting

---

## 🏢 Departments

The company network contains two departments:

* HR
* IT

---

## 🖥️ Devices Used

| Device       | Quantity |
| ------------ | -------: |
| Cisco Router |        1 |
| Cisco Switch |        1 |
| PCs          |        4 |

---

## 🌐 VLAN Design

| VLAN    | Department | Network         | Gateway      |
| ------- | ---------- | --------------- | ------------ |
| VLAN 10 | HR         | 192.168.10.0/24 | 192.168.10.1 |
| VLAN 20 | IT         | 192.168.20.0/24 | 192.168.20.1 |

### PC Addressing

| Device | Department | IP Address    | Gateway      |
| ------ | ---------- | ------------- | ------------ |
| PC1    | HR         | 192.168.10.10 | 192.168.10.1 |
| PC2    | HR         | 192.168.10.11 | 192.168.10.1 |
| PC3    | IT         | 192.168.20.10 | 192.168.20.1 |
| PC4    | IT         | 192.168.20.11 | 192.168.20.1 |

---

## ⚙️ VLAN Configuration

Two VLANs were created on the Cisco switch:

```text
VLAN 10 → HR
VLAN 20 → IT
```

PC ports were assigned to their respective VLANs.

---

## 🔗 Trunking

A trunk link was configured between the switch and router.

The trunk carries traffic for:

```text
VLAN 10
VLAN 20
```

---

## 🚦 Router-on-a-Stick

Router subinterfaces were used to provide gateways for the two VLANs.

Conceptually:

```text
Router
│
├── Subinterface → VLAN 10 → 192.168.10.1
│
└── Subinterface → VLAN 20 → 192.168.20.1
```

802.1Q VLAN tagging was used for the subinterfaces.

---

## 🔍 Verification Commands

The following Cisco IOS commands were used:

```text
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

These commands were used to verify:

* VLAN creation
* Port assignments
* Trunk status
* Router interface/subinterface status
* Configuration

---

## 🧪 Connectivity Testing

Connectivity was tested within and between VLANs.

Examples:

```text
PC1 → PC2
PC3 → PC4
PC1 → PC3
PC2 → PC4
```

Successful inter-VLAN communication confirmed that Router-on-a-Stick was functioning correctly.

---

## 🛠️ Troubleshooting

During practical testing, connectivity issues were investigated using a structured approach:

1. Check whether the VLAN exists.
2. Check the PC's switch port assignment.
3. Check trunk configuration.
4. Check router subinterfaces.
5. Verify VLAN IDs.
6. Verify IP address and subnet mask.
7. Verify default gateway.
8. Check interface status.
9. Test connectivity using `ping`.

---

## 📚 Skills Practiced

* VLAN configuration
* Access ports
* Trunking
* 802.1Q
* Router-on-a-Stick
* Inter-VLAN Routing
* IPv4 addressing
* Default gateways
* Cisco IOS verification
* Network troubleshooting

---

## 🏁 Project Outcome

This project moved the network from a basic single-LAN setup to a segmented departmental network.

It provided practical experience with VLAN-based network segmentation and communication between different departments.

---

## 🇩🇪 Mission Germany

This project is part of my **Mission Germany** practical IT journey.

The focus is on building real-world networking and troubleshooting skills rather than learning only theoretical concepts.
