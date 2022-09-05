from curses.ascii import isupper
from pickle import FALSE, TRUE
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
lower_case = FALSE
upper_case = FALSE
number = FALSE
special = FALSE

for c in password:
    if c.islower():
        lower_case = TRUE
    elif c.isupper():
        upper_case = TRUE
    elif c.isnumeric():
        number = TRUE
    elif c in "$#@":
        special = TRUE
    else: 
        continue
    if lower_case == TRUE:
        if upper_case == TRUE:
            if number == TRUE:
                if special == TRUE:
                    is_valid = TRUE
                    break   

print(is_valid)
