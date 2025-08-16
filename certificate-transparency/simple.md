## Certificate Transparency (CT) logs

Certificate Transparency (CT) logs are public records of SSL/TLS certificates issued by Certificate Authorities (CAs). They help improve the security of the web by allowing anyone to monitor and audit the issuance of certificates, making it harder for malicious actors to use fraudulent certificates.

We can use tool like [crt.sh](https://crt.sh) to search for certificates issued by a specific CA or for a specific domain. This can help identify any unauthorized or misissued certificates

Rather than manually bruteforcing subdomains, plus we can use the CT logs to find subdomains that have been issued certificates.
