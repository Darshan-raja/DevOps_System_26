

EC2 type T2 micro instance type instance is also viratul server

• General Purpose: Balanced CPU and memory (e.g., T2 micro)

• Compute Optimized: For intensive CPU tasks

• Memory Optimized: For memory-heavy applications

• Storage Optimized: For high storage performance

• Accelerated Computing: For specialized processing (e.g., GPUs)

when come to the security group 

** linux command for devops**
• ls: List files and directories
• cd: Change directory
• pwd: Print working directory
• cp: Copy files and directories
• mv: Move or rename files and directories
• rm: Remove files and directories
• mkdir: Create directories
• rmdir: Remove empty directories
• touch: Create empty files
• cat: Concatenate and display files
• head: Display the first few lines of a file
• tail: Display the last few lines of a file    
• grep: Search for text patterns in files
• find: Search for files and directories based on criteria
• chmod: Change file permissions
• chown: Change file ownership
• ps: Display running processes
• top: Display real-time process information
• kill: Terminate processes
• df: Display disk space usage
• du: Display directory size
• ifconfig: Display network interface information
• ping: Test network connectivity
• traceroute: Trace the route to a remote host
• netstat: Display network connections and routing tables
• ssh: Securely connect to remote hosts
• scp: Securely copy files between hosts
• crontab: Schedule tasks to run at specific times
• apt: Package manager for Debian-based distributions
• yum: Package manager for Red Hat-based distributions
• pip: Package manager for Python
• npm: Package manager for JavaScript
• git: Version control system


1. File and Directory Management
Command	Description	Example
ls	List directory contents	ls -l
cd	Change directory	cd /var/log
pwd	Print current path	pwd
mkdir	Create directory	mkdir project
touch	Create empty file	touch app.log
cp	Copy files/directories	cp file.txt /backup/
mv	Move or rename	mv old.log new.log
rm	Remove files/directories	rm -rf temp/
ln	Create hard/soft links	ln -s /opt/app app_link
1. Process and System Management
Command	Description	Example
ps	List running processes	`ps aux
top	Real-time system usage	top
kill	Terminate process	kill -9 1523
df	Disk usage	df -h
du	Folder/file size	du -sh /var/log
free	Memory usage	free -m
uname	System information	uname -a
lsof	Open files/processes	lsof -i :8080
1. Networking Commands
Command	Description	Example
wget	Download files	wget https://example.com/file.zip
curl	API calls & transfers	curl http://localhost:8080/health
ssh	Remote login	ssh ubuntu@3.110.10.20
scp	Secure copy	scp file.txt ubuntu@ip:/home/ubuntu/
ping	Check network connectivity	ping google.com
netstat	Network statistics	netstat -tulpn
ifconfig	Network interface config	ifconfig eth0
dig	DNS lookup	dig google.com
nc	Port checking / netcat	nc -zv 127.0.0.1 22
1. Permissions and User Management
Command	Description	Example
chmod	Change permissions	chmod 755 script.sh
chown	Change owner	chown ubuntu:ubuntu app.log
chgrp	Change group	chgrp developers file.txt
useradd	Create user	sudo useradd devops
passwd	Change password	sudo passwd devops
su	Switch user	su - devops
sudo	Run as root	sudo systemctl restart docker
usermod	Modify users	usermod -aG docker devops
groupadd	Create group	groupadd developers
id	Show user/group ID	id ubuntu
1. File Content & Logs (Important for DevOps)
Command	Description	Example
cat	View file	cat /etc/os-release
head	First lines	head -n 20 app.log
tail	Last lines	tail -f app.log
less	Scroll through file	less /var/log/syslog
grep	Search text	grep error app.log
awk	Field extraction	awk '{print $1}' data.txt
sed	Replace text	sed -i 's/old/new/g' file.txt
1. Systemctl (Service Management)

Most DevOps tools run as systemd services: Docker, Jenkins, Nginx, Kubelet, etc.

Command	Description	Example
systemctl start	Start service	systemctl start docker
systemctl stop	Stop service	systemctl stop nginx
systemctl restart	Restart service	systemctl restart jenkins
systemctl status	Status check	systemctl status docker
systemctl enable	Start on boot	systemctl enable docker