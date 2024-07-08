from pwn import *

io = process('./time')
io.sendline('echo Hello, world')
print(io.recvuntil("Enter your number: "))
io.sendline(b'7')
display = io.recvline()
print(display)
