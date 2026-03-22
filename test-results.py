score = int(input("Score?"))

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >=80:
    print("Grade: B")
    print("Keep up the good work")
elif score >=70:
    print("Grade: C")
    print("I know you can do better")
elif score >=60:
    print("Do better")
    print("You need to study more")
else:
    print(f"Grade F | Your score was {score}. see me after class.")
