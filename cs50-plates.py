def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0] in ["0","1","2","3","4","5","6","7","8","9"]:
        return False
    if s[1] in ["0","1","2","3","4","5","6","7","8","9"]:
        return False
    for chan in s:
        if chan in [".", " ", "!","?","#","@","$","%","&"]:
            return False
    for char in s:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            if char == "0":
                return False
            break
    found_number = False
    for char in s:
        if found_number and char in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            return False
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            found_number = True
    return True
main()


