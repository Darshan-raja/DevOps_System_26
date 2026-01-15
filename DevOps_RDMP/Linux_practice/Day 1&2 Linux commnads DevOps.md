--> ##Linux for DevOps baisc commands with exmaples ##

1. ls (list).
exmple : ls
2. pwd (print working directory).
exmple : pwd
3. cd (change directory).
exmple : cd Desktop
4. mkdir (make directory).
exmple : mkdir newfolder
5. rmdir (remove directory).
exmple : rmdir newfolder
6. touch (create a new file).
exmple : touch newfile.txt
7. rm (remove file).
exmple : rm newfile.txt
8. cp (copy file).
exmple : cp newfile.txt Desktop
9. mv (move file).
10. cat (concatenate files and print on the standard output).
exmple : cat newfile.txt
11. more (display the content of a file).
exmple : more newfile.txt
12. less (display the content of a file).
exmple : less newfile.txt
13. head (display the first part of a file).
exmple : head newfile.txt
14. tail (display the last part of a file).
exmple : tail newfile.txt
15. grep (search for a pattern in a file).
exmple : grep "hello" newfile.txt
16. find (search for a file or directory).
exmple : find / -name newfile.txt
17. chmod (change the permissions of a file or directory).
exmple : chmod 777 newfile.txt
18. chown (change the owner of a file or directory).
exmple : chown user:newfile.txt
19. chgrp (change the group of a file or directory).
exmple : chgrp group:newfile.txt
20. ps (process status).
exmple : ps -ef
21. top (display the top processes).
exmple : top
22. kill (terminate a process).
exmple : kill 1234
23. killall (terminate all processes with a name).

-->## Mutiliple commands in one line:**

1. ls -l | grep "hello" (list all files and directories and search for "hello" in the output).
   exmaple : ls -l | grep "hello" | wc -l (list all files and directories and search for "hello" in the output and count the number of lines).

2. mkdir ""newfoldername"" && touch ""newfoldername/newfilename.txt"" (create a directory and a file in one command). "&&" is used to execute the second command only if the first command is successful.
   exmaple : mkdir newfolder && touch newfolder/newfile.txt
3. mkdir  ""dir 1"" && mkdir ""dir 2"" && mkdir ""dir 3"" (create three directories in one command).
   exmaple : mkdir dir1 dir2 dir3

