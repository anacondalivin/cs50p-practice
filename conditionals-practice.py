x = int(input("What's x?"))
y = int(input("What's y?"))

# approach 1 - using or operator
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# approach 2 - using != operator
if x !=y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# approach 3 - using elif for specifc comparison
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
