#!/usr/bin/env python
from ctypes import CDLL
from pwn import *


io   = process('./time')

libc = CDLL("libc.so.6")
t = int(libc.time(0))
#print("Current time is: %d "  % (t))
ran_int = int((libc.srand(t)))
r = libc.rand()
io.recvline()

print(io.recvuntil("Enter your number: "))
io.sendline(b'%d' % r)
display = io.recvline()
print(display)
print(io.recvline())
print(io.recvline())
