text = input("Say something ")
result = ""
for char in text:
    if char.lower() not in["a", "e", "i", "o", "u"]:
        result += char
print(result)
