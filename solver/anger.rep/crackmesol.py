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
