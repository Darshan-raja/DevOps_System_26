--> Linux for DevOps basic commands with examples

1. ls (list).
example : ls
2. pwd (print working directory).
example : pwd
3. cd (change directory).
4. cd .. (go back one directory).
   example : cd ..
5. cd / (go to the root directory).
example : cd Desktop
6. mkdir (make directory).
example : mkdir newfolder
7. rmdir (remove directory).
example : rmdir newfolder
8. touch (create a new file).
example : touch newfile.txt
9. rm (remove file).
example : rm newfile.txt
10. cp (copy file).
example : cp newfile.txt Desktop
11. mv (move file).
12. cat (concatenate files and print on the standard output).
example : cat newfile.txt
13. more (display the content of a file).
example : more newfile.txt
14. less (display the content of a file).
example : less newfile.txt
15. head (display the first part of a file).
examle : head newfile.txt
16. tail (display the last part of a file).
example : tail newfile.txt
17. grep (search for a pattern in a file).
example : grep "hello" newfile.txt
18. find (search for a file or directory).
example : find / -name newfile.txt
19. chmod (change the permissions of a file or directory).
example : chmod 777 newfile.txt
20. chown (change the owner of a file or directory).
examle : chown user:newfile.txt
21. chgrp (change the group of a file or directory).
example : chgrp group:newfile.txt
22. ps (process status).
example : ps -ef
23. top (display the top processes).
example : top
24. kill (terminate a process).
example : kill 1234
25. killall (terminate all processes with a name).

-->## Multiple commands in one line:**

1. ls -l | grep "hello" (list all files and directories and search for "hello" in the output).
   example : ls -l | grep "hello" | wc -l (list all files and directories and search for "hello" in the output and count the number of lines).

2. mkdir ""newfoldername"" && touch ""newfoldername/newfilename.txt""
    (create a directory and a file in one command). "&&" is used to execute the second command only if the first command is successful.
   example : mkdir project && touch project/file1.txt project/file2.txt

3. mkdir  ""dir 1"" && mkdir ""dir 2"" && mkdir ""dir 3"" (create three directories in one command).
   example : mkdir dir1 dir2 dir3
4. touch ""file1.txt"" ""file2.txt"" ""file3.txt"" (create three files in one command).
   example : touch file1.txt file2.txt file3.txt

