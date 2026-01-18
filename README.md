# CTF Write-Up
### A write-up for GDG Cybersecurity Round 2 Enrollments.

## Task 2: Hidden Recipe


- **Flag Format:** `Gdg{flag}`
- **Provided File:** [Virtual Box File](https://drive.google.com/file/d/1S-8rtj4Q0osUNJC7hnqx4oYx7iz6pYTS/view?)

---

### **Part 1**

On setting up the vm and figuring out the ip address, I initially ran a nmap scan to figure out all open ports and what services were being run. 

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20145354.png?raw=true)

According to the scan, there were 2 interesting findds:

- An open SSH port
- An open FTP port

Also inspected the site directly, there seems to be a login and register page.
Created an account and inspected the site further. However everything seemed normal and in place.

Next I ran a gobuster scan to find if there were any hidden directories:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20154258.png?raw=true)

Out of all the given directories, i found a base64 string in `/logs` which after decoding gives me:

```
2024-11-14T13:42:31Z INFO sshd[1234]: Accepted password for deploy from 192.168.1.10

2024-11-14T13:42:33Z INFO sshd[1234]: User deploy authenticated using password 'Spring2021!'

2024-11-14T13:42:40Z INFO ftpd[567]: FTP service listening on 0.0.0.0:21
```

This log gives me a major clue:
A user named `deploy` was able to ftp into the server with the password `Spring2021!`

However on trying to access the server with ftp, server responds with: `530 permission denied`

Concurrently while logging in with an account that i created, i was also looking at the requests and found this:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20160200.png?raw=true)

If we can just switch the admin value to true, we might get admin access to the site.

So i inspected the stored cookie value and extracted the JSON Web Token
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUsImFkbWluIjpmYWxzZSwiaWF0IjoxNzY4NzMyMjk1LCJleHAiOjE3NjkzMzcwOTV9.Pl7Y00TVoNyr3dZPPB03m8tJmpBsKpqLFuoWCRw3bIk`

To edit the token i loaded up [jwt.io](https://jwt.io) and flipped the key-value pair to `admin: true`

However when i reloaded the page, it just signed me off. So i tried it again but this time, removed the signature: `alg: none`.

This worked and I got admin access to the webpage:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20161211.png?raw=true)

Over here i was able to download a logs file which contained some useful info:

```
2024-10-17T21:18:12Z INFO  sshd[1133]: Accepted password for deploy from 10.10.14.7 port 54122 ssh2
2024-10-17T21:18:12Z INFO  sshd[1133]: pam_unix(sshd:session): session opened for user deploy(uid=1001)
2024-10-17T21:18:12Z INFO sshd[1133]: User deploy authenticated using password 'Markisarobot!'
```

However the password does not seem to work again:
```
└─$ ssh deploy@192.168.29.150
deploy@192.168.29.150's password: 
Permission denied, please try again.
```

I also found this:
```
2024-10-17T21:23:11Z INFO  ftpd[2077]: FTP login successful: user=backup from 192.168.56.1
2024-10-17T21:23:11Z WARN  ftpd[2077]: Cleartext authentication in use
2024-10-17T21:23:11Z INFO  ftpd[2077]: USER backup
2024-10-17T21:23:11Z INFO  ftpd[2077]: PASS oLd$bAcKuPsN@ThInGt@sEeHeRe
```

This time i was successfully able to authenticate:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20161920.png?raw=true)

After unzipping and inspecting the folder, i found one interesting detail:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20162137.png?raw=true)

Now when i tried to ssh with these credentials, i was able to login:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-2/Screenshots/Screenshot%202026-01-18%20162420.png?raw=true)

However the file required admin permissions to execute. Using sudo wasn't viable since it wasn't in the sudoers file. However su worked and i was able to run the binary which gave me the flag.


# Conclusion
**Flag found:** `gdg{5utd0_ld3_l3_4_5tndw1ch}`
