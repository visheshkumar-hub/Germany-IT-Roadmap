# AWS EC2 Linux Lab – Commands

This file records the commands actually practiced during the AWS EC2 Linux hands-on lab.

---

## 1. System Identity

```bash
hostname
```

```bash
whoami
```

Purpose:

* Check server hostname.
* Check the current Linux user.

---

## 2. Operating System and Kernel

```bash
cat /etc/os-release
```

```bash
uname -r
```

```bash
uname -m
```

Purpose:

* Identify Linux distribution and version.
* Check kernel version.
* Check CPU architecture.

---

## 3. CPU Information

```bash
lscpu | grep -E 'Model name|CPU\(s\)'
```

Purpose:

* Check number of CPUs.
* Check CPU model.

---

## 4. Memory and Disk

```bash
free -h
```

```bash
df -h /
```

Purpose:

* Check RAM and swap usage.
* Check root filesystem disk usage.

---

## 5. Network Interface

```bash
ip addr
```

Purpose:

* View network interfaces.
* Check IP addresses.
* Check MAC address.

---

## 6. Routing

```bash
ip route
```

Purpose:

* View the routing table.
* Identify the default gateway.
* Understand how traffic leaves the local network.

---

## 7. Gateway Connectivity

```bash
ping -c 4 172.31.0.1
```

Purpose:

* Test connectivity to the EC2 subnet gateway.

---

## 8. Internet Connectivity

```bash
ping -c 4 8.8.8.8
```

Purpose:

* Test Internet connectivity using an IP address.

---

## 9. DNS Testing

```bash
ping -c 4 google.com
```

Purpose:

* Test DNS name resolution and connectivity together.

---

## 10. DNS Configuration

```bash
resolvectl status
```

Purpose:

* Check the DNS server configured for the EC2 network interface.

---

## 11. Process Monitoring

```bash
ps
```

```bash
ps aux
```

```bash
ps aux --sort=-%cpu | head
```

```bash
ps aux --sort=-%mem | head
```

Purpose:

* View running processes.
* Check process IDs.
* Identify CPU and memory usage.

---

## 12. Live Process Monitoring

```bash
top
```

Press:

```text
q
```

to exit `top`.

Purpose:

* Monitor CPU usage.
* Monitor memory usage.
* Check system load.
* Observe running processes in real time.

---

## 13. Linux Services

List running services:

```bash
systemctl --type=service --state=running | head
```

Check cron service:

```bash
systemctl status cron
```

Check whether cron is running:

```bash
systemctl is-active cron
```

Check whether cron starts automatically at boot:

```bash
systemctl is-enabled cron
```

---

## 14. Restart Service

```bash
sudo systemctl restart cron
```

Verify:

```bash
systemctl is-active cron
```

Expected result:

```text
active
```

---

## 15. Stop and Start Service

Stop:

```bash
sudo systemctl stop cron
```

Check:

```bash
systemctl is-active cron
```

Expected:

```text
inactive
```

Start again:

```bash
sudo systemctl start cron
```

Verify:

```bash
systemctl is-active cron
```

Expected:

```text
active
```

---

## 16. Enable and Disable Service

Disable automatic startup:

```bash
sudo systemctl disable cron
```

Check:

```bash
systemctl is-enabled cron
```

Expected:

```text
disabled
```

The service can still be running after `disable`.

Enable automatic startup again:

```bash
sudo systemctl enable cron
```

Verify:

```bash
systemctl is-enabled cron
```

Expected:

```text
enabled
```

Final service state:

```text
enabled
active
```

---

## 17. SSH Key Security

On the local Ubuntu VM:

```bash
chmod 600 ~/aws-key/mission-germany-key.pem
```

Verify:

```bash
ls -l ~/aws-key/mission-germany-key.pem
```

Expected permission format:

```text
-rw-------
```

---

## 18. SSH Connection

From the local Ubuntu VM:

```bash
ssh -i ~/aws-key/mission-germany-key.pem ubuntu@<EC2-PUBLIC-IP>
```

The actual public IP is intentionally omitted from this documentation.

---

## Security Note

Never commit any of the following to GitHub:

* `.pem` private keys
* AWS access keys
* Secret keys
* Passwords
* Tokens
* Credentials

These should remain outside the repository.

---

## Lab Status

**Completed – AWS EC2 Linux Hands-on Lab**
