## Using FFUF for directory brute-forcing

```shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.161.31/FUZZ
```

## Using Dirb for directory brute-forcing

```shell
dirb http://10.10.161.31/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```
## Using Gobuster for directory brute-forcing

```shell
gobuster dir --url http://10.10.161.31/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```
