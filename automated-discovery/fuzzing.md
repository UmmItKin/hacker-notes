## Using FFUF for directory brute-forcing

```shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.161.31/FUZZ
```

### Add Host header to ffuf

```shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.207.231
```

### Filter by response size in ffuf

```shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.207.231 -fs {size}
```
## Using Dirb for directory brute-forcing

```shell
dirb http://10.10.161.31/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```

## Using Gobuster for directory brute-forcing

```shell
gobuster dir --url http://10.10.161.31/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```
