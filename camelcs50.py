word = input("camelCase:")
result = ""

for char in word:
    if char.isupper():
        result += "-" + char.lower()
    else:
        result += char
print(result)
