

EC2 type T2 micro instance type instance is also viratul server

• General Purpose: Balanced CPU and memory (e.g., T2 micro)

• Compute Optimized: For intensive CPU tasks

• Memory Optimized: For memory-heavy applications

• Storage Optimized: For high storage performance

• Accelerated Computing: For specialized processing (e.g., GPUs)

when come to the security group

** linux command for devops**
# Linux Commands for DevOps (Fresher-Friendly Guide)

This file contains all essential Linux commands a DevOps fresher must know, explained simply with **two examples each**.

---

## 1. `ls` – List files and directories

**Example 1:** `ls`
**Example 2:** `ls -l`

## 2. `sudo` – Run command as root

**Example 1:** `sudo apt update`
**Example 2:** `sudo systemctl restart nginx`

## 3. `cd` – Change directory

**Example 1:** `cd /var/log`
**Example 2:** `cd ..`

## 4. `pwd` – Print working directory current working

**Example 1:** `pwd`
**Example 2:** `echo $(pwd)`

## 5. `cp` – Copy files/directories

**Example 1:** `cp file.txt backup.txt`
**Example 2:** `cp -r /data /backup/`

## 6. `mv` – Move or rename

**Example 1:** `mv old.log new.log`
**Example 2:** `mv /tmp/app /opt/app/`

## 7. `rm` – Remove files/directories

**Example 1:** `rm error.log`
**Example 2:** `rm -rf /tmp/cache/`

## 8. `ln` – Create links

**Example 1:** `ln -s /opt/app/config config_link`
**Example 2:** `ln file1.txt file2.txt`

## 9. `mkdir` – Create directory

**Example 1:** `mkdir logs`
**Example 2:** `mkdir -p /opt/app/release/v1`

## 10. `rmdir` – Remove empty directories

**Example 1:** `rmdir temp`
**Example 2:** `rmdir old_backup`

## 11. `touch` – Create empty files

**Example 1:** `touch app.log`
**Example 2:** `touch notes.txt`

## 12. `cat` – View file content

**Example 1:** `cat app.log`
**Example 2:** `cat /etc/os-release`

## 13. `head` – Display first few lines

**Example 1:** `head app.log`
**Example 2:** `head -n 20 system.log`

## 14. `tail` – Display last few lines

**Example 1:** `tail app.log`
**Example 2:** `tail -f app.log`

## 15. `grep` – Search text

**Example 1:** `grep "error" app.log`
**Example 2:** `grep -R "port" /etc/`

## 16. `find` – Search for files

**Example 1:** `find /var/log -name "*.log"`
**Example 2:** `find /home -size +10M`

## 17. `chmod` – Change permissions

**Example 1:** `chmod 755 script.sh`
**Example 2:** `chmod 644 file.txt`

## 18. `chown` – Change file ownership

**Example 1:** `chown ubuntu:ubuntu file.txt`
**Example 2:** `chown -R jenkins:jenkins /var/jenkins_home`

## 19. `ps` – Show running processes

**Example 1:** `ps aux`
**Example 2:** `ps aux | grep nginx`

## 20. `top` – Live resource usage

**Example 1:** `top`
**Example 2:** `top -o %CPU`

## 21. `kill` – Terminate process

**Example 1:** `kill 1234`
**Example 2:** `kill -9 5678`

## 22. `df` – Disk usage

**Example 1:** `df -h`
**Example 2:** `df -T`

## 23. `du` – Folder size

**Example 1:** `du -sh /var/log`
**Example 2:** `du -ah /opt/app | head`

## 24. `ifconfig` / `ip` – Network info

**Example 1:** `ifconfig`
**Example 2:** `ip addr show`

## 25. `ping` – Test network connectivity

**Example 1:** `ping google.com`
**Example 2:** `ping 8.8.8.8`

## 26. `traceroute` – Trace path

**Example 1:** `traceroute google.com`
**Example 2:** `traceroute 8.8.8.8`

