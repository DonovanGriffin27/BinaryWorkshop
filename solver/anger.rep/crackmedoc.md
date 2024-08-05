# crackme solution
This document serves as the write for solution to the crackme program.

## Background Information
**angr** is a multi-architecture **binary analysis toolkit**, with the capability to perform dynamic symbolic execution and various static analyses on binaries. It combines both static and dynamic symbolic ("concolic") analysis, providing tools to solve a variety of tasks.

## The tasks at hand
### crackme.c program
**'crackme.c'** is a C program file that is essentially a **password verification program**. The program looks for the **correct** password based off the user's input then displays a message based off in the input is **valid** or **invalid**. 
**crackme** reads a 10-character password input from the user and uses a linked list of nodes to permute the input characters based on their numeric values. It then constructs a string by following the linked list pointers and compares it to a predefined password. If the constructed string matches the predefined password, the user is congratulated; otherwise, an error message is shown.

## Steps to a solution
- We realized that **nodes** point to eachother and there is a **list** with **chracters mapped** on that **list**.
- To move throughout the linked list, use each value in the flag array as an index. To create a new string, gather character values whose origins trace back to the nodes that these indices point to.

## Solution Code
``` python
#!/usr/bin/env python3
import angr
import claripy

# Load the binary
target = angr.Project('crackme', main_opts = {'base_addr': 0x0}, load_options = {'auto_load_libs': False})

# Create a symbolic variable for the input
flag = claripy.BVS("flag", 8 * 10)  # 10 bytes of symbolic int

entry_state = target.factory.entry_state(stdin = flag)

#(0 - 9) for loop
for i in range(10):
        entry_state.solver.add(flag.get_byte(i) >= 48) 
        entry_state.solver.add(flag.get_byte(i) <= 57) 

# Create a simulation 
simulation = target.factory.simulation_manager(entry_state)

# Specify the desired address (where the correct input leads to)
desired_adr = 0x1219

# Specify the address (which means the input is incorrect)
wrong_adr = 0x1227

# Start the exploration
simulation.explore(find=desired_adr, avoid=wrong_adr)

solution = simulation.found[0].posix.dumps(0)
print(solution)
```
As shown above, we started our solution off by importing the **angr** library, then created a variables named **flag** which has 10-bytes and is constrained to **digits (0-9)**. Then we looked for possible inputs from the address **0x1219** while avoiding the wrong adress which is **0x1227**. Once all of these segments are executed our solution is then displayed.

### Result
The solution itself is: 
```
b'6241570398'
```
Once this solution is the input for originial **crackme.c** program the resulting output is:
```
Congratulations! You have found the flag.
```
 


