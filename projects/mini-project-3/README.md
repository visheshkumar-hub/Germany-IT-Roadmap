# 🇩🇪 Mini Project 3 — Office IT Infrastructure

## 🎯 Objective

Build a multi-department office network using multiple switches, VLANs, trunking, and Router-on-a-Stick inter-VLAN routing.

The project focused on:

* Multiple VLANs
* Access ports
* Switch-to-switch trunking
* Router-to-switch trunking
* Inter-VLAN Routing
* Server connectivity
* Network verification
* Troubleshooting

---

## 🏢 Departments

The office network contains three departments:

* HR
* IT
* Accounts

---

## 🖥️ Devices Used

| Device            | Quantity |
| ----------------- | -------: |
| Cisco Router 2911 |        1 |
| Cisco 2960 Switch |        2 |
| PCs               |        6 |
| Server            |        1 |

---

## 🌐 VLAN Design

| VLAN    | Department | Network         | Gateway      |
| ------- | ---------- | --------------- | ------------ |
| VLAN 10 | HR         | 192.168.10.0/24 | 192.168.10.1 |
| VLAN 20 | IT         | 192.168.20.0/24 | 192.168.20.1 |
| VLAN 30 | Accounts   | 192.168.30.0/24 | 192.168.30.1 |

---

## 🏗️ Network Architecture

```text id="7yq1lk"
                    Router
                      |
                 Trunk Link
                      |
                  Switch 1
                 /        \
           Access Ports    Trunk
             |              |
        HR / IT /       Switch 2
        Accounts        /       \
                     PCs       Server
```

---

## 🔀 VLAN Configuration

Three VLANs were created:

```text id="r4e6m0"
VLAN 10 → HR
VLAN 20 → IT
VLAN 30 → Accounts
```

PC ports were assigned to the appropriate VLANs.

---

## 🔗 Trunking

Trunk links were configured for carrying multiple VLANs.

The network included:

* Switch-to-switch trunk
* Router-to-switch trunk

The trunk links carried traffic for:

```text id="3b4j6p"
VLAN 10
VLAN 20
VLAN 30
```

---

## 🚦 Router-on-a-Stick

Router subinterfaces were configured to provide gateways for the three VLANs.

Conceptually:

```text id="5mzzd7"
Router
│
├── VLAN 10 → 192.168.10.1
├── VLAN 20 → 192.168.20.1
└── VLAN 30 → 192.168.30.1
```

802.1Q tagging was used to identify VLAN traffic.

---

## 🖥️ Server Connectivity

A server was included in the office network.

Connectivity between the server and the different network segments was tested as part of the practical lab.

---

## 🔍 Verification Commands

The following Cisco IOS commands were used:

```text id="j93s2g"
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

These commands were used to verify:

* VLAN creation
* Port assignments
* Trunk configuration
* Router interfaces
* Router subinterfaces
* Overall configuration

---

## 🧪 Connectivity Testing

The following connectivity tests were performed:

### Same VLAN

Devices within the same VLAN were tested using `ping`.

### Inter-VLAN

Communication between:

```text id="c9es6u"
HR ↔ IT
HR ↔ Accounts
IT ↔ Accounts
```

was tested through the router.

### Server

Connectivity between the server and network devices was also verified.

---

## 🛠️ Troubleshooting Method

When connectivity problems occurred, the following sequence was used:

1. Check whether the VLAN exists.
2. Verify the PC's access-port assignment.
3. Check switch-to-switch trunk.
4. Check router-to-switch trunk.
5. Verify router subinterfaces.
6. Verify VLAN IDs.
7. Check IP address and subnet mask.
8. Check default gateway.
9. Check interface status.
10. Test using `ping`.

This structured approach helped identify configuration problems instead of changing settings randomly.

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
* Cisco IOS commands
* Server connectivity
* Network troubleshooting

---

## 🏁 Project Outcome

This project expanded the previous two projects into a larger office network with multiple switches, three departments, a server, and inter-VLAN routing.

It provided practical experience with network segmentation, trunking, routing, verification, and troubleshooting.

---

## 🇩🇪 Mission Germany

This project is part of my **Mission Germany** practical IT journey.

The objective is to develop hands-on networking, troubleshooting, infrastructure, and documentation skills relevant to an IT career.
