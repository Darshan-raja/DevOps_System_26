# Day 3 DevOps Commands

## File Commands

### cat

Display the contents of a file.
Example:

```bash
cat file.txt
```

### cat file1 file2

Concatenate and display the contents of multiple files.

Example:

```bash
cat file1.txt file2.txt
```

### cat > file.txt

Create a new file or overwrite an existing file with the contents of standard input.

Example:

### cat file.txt >> new_file.txt

Append the contents of file.txt to new_file.txt.

Example:

```bash
cat file.txt >> new_file.txt
```

### cat file.txt | grep "search term"

Search for a specific term in a file.

Example:

```bash
cat file.txt | grep "search term"
```

### cat file.txt | wc -l

Count the number of lines in a file.

Example:
Copy or Merge File Contents Using cat Command

 command can combine the content of one or more files and redirect it into another file using >.

Syntax:

cat file1 file2 > new_file
Example:

cat file1.txt file2.txt > merged_file.txt

## Directory Commands

### mkdir

Create a new directory.

Example:

```bash
mkdir project
```

### mkdir dir1 dir2 dir3

Create multiple directories at once.

Example:

```bash
mkdir frontend backend database
```

### mkdir -p parent/child/grandchild

Create directory hierarchy.

Example:

```bash
mkdir -p India/Karnataka/Bangalore
```
Got it 👍 — here’s a **single, all-in-one Linux file path guide**, clean and ready to save as a **`.md` file**.

````md
# Linux File Path – All-in-One Guide

A **file path** in Linux shows the exact location of a file or directory in the filesystem.

---

## 1. Types of File Paths

### Absolute Path
- Starts from the root directory `/`
- Always works, no matter where you are

**Example**
```bash
/home/user/Documents/file.txt
````

**Command**

```bash
cat /home/user/Documents/file.txt
```

---

### Relative Path

* Starts from the current directory
* Shorter but depends on where you are

**Example**

```bash
Documents/file.txt
```

**Command**

```bash
cat Documents/file.txt
```

---

## 2. Special Path Symbols

| Symbol | Meaning                           |
| ------ | --------------------------------- |
| `/`    | Root directory                    |
| `.`    | Current directory                 |
| `..`   | Parent directory                  |
| `~`    | Home directory                    |
| `*`    | Wildcard (matches multiple files) |

---

## 3. Common Linux File Path Commands

### Show Current Directory

```bash
pwd
```

### List Files in a Path

```bash
ls /etc
```

### Change Directory

```bash
cd /var/log
```

### Go to Home Directory

```bash
cd ~
```

### Go Back One Directory

```bash
cd ..
```

---

## 4. File Operations Using Paths

### Create a File

```bash
touch /tmp/test.txt
```

### Create a Directory

```bash
mkdir ~/projects
```

### Copy a File

```bash
cp ~/file.txt /tmp/file.txt
```

### Move or Rename a File

```bash
mv old.txt ../new.txt
```

### Delete a File

```bash
rm /tmp/test.txt
```

### Delete a Directory

```bash
rm -r ~/projects
```

---

## 5. Viewing Files with Paths

### Display File Content

```bash
cat /var/log/syslog
```

### View Large File

```bash
less /var/log/syslog
```

### Show File Details

```bash
ls -l /home/user
```

---

## 6. Example Workflow (All Together)

```bash
pwd
cd ~/Downloads
ls .
mkdir test
touch test/file.txt
cat test/file.txt
cd ..
rm -r Downloads/test
```

---

## 7. Important Notes

* Linux paths are **case-sensitive**
* `/File.txt` and `/file.txt` are different
* Prefer **absolute paths** in scripts
* Use **relative paths** for quick navigation

---

## Summary

* Absolute path → starts with `/`
* Relative path → based on current directory
* Paths are used in almost every Linux command

```

