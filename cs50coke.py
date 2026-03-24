owed = 50
inserted = 0
while owed > 0:
    print(f"Amount Due: {owed} cents")
    coin = int(input("Insert Coin: "))
    if coin in [25,10,5]:
        owed = owed - coin
print(f"Change Owed: {owed * -1} cents")

