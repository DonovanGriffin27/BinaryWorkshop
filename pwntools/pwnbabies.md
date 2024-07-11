# Documentation for the babypwn files

## 'babypwn'

### File Output
**babypwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, not stripped**
### 'babypwn' checksec output
**RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   70 Symbols        No       0               2               babypwn**

## 'babypwn.c'

### 'babypwn.c' File Output
**babypwn.c: C source, ASCII text**
###  'babypwn.c' checksec output

## Possible Vulnerabilities
- The character array is initialized as 32 bits but the input is reading 64 bits.
- The check variable was never initialized but it is being compared.
- There is a fixed memory adress.
### Why these are an issue
These **vulnerabilites**






