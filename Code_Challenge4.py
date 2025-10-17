print("Welcome to Manhwa Recommender")

manhwa = input("What Genre do you prefer? (Action/Regressor/Supernatural) ").lower()
length = input("How long do you want to read? (Short/Medium/Long) ").lower()
decade = input("What time of release would you like? (2000s/2010s) ")

# Action
if manhwa == "action":
    if length == "short":
        if decade == "2000s":
            print("We recommend", "The Breaker")
        elif decade == "2010s":
            print("We recommend", "Revenge Of The Iron Blooded Sword Hound")
    elif length == "medium":
        if decade == "2000s" or decade == "2010s":
            print("No Available Manhwa")
    elif length == "long":
        if decade == "2000s":
            print("We recommend", "The God of High School")
        elif decade == "2010s":
            print("We recommend", "Viral Hit")

# Regressor
elif manhwa == "regressor":
    if length == "short":
        if decade == "2000s":
            print("No Available Manhwa")
        elif decade == "2010s":
            print("We recommend", "Absolute Necromancer")
    elif length == "medium":
        if decade == "2000s":
            print("No Available Manhwa")
        elif decade == "2010s":
            print("We recommend", "Superhuman Battlefield")
    elif length == "long":
        if decade == "2000s":
            print("No Available Manhwa")
        elif decade == "2010s":
            print("We recommend", "The Worn and Torn Newbie")

# Supernatural
elif manhwa == "supernatural":
    if length == "short":
        if decade == "2000s":
            print("We recommend", "BJ Archmage")
        elif decade == "2010s":
            print("We recommend", "Questism")
    elif length == "medium":
        if decade == "2000s" or decade == "2010s":
            print("No Available Manhwa")
    elif length == "long":
        if decade == "2000s":
            print("No Available Manhwa")
        elif decade == "2010s":
            print("We recommend", "Nano Machine")
