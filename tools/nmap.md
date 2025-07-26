## Host Discovery with TTL and Nmap

Host discovery is a crucial step in network reconnaissance, allowing you to identify active hosts and gather information about them. Two common methods for host discovery are analyzing **TTL (Time To Live)** values and using network scanning tools like **nmap**. Below, we’ll explore both techniques in detail.

## Understanding TTL (Time To Live)

**TTL** is a timer value included in packets sent over networks that tells the recipient how long to hold or use the packet before discarding and expiring the data. Different operating systems set different default TTL values, which can be used to infer the OS of the target.

### Default TTL Values

| Operating System | Default TTL Value |
|------------------|-------------------|
| Windows          | 128               |
| Linux            | 64                |

### Determining the OS Based on TTL

determine the OS of a target by pinging an address and observing the TTL value in the response

1. **Ping the Target Address:**
   ```
   ping blog.ummit.dev
   ```

2. **Analyze the TTL Value:**
   The output will look something like this:
   ```
   PING blog.ummit.dev (104.21.77.210) 56(84) bytes of data.
   64 bytes from 104.21.77.210: icmp_seq=1 ttl=59 time=40.0 ms
   64 bytes from 104.21.77.210: icmp_seq=2 ttl=59 time=39.9 ms
   64 bytes from 104.21.77.210: icmp_seq=3 ttl=59 time=40.0 ms
   64 bytes from 104.21.77.210: icmp_seq=4 ttl=59 time=40.0 ms
   64 bytes from 104.21.77.210: icmp_seq=5 ttl=59 time=41.9 ms
   64 bytes from 104.21.77.210: icmp_seq=6 ttl=59 time=40.1 ms
   ```

3. **Interpret the TTL Value:**
   In the example above, the TTL value is **59**. Since Linux typically sets a default TTL of **64**, the target host is most likely running a Linux-based operating system.

---

## Using Nmap for Host Discovery

**nmap** is a powerful network scanning tool that can be used to discover hosts and services on a network. Here’s how you can use nmap for host discovery:

### Basic Host Discovery

Run the following command:

```bash
sudo nmap blog.ummit.dev -oA host -PE --packet-trace --disable-arp-ping

....

SENT (3.3380s) TCP 10.147.133.233:57209 > 172.67.211.196:5800 S ttl=37 id=60582 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3380s) TCP 10.147.133.233:57209 > 172.67.211.196:20005 S ttl=46 id=9154 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3380s) TCP 10.147.133.233:57209 > 172.67.211.196:990 S ttl=56 id=11487 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3380s) TCP 10.147.133.233:57209 > 172.67.211.196:9071 S ttl=57 id=50743 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3380s) TCP 10.147.133.233:57209 > 172.67.211.196:8100 S ttl=48 id=32947 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3381s) TCP 10.147.133.233:57209 > 172.67.211.196:5000 S ttl=56 id=12553 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3782s) TCP 10.147.133.233:57209 > 172.67.211.196:407 S ttl=45 id=27325 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3782s) TCP 10.147.133.233:57209 > 172.67.211.196:7007 S ttl=37 id=2149 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3782s) TCP 10.147.133.233:57209 > 172.67.211.196:10243 S ttl=45 id=29541 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3782s) TCP 10.147.133.233:57209 > 172.67.211.196:1045 S ttl=49 id=39365 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3803s) TCP 10.147.133.233:57209 > 172.67.211.196:5904 S ttl=43 id=63685 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3803s) TCP 10.147.133.233:57209 > 172.67.211.196:4446 S ttl=46 id=20452 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3803s) TCP 10.147.133.233:57209 > 172.67.211.196:8009 S ttl=48 id=37971 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3803s) TCP 10.147.133.233:57209 > 172.67.211.196:2004 S ttl=57 id=33946 iplen=44  seq=1010306950 win=1024 <mss 1460>
SENT (3.3803s) TCP 10.147.133.233:57209 > 172.67.211.196:1052 S ttl=57 id=8526 iplen=44  seq=1010306950 win=1024 <mss 1460>

...

SENT (5.5913s) TCP 10.147.133.233:57209 > 172.67.211.196:720 S ttl=53 id=52282 iplen=44  seq=1010306950 win=1024 <mss 1460>
Nmap scan report for blog.ummit.dev (172.67.211.196)
Host is up (0.040s latency).
Other addresses for blog.ummit.dev (not scanned): 104.21.77.210 2606:4700:3031::ac43:d3c4 2606:4700:3031::6815:4dd2
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
8080/tcp open  http-proxy
8443/tcp open  https-alt

Nmap done: 1 IP address (1 host up) scanned in 5.72 seconds
```
