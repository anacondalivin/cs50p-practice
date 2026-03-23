name = input("What is the Home team name?").strip()
opponent = input("What is the Away team name?").strip()
print(f"Thank you. The Home name is the {name}")
print(f"The Away name is the {opponent}")

home_score = int(input("What is the Home team score?").strip())
away_score = int(input("What is the Away team score?").strip())

print(" ------ SCOREBOARD ------")
print(f"Home: {name} | Score: {home_score}")
print(f"Away: {opponent} | Score: {away_score}")
# commentator reacts diffrently depending on whos's winning
if home_score > away_score:
    print(f"{name} is winning")
    if home_score - away_score >= 21:
          print(f"Tell the {opponent} to pack their bags. We've got ourselves a blowout!")
elif away_score > home_score:
    print(f"{opponent} is winning")
    if away_score - home_score >= 21:
        print("We got ourselves a blowout!")
else:
    print("We got ourselves a tie?") 
