## Local file inclusion (LFI)

Local File Inclusion (LFI) is a type of vulnerability that allows an attacker to include files on a server through the web browser. This can lead to unauthorized access to sensitive files and potentially remote code execution (RCE).

As many server for the example, the root directory is `/var/www/html/` and the web server user is `www-data`. Normally we're access to the files with web root directory (`/var/www/html/`) and the web server user (`www-data`) has read access to the files in this directory.

But watch out, if the application allows you to include files from outside the web root directory, it can lead to LFI vulnerabilities. This also known as `dot-dot-slash` attack, where an attacker can traverse the directory structure using `../` to access files outside the intended directory.

This simple example shows how an attacker can exploit LFI to read sensitive files:

```shell
http://thewebsite.com/file.php?file=../../../../etc/passwd
```

This request attempts to read the `/etc/passwd` file, which contains user account information on Unix-like systems. If the application does not properly validate or sanitize the input, it may allow the attacker to read this file.

## Bypassing File Inclusion Filters

To exploit LFI vulnerabilities, attackers often try to bypass file inclusion filters that may be in place. Here are some common techniques:
