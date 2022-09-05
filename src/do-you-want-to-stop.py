
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).
i="no"
while i == "no":
    i = input("Do you want to stop? ")
    if i == 'yes':
        break
    else:
        i="no"