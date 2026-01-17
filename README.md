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
### **Part 1**

The first step I did was to read the README.txt in the sub-folder


![Screenshot](https://raw.githubusercontent.com/Friedlguana/gdg-cybersec/refs/heads/main/Screenshots/Screenshot%202026-01-17%20130234.png)

File hints at something being hidden. Executed ```ls -lah``` to view all files and found a .git folder. On inspection, I also found a objects folder and a logs file.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20131525.png?raw=true)

Secrets were accidently commited to this repo. Using the objects folder we can recreate to the comit before the config file is removed.

Inspection of the commit of hash ```1820c46b2c72a1eaa2c6e517d2a5ffc496f4e0aa``` confirmed the commit that i had to investigate.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20132518.png?raw=true)

On retrieval and inspection of the file, the first part of the flag was found.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20134006.png?raw=true)

- **1st part of the Flag:** `gdg{sw1ss_`
---

### **Part 2**

The first step I did, again, was to read the README.txt in the sub-folder
Readme hints at a hidden message, which is classic steganography

Executing `strings heheheha.png` gives only noise, so the flag is not hidden in the image in plaintext.

Next while running all the usual tools to extract hidden messages and clue, zsteg provided a string which turns out to be the second part of the flag.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-17%20160156.png?raw=true)

- **2nd part of the Flag:** `armykn1f3_`
---

### **Part 3**

On inspecting the readme, it's evident that there is a *zip bomb*.
So i unzipped the rar file onto a folder. There were around 3000 qr codes, so i got started by scanning all the qr codes using a simple [python automation script.](https://github.com/Friedlguana/gdg-cybersec/blob/main/script.py)

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-18%20005750.png?raw=true)

This obviously gave a lot of noise so i rewrote the [script](https://github.com/Friedlguana/gdg-cybersec/blob/main/main.py) to filter out all invalid qr codes and this gave me a result:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-18%20010945.png?raw=true)

I then passed this result into cyberchef which spit out the decoded message from base64:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/main/Screenshots/Screenshot%202026-01-18%20011220.png?raw=true)

- **3rd part of the Flag:** `gglol}`

# Conclusion

Combining all 3 parts we get a complete flag: `gdg{sw1ss_armykn1f3_gglol}`
