
# Print the numbers described in the exercise

numbers="1"
for i in range(1,11):
    if i==1:
        print(numbers)
    else:
        numbers=numbers+" "+str(i)
        print(numbers)