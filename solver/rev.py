# Import Angr
import angr

# Establish the Angr Project
target = angr.Project('r100')

desired_adr = 0x00400844

wrong_adr = 0x00400855

# Establish the entry state
entry_state = target.factory.entry_state(args=["./fairlight"])

# Establish the simulation
simulation = target.factory.simulation_manager(entry_state)

# Start the simulation
simulation.explore(find = desired_adr, avoid = wrong_adr)

solution = simulation.found[0].posix.dumps(0)
print(solution)
