from curses.ascii import isupper
from pickle import FALSE, TRUE
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
lower_case = False
upper_case = False
number = False
special = False

for c in password:
    if c.islower():
        lower_case = True
    elif c.isupper():
        upper_case = True
    elif c.isnumeric():
        number = True
    elif c in "$#@":
        special = True
    else: 
        continue
    if lower_case == True:
        if upper_case == True:
            if number == True:
                if special == True:
                    is_valid = True
                    break   

print(is_valid)
