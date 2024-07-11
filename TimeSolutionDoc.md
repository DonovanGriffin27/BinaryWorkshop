# 'time' Solution
### This document will explain the steps that were taken to develop a solution for the guessing game program

### Introduction
The binary we developed a solution for was the 'time' file from the nightmare repository created by 'guyinatuxedo'. 
The details of the 'time' file include:
- 64 bit binary
- Prompts user to enter guess a number
- Reads the user's input
- Based off user input, tells the user if their guess was valid

### Solution Process
From the understanding that the **'time'** file is essentially a number guessing game, we then looked at the **main** function in **Ghidra** which is an open source reverse engineering tool developed by the National Security Agency of the United States. **From looking at the'main' function we saw that the rand() function is what supplies the program with a random number. Then based off user input, the program performs a conditional operation to see if the random generated number matches the user's input.** Also from looking at the source code, we saw that **the programs seed for a random number is based on the current time.** With all the knowledge gained from looking at the source code we developed a python program that serves as a solution.

``` python
#!/usr/bin/env python
from ctypes import CDLL
from pwn import *

io  = process('./time')

libc = CDLL("libc.so.6")
t = int(libc.time(0))
print("Current time is: %d "  % (t))
ran_int = int((libc.srand(t)))
r = libc.rand()
io.recvline()

print(io.recvuntil("Enter your number: "))
io.sendline(r)
display = io.recvline()
print(display)
print(io.recvline())
print(io.recvline())
```

- The program starts off by passing a python enviorment then importing a C Dynamic Link Library and pwntools.
- Then from declaring our io variable and C library variable we were able to  **include the 'time' file in our solution file and also get the current time to match the seed.**
- We then created a variable that has a value that matches the current time for my program it was decalred as **'t'** next a random integer variable was created thhat generates a random number from the **srand()** function which has the time variable **('t') as the argument.**
- Then once this operation was performed we creted our **rand()** function variable which for my program was declared as **'r'** after that we received that line which is able to be done because of the pwntools import.
- We then used recieve line until the part of the program that asks the user to enter a guessing number. **Once that portion of the code occurs it was then time to send the rand() function variable we created earlier.** This was done by using the integer place holder to send the variable.
- The last steps were to print the last parts of the source code. From running the solution python file we were able to see that the random number variable we created matched the random number generated.         
