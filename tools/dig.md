# DNS Queries with `dig`

```shell
dig ns <domain.tld> @<nameserver
dig any <domain.tld> @<nameserver>
dig axfr <domain.tld> @<nameserver>
```

# DNS Enumeration with `dnsenum`

```shell
dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list <domain.tld> 	Subdomain brute forcing.
```
