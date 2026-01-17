# CTF Write-Up
### A write-up for GDG Cybersecurity Round 2 Enrollments.

## Task 1: 3 Levels


- **Flag Format:** `Gdg{part1_part2_part3}`
- **Provided File:** [Zip File](https://drive.google.com/file/d/1fuI2GhLqQvgCnVCtJXcjhodA_z9pCemW/view?usp=sharing)

---

## Tools Used :
- **Linux-based OS**  - Kali Linux
- [**Cyberchef**](https://gchq.github.io/CyberChef/) - An Online AIO Data Analysis Tool
---
### **Step 1: Analyzing files**

The first step I did was to read the README.txt in the first sub-folder


![Screenshot](https://raw.githubusercontent.com/Friedlguana/gdg-cybersec/refs/heads/main/Screenshots/Screenshot%202026-01-17%20130234.png)

File hints at something being hidden. Executed ```ls -lah``` to view all files and found a .git folder. On inspection, I also found a objects folder and a logs file.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20131525.png?raw=true)

Secrets were accidently commited to this repo. Using the objects folder we can recreate to the comit before the config file is removed.

Inspection of the commit of hash ```1820c46b2c72a1eaa2c6e517d2a5ffc496f4e0aa``` confirmed the commit that i had to investigate.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20132518.png?raw=true)

On retrieval and inspection of the file, the first part of the flag was found.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20134006.png?raw=true)

- **1st part of the Flag:** `gdg{sw1ss_`
