# CTF Write-Up
### A write-up for GDG Cybersecurity Round 2 Enrollments.

## Task 1B: apple_pi3


- **Flag Format:** `Gdg{flag}`
- **Provided File:** [Binary File](https://drive.google.com/file/d/1SdMAUG_3JF0pGujEzn6jpeGXnIYEl8f2/view)

---

### **Part 1**

First thing to do with the binary was to run it as well as run preliminary inspections on it. On inspecting noticed interesting stuff when executed `strings apple_pie`:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20030114.png?raw=true)

Fired up ghidra and ran analysis to find something related to these keywords and found something interesting

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20030404.png?raw=true)

Converting the hex data stored in to char provided with the following:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20030538.png?raw=true)

upon passing `not_the_password` as the password in the binary however did not give a flag, but a different output.

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20030926.png?raw=true)

While doing these operations, i noted another function called `def_nothing_important`. On further inspection i found some data stored in a stack:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20031218.png?raw=true)

This data also seem to have XOR encrypted with key of '5'. So i extracted the hex data, converted from hex and also removed the xor encryption. This operation revealed a flag:

![Screenshot](https://github.com/Friedlguana/gdg-cybersec/blob/task-1b/Screenshots/Screenshot%202026-01-18%20031507.png?raw=true)

# Conclusion
**Flag found:** `gdg{P1E_3xpl01ted_lol}`
