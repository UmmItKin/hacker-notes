### Nmap Output Formats

```bash
sudo nmap 10.129.2.28 -p- -oA target
```

Scans all ports on the target IP and saves output in three formats: normal (.nmap), grepable (.gnmap), and XML (.xml).

```
Normal output (-oN) with the .nmap file extension
Grepable output (-oG) with the .gnmap file extension
XML output (-oX) with the .xml file extension 
```

### Converting XML to HTML

```bash
xsltproc report.xml -o report.html
```

Converts the XML report to a readable HTML format.

### Common Nmap Scans

```bash
sudo nmap -p21 -sV --disable-arp-ping -n --packet-trace <IP>
```

```bash
sudo nmap -p80 <IP> --script discovery
```

```bash
sudo nmap -sV --top-ports 10 --disable-arp-ping <IP>
```

```bash
sudo nmap -Pn --disable-arp-ping -p53 -sU -sC <IP>
```

```bash
sudo nmap -g53 --max-retries=1 -Pn -p- --disable-arp-ping <IP>
```