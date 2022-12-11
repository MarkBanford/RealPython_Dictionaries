'Testing knowledge'

# 1. Create empty dict called "captains"
# 2. Enter the following into it

''' "Enterprise" - "Picard"
    "Voyager" - "Janeway"
    "Defiant" - "Sisko"

'''

# 3. Write 2 if statements to check if "Enterprise" and "Discovery" exists as keys.
# set their value to "unknown" if the key does not exist.

# 4. Loop over dictionary to print "ship is captained by captain"
# 5. delete "Discovery" from dictionary


# 1 + 2 solution
captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3 soln

if "Enterprise" in captains:
    pass
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    pass
else:
    captains["Discovery"] = "unknown"

# 4 soln

for k, v in captains.items():
    print(f'The {k} is captained by {v}')
