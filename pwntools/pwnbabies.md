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










