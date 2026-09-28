# AWS EC2 Linux Lab

## Mission Germany – AWS Hands-on Lab

### Objective

Hands-on practice of managing an Ubuntu Linux server running on Amazon EC2.

The lab focused on:

* Launching an EC2 instance
* Connecting to the server using SSH
* Understanding Linux system information
* Checking CPU, memory and disk resources
* Understanding IP addressing and routing
* Testing network connectivity and DNS
* Monitoring Linux processes
* Managing Linux services using `systemctl`
* Safely stopping the EC2 instance after the lab

---

## AWS Environment

| Item                 | Details                             |
| -------------------- | ----------------------------------- |
| AWS Region           | Europe (Frankfurt) – `eu-central-1` |
| Availability Zone    | `eu-central-1c`                     |
| Instance Name        | `Mission-Germany-EC2-Lab-01`        |
| Instance Type        | `t3.micro`                          |
| Operating System     | Ubuntu Server 26.04 LTS             |
| Architecture         | x86_64                              |
| Private IP           | `172.31.7.122`                      |
| Connection Method    | SSH                                 |
| Storage              | 8 GiB gp3                           |
| Final Instance State | Stopped                             |

---

## SSH Access

The EC2 instance was accessed from my local Ubuntu 24.04 virtual machine using SSH.

The private key was stored securely and its Linux permissions were restricted using:

```bash
chmod 600 ~/aws-key/mission-germany-key.pem
```

SSH connection:

```bash
ssh -i ~/aws-key/mission-germany-key.pem ubuntu@<EC2-PUBLIC-IP>
```

> The actual public IP and private key are intentionally not stored in this repository.

---

## Linux System Information

The following information was checked on the EC2 Ubuntu server:

* Hostname
* Current user
* Ubuntu version
* Linux kernel version
* CPU architecture
* CPU information
* Memory usage
* Disk usage

Commands used included:

```bash
hostname
whoami
cat /etc/os-release
uname -r
uname -m
lscpu
free -h
df -h /
```

---

## Linux Networking

The EC2 server's network configuration and connectivity were examined.

Topics practiced:

* Network interface
* Private IP address
* Default gateway
* Routing table
* Gateway connectivity
* Internet connectivity
* DNS resolution

Commands used:

```bash
ip addr
ip route
ping -c 4 172.31.0.1
ping -c 4 8.8.8.8
ping -c 4 google.com
resolvectl status
```

---

## Linux Process Monitoring

Linux processes were inspected using:

```bash
ps
ps aux
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
top
```

The practical covered:

* PID
* CPU usage
* Memory usage
* Running processes
* Process monitoring
* Understanding `systemd` as PID 1
* Checking system load

---

## Linux Service Management

The `cron` service was used to practice Linux service administration with `systemctl`.

Commands practiced:

```bash
systemctl status cron
systemctl is-enabled cron
systemctl is-active cron

sudo systemctl restart cron
sudo systemctl stop cron
sudo systemctl start cron

sudo systemctl disable cron
sudo systemctl enable cron
```

The practical demonstrated the difference between:

* `start` and `stop`
* `restart`
* `is-active`
* `enable` and `disable`

Important concept:

`stop` affects the current running service, while `disable` controls whether the service automatically starts during boot.

---

## Troubleshooting Experience

During the lab, EC2 Instance Connect initially failed.

The SSH connection was then established using the EC2 key pair from Windows.

A Windows private-key permission problem was encountered and resolved by restricting the `.pem` file permissions.

The key was subsequently transferred to the local Ubuntu VM through a VirtualBox shared folder and secured with:

```bash
chmod 600
```

The EC2 server was then successfully accessed from the Ubuntu VM.

---

## Security Practices

The following security practices were followed:

* Root MFA enabled
* No root access keys created
* IAM user used for lab work
* IAM user MFA enabled
* EC2 Security Group restricted SSH access to My IP
* Private SSH key permissions restricted
* Private key not uploaded to GitHub
* EC2 instance stopped after completing the lab

---

## Learning Outcomes

After completing this lab, I practiced:

1. Launching and accessing an AWS EC2 Linux server.
2. Connecting to a remote Linux server using SSH.
3. Troubleshooting SSH key permission issues.
4. Reading Linux system information.
5. Understanding basic Linux networking.
6. Testing gateway, Internet and DNS connectivity.
7. Monitoring Linux processes.
8. Managing Linux services with `systemctl`.
9. Understanding `start`, `stop`, `restart`, `enable` and `disable`.
10. Following basic AWS and SSH security practices.

---

## Status

**AWS EC2 Linux Lab: Completed**

The EC2 instance was stopped after completing the hands-on session.
