
# Print the pattern

pattern = "*"

for i in range(9):
    if i==0:
        print(pattern)
    elif i<5:
        pattern = pattern + " *"
        print(pattern)
    else:
        pattern = pattern[:-2]
        print(pattern)