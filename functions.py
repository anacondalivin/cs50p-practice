def parrot_song (name, number):
    print(f"Grandrising to you {name}")
    print(f"today is your {number}th birthday ")
    print("Grandrising to you!")
    print()

parrot_song("queen",22)
parrot_song("mom", 45)
parrot_song("bro", 19)

def display_invoice(username, amount, due_data):
    print(f"Goodevening {username}")
    print(f"You have a oustanding balance of ${amount:.2f} is due; {due_data}")
    
display_invoice("Customer", 2000.00, "04/21")    


def add(a,b):
    c = a + b
    return c
def subtract(a,b):
    c = a - b
    return c
def multiply(a,b):
    c = a * b
    return  c
def divide(a,b):
    c = a/b
    return c
print(add(10, 20))
print(subtract(10,20))
print(multiply(10,20))
print(divide(10,20))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Josh", "Downs")
print(full_name)