If you want, I can also:
- compress this into a **1-page cheat sheet**
- add **filesystem diagrams**
- or tailor it for **bash scripting beginners**
```

### cd directory

Move into a directory.

Example:

```bash
cd backend
```

### cd ".."

Move to previous directory.

Example:

```bash
cd ..
```

### cd ../../

Move multiple directories back.

Example:

```bash
cd ../../..
```

### cd ~

Go to home directory.

Example:

```bash
cd ~
```

## Listing & Navigation

## ls

List files and directories.

Example:

```bash
ls
```

### pwd

Print current working directory.

Example:

```bash
pwd
```

## File Commands

### touch file

Create an empty file.

Example:

```bash
touch app.py
```

### touch file1 file2 file3

Create multiple files.

Example:

```bash
touch a.txt b.txt c.txt
```

## File Editors

### nano file

Open file in nano editor.

Example:

```bash
nano config.txt
```

Shortcuts:
--> CTRL+O save
--> CTRL+X exit

### vi / vim file

Open file in vi editor.

Example:

```bash
vi deployment.yaml
```

Modes:
1 iinsert
2 ESC command
3 :wq save and quit
4 :q! quit without saving

## File Content Commands

### cat file

Display file content.

Example:

```bash
cat app.log
```

### cat > file

Overwrite file with new content.

Example:

```bash
cat > config.txt
```

### cat >> file

Append content to file.

Example:

```bash
cat >> app.log
```

### cat input.txt > output.txt

Redirect content to another file.

Example:

```bash
cat a.txt > b.txt
```

## Real-World Usage (DevOps)

Used daily for:
-> Linux Servers
-> AWS EC2
->Docker Containers
->Kubernetes Nodes
-> CI/CD Pipelines

Master these commands for interviews and production systems.

## System-level Commands

1. `uname` - Find the name of the system
2. `uptime` - Find the uptime of the system
3. `top` - Find the top processes running on the system
4. `who` - Find the users logged into the system
5. `whoami` - Find the current user
6. `w` - Find the users logged into the system and what they are doing
7. `free` - Find the memory usage of the system
8. `df` - Find the disk space usage of the system
9. `id` - Check the user id and group id
10. `SUDO` - Super user do used to execute the commands with root privileges
11. `apt` - Install the packages on the system
12. `sudo apt-get update` - Update the package list
13. `sudo apt-get upgrade` - Upgrade the packages
14. `yum` - Install the packages on the system
15. `sudo yum update` - Update the package list
16. `sudo yum upgrade` - Upgrade the packages
17. `dnf` - Install the packages on the system
18. `sudo dnf update` - Update the package list
19. `sudo dnf upgrade` - Upgrade the packages

## User & Group Management Commands

1. `useradd` - Create a new user
2. `useradd -m username` - Create a new user with home directory
3. `userdel` - Delete a user
4. `passwd` - Change the password of a user
5. `groupadd` - Create a new group
6. `groupdel` - Delete a group
7. `usermod` - Modify a user
8. `Su` - Switch to the root user
9. `sudo` - Execute the commands with root privileges
10. `sudo su` - Switch to the root user and execute the commands with root privileges
11. `sudo su -` - Switch to the root user with environment variables
12. `cat /etc/passwd` - View the password file
13. `cat /etc/group` - View the group file
14. `cat /etc/shadow` - View the shadow file
15. `sudo groupadd groupname` - Create a new group
16. `sudo groupdel groupname` - Delete a group
17. `sudo useradd -g groupname username` - Create a new user in a group
18. `sudo gpasswd -a username groupname` - Add a user to a group
19. `sudo gpasswd -d username groupname` - Delete a user from a group
20. `sudo passwd username` - Change the password of a user
21. `id username` - Check the user id and group id of a user
22. `groups username` - Check the groups of a user
23. `sudo usermod -aG groupname username` - Add a user to a group
24. `sudo usermod -G groupname username` - Remove a user from a group
25. `sudo chage -l username` - Check the password expiry details of a user
26. `sudo chage -E YYYY-MM-DD username` - Set the account expiry date of a user
27. `sudo chage -M days username` - Set the maximum password validity days
28. `sudo chage -m days username` - Set the minimum password validity days

## File Permissions

### Permission Format: `drwxrwxr-x`

- `d` - directory
- `-` - file
- `r` - read
- `w` - write
- `x` - execute

### Permission Levels

- `000 (---)` - no permissions
- `010 (-1-)` - read permission

### Common Commands

```bash
ls -l
```

View permissions of a file or directory.

```bash
chmod 755 filename
```

Change file permissions.

```bash
chown user filename
```

Change file owner.

```bash
chgrp groupname filename
```

Change file group.