## 27. `netstat` – Show ports & connections

**Example 1:** `netstat -tulpn`
**Example 2:** `netstat -an | grep 8080`

## 28. `ssh` – Login into a server

**Example 1:** `ssh ubuntu@3.110.10.20`
**Example 2:** `ssh -i key.pem ec2-user@IP`

## 29. `scp` – Copy files between servers

**Example 1:** `scp file.txt ubuntu@server:/opt/`
**Example 2:** `scp -i key.pem app.zip ec2-user@IP:/home/ec2-user/`

## 30. `crontab` – Schedule tasks

**Example 1:** `crontab -e`
**Example 2:** `0 3 * * * /opt/backup.sh`

## 31. `apt` – Package manager (Debian/Ubuntu)

**Example 1:** `sudo apt install nginx`
**Example 2:** `sudo apt update`

## 32. `yum` – Package manager (RHEL/CentOS)

**Example 1:** `sudo yum install git`
**Example 2:** `sudo yum update -y`

## 33. `pip` – Python package manager

**Example 1:** `pip install boto3`
**Example 2:** `pip install flask`

## 34. `npm` – JavaScript package manager

**Example 1:** `npm install`
**Example 2:** `npm run build`

## 35. `git` – Version control

**Example 1:** `git clone repo-url`
**Example 2:** `git commit -m "updated config"`

## 36. `curl` – API calls / downloads

**Example 1:** `curl http://localhost:8080/health`
**Example 2:** `curl -O https://example.com/file.zip`

## 37. `wget` – Download files

**Example 1:** `wget https://example.com/app.tar.gz`
**Example 2:** `wget -c resume.pdf`

## 38. `tar` – Compress/uncompress

**Example 1:** `tar -czvf backup.tar.gz /opt/app`
**Example 2:** `tar -xzvf backup.tar.gz`

## 39. `zip` – Compress

**Example 1:** `zip logs.zip *.log`
**Example 2:** `zip -r project.zip project/`

## 40. `unzip` – Extract zip files

**Example 1:** `unzip backup.zip`
**Example 2:** `unzip -l backup.zip`

## 41. `vim` – Edit text files

**Example 1:** `vim app.conf`
**Example 2:** `vim /etc/nginx/nginx.conf`

## 42. `nano` – Simple text editor

**Example 1:** `nano app.conf`
**Example 2:** `nano deploy.yaml`

## 43. `awk` – Extract fields & analyze text

**Example 1:** `awk '{print $1}' users.txt`
**Example 2:** `awk '/ERROR/' app.log`

## 44. `sed` – Replace/edit text

**Example 1:** `sed -i 's/old/new/' file.txt`
**Example 2:** `sed '1,10d' log.txt`




---


Tell me anytime!





 # Linux Commands Cheat Sheet (DevOps Friendly)

## 1. File and Directory Management

| Command | Description | Example |
|--------|-------------|---------|
| `ls` | List directory contents | `ls -l` |
| `cd` | Change directory | `cd /var/log` |
| `pwd` | Print current path | `pwd` |
| `mkdir` | Create directory | `mkdir project` |
| `touch` | Create empty file | `touch app.log` |
| `cp` | Copy files/directories | `cp file.txt /backup/` |
| `mv` | Move or rename | `mv old.log new.log` |
| `rm` | Remove files/directories | `rm -rf temp/` |
| `ln` | Create hard/soft links | `ln -s /opt/app app_link` |
        'ln -ltr' app_link # to see the target of the link

---

## 2. Process and System Management

| Command | Description | Example |
|--------|-------------|---------|
| `ps` | List running processes | `ps aux` |
| `top` | Real-time system usage | `top` |
| `kill` | Terminate a process | `kill -9 1523` |
| `df` | Disk usage | `df -h` |
| `du` | Folder/file size | `du -sh /var/log` |
| `free` | Memory usage | `free -m` |
| `uname` | System information | `uname -a` |
| `lsof` | Open files/processes | `lsof -i :8080` |

---

## 3. Networking Commands

| Command | Description | Example |
|--------|-------------|---------|
| `wget` | Download files | `wget https://example.com/file.zip` |
| `curl` | API calls & transfers | `curl http://localhost:8080/health` |
| `ssh` | Remote login | `ssh ubuntu@3.110.10.20` |
| `scp` | Secure copy | `scp file.txt ubuntu@ip:/home/ubuntu/` |
| `ping` | Check network connectivity | `ping google.com` |
| `netstat` | Network statistics | `netstat -tulpn` |
| `ifconfig` | Network interface config | `ifconfig eth0` |
| `dig` | DNS lookup | `dig google.com` |
| `nc` | Port checking / netcat | `nc -zv 127.0.0.1 22` |

---

## 4. Permissions and User Management

| Command | Description | Example |
|--------|-------------|---------|
| `chmod` | Change permissions | `chmod 755 script.sh` |
| `chown` | Change owner | `chown ubuntu:ubuntu app.log` |
| `chgrp` | Change group | `chgrp developers file.txt` |
| `useradd` | Create user | `sudo useradd devops` |
| `passwd` | Change password | `sudo passwd devops` |
| `su` | Switch user | `su - devops` |
| `sudo` | Run as root | `sudo systemctl restart docker` |
| `usermod` | Modify users | `usermod -aG docker devops` |
| `groupadd` | Create group | `groupadd developers` |
| `id` | Show user/group ID | `id ubuntu` |

---

## 5. File Content & Logs

| Command | Description | Example |
|--------|-------------|---------|
| `cat` | View file | `cat /etc/os-release` |
| `head` | First lines | `head -n 20 app.log` |
| `tail` | Last lines (live) | `tail -f app.log` |
| `less` | Scroll through file | `less /var/log/syslog` |
| `grep` | Search text | `grep error app.log` |
| `awk` | Field extraction | `awk '{print $1}' data.txt` |
| `sed` | Replace text | `sed -i 's/old/new/g' file.txt` |

---

## 6. Systemctl (Service Management)

| Command | Description | Example |
|--------|-------------|---------|
| `systemctl start` | Start service | `systemctl start docker` |
| `systemctl stop` | Stop service | `systemctl stop nginx` |
| `systemctl restart` | Restart service | `systemctl restart jenkins` |
| `systemctl status` | Status check | `systemctl status docker` |
| `systemctl enable` | Start on boot | `systemctl enable docker` |

---

## 7. Package Management

| Command | Description | Example |
|--------|-------------|---------|
| `apt-get` | Debian/Ubuntu | `apt-get install nginx` |
| `yum` | CentOS/RHEL | `yum install httpd` |
| `dnf` | Fedora | `dnf install docker` |
| `rpm` | RPM packages | `rpm -i package.rpm` |
| `pip` | Python packages | `pip install requests` |
| `gem` | Ruby gems | `gem install rails` |


---

## 8. Other Commands

| Command | Description | Example |
|--------|-------------|---------|
| `tar` | Archive files | `tar -czvf archive.tar.gz /path/to/files` |
| `gzip` | Compress files | `gzip file.txt` |
| `unzip` | Extract zip files | `unzip archive.zip` |

interive questions

hard link and soft link

types of deployment
public
private
hybrid

IAAS (Infrastructure-as-a-Service) example : AWS EC2
PAAS (Platform-as-a-Service)example : Heroku, AWS Lambda, Azure Functions, Google Cloud Functions, IBM Cloud Functions, OpenFaaS
SAAS (Software-as-a-Service) xample : Google Docs, Slack, GitHub, Salesforce,
FaaS (Function-as-a-Service) : AWS Lambda, Azure Functions, Google Cloud Functions, IBM Cloud Functions, OpenFaaS
BaaS (Backend-as-a-Service) : Firebase, AWS Amplify, Google Firebase, Microsoft Azure, IBM Cloud, Oracle Cloud, SAP Cloud Platform

