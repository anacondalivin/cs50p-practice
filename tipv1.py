bill = float(input("Whats is the total?"))
print(f"Thank you! ${bill:.2f} is your total")
rate = input("Rate the service (excellent, good, decent):").lower()

if rate == "excellent":
    tip = bill * 0.20
    total = bill + tip 
    print(F"Your tip would be ${tip:.2f}.")
    print(f"Your total with tip is ${total:.2f}")
   

elif rate == "good":
    tip = bill * 0.15
    total = bill + tip 
    print(f"Your total with tip is ${total:.2f}")
    print(f"Your tip would be ${tip:.2f}.")

elif rate == "decent":
    tip = bill * 0.10
    total = bill + tip
    print(f"Your total with tip is ${total:.2f}")
    print(f"Your tip amount would be ${tip:.2f}.")
  

else: 
    tip = 0
    total = bill + tip 
    print("I am sorry we didnt treat you with care. We dont deserve a tip")
    print(f"Your total without tip iis ${total:.2f}.")
