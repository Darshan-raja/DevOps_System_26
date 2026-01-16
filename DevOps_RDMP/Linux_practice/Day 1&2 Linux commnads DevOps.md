Gotcha 👍
Below is **clean Markdown (.md)** with **no extra gaps between sections** (compact, continuous). You can paste this directly into a `.md` file.

---

## Linux for DevOps – Basic Commands with Examples

### File & Directory Navigation

1. **ls** (list files and directories)
   Example: `ls`
2. **pwd** (print working directory)
   Example: `pwd`
3. **cd** (change directory)
   Example: `cd Desktop`
4. **cd ..** (go back one directory)
   Example: `cd ..`
5. **cd /** (go to root directory)
   Example: `cd /`
6. **cd ../..** (go back two directories)
   Example: `cd ../..`
7. **cd ./ ** (current directory reference)
   Example: `cd ./`

### File & Directory Management

8. **mkdir** (make directory)
   Example: `mkdir newfolder`
9. **rmdir** (remove empty directory)
   Example: `rmdir newfolder`
10. **touch** (create a new file)
    Example: `touch newfile.txt`
11. **rm** (remove file)
    Example: `rm newfile.txt`
12. **cp** (copy file)
    Example: `cp newfile.txt Desktop`
13. **mv** (move or rename file)
    Example: `mv newfile.txt Desktop/`

### File Viewing & Searching

14. **cat** (display file content)
    Example: `cat newfile.txt`
15. **more** (view file page by page)
    Example: `more newfile.txt`
16. **less** (advanced file viewer)
    Example: `less newfile.txt`
17. **head** (display first lines of a file)
    Example: `head newfile.txt`
18. **tail** (display last lines of a file)
    Example: `tail newfile.txt`
19. **grep** (search text in a file)
    Example: `grep "hello" newfile.txt`
20. **find** (search for files/directories)
    Example: `find / -name newfile.txt`

### Permissions & Ownership

21. **chmod** (change file permissions)
    Example: `chmod 777 newfile.txt`
22. **chown** (change file owner)
    Example: `chown user newfile.txt`
23. **chgrp** (change file group)
    Example: `chgrp group newfile.txt`

### Process Management

24. **ps** (process status)
    Example: `ps -ef`
25. **top** (display running processes)
    Example: `top`
26. **kill** (terminate a process by PID)
    Example: `kill 1234`
27. **killall** (terminate processes by name)
    Example: `killall nginx`

## Multiple Commands in One Line

28. **Pipe (`|`) usage**
    Example: `ls -l | grep "hello"`
    Count matches: `ls -l | grep "hello" | wc -l`
29. **Using `&&` (run next command if previous succeeds)**
    Example: `mkdir project && touch project/file1.txt project/file2.txt`
30. **Create multiple directories in one command**
    Example: `mkdir dir1 dir2 dir3`
31. **Create multiple files in one command**
    Example: `touch file1.txt file2.txt file3.txt`

---

If you want, I can also:

* Minify it even more (single-line bullets)
* Add **DevOps-focused notes** inline
* Split into **Beginner / Intermediate / Advanced** `.md` files