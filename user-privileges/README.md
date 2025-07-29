# Misconfiguration

## Basic Commands
- **Switch User to user2**:  
  ```bash
  sudo -u user2 /bin/bash
  ```

- **List User Privileges**:  
  ```bash
  sudo -l
  ```

### Networking Commands
- **Check Active Connections**:  
  ```bash
  netstat -antpl
  ```

- **Connect to Localhost on Port 80**:  
  ```bash
  nc localhost 80
  ```

### SSH Commands
- **SSH into localhost as root on port 80**:  
  ```bash
  ssh -i id_rsa root@localhost -p 80
  ```