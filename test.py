#!/usr/bin/env python

from ctypes import CDLL

libc = CDLL("libc.so.6")
t = int(libc.time(0))
print("Current time is: %d "  % (t))
ran_int = int((libc.srand(t)))
r = libc.rand()
print("Random number is: %d " % (r))
