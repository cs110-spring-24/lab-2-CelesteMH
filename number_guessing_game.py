import random
num = random.randint(1, 100)

user = input("Guess a number between 1-100: ")
user = int(user)
userhigh = 100
userlow = 1
loopnum = 1

while user != num or user == num:
    if user > num:
        print("Too high")
        if user < userhigh:
            userhigh = user
    elif user < num:
        print("Too low")
        if user > userlow:
            userlow = user
    else:
        print(f"it took you {loopnum} guesses to get {num}!!")
        round = input("You got it! Would you like to play again? ")
        if round == "yes" or round == "Yes":
            loopnum = 0
            num = random.randint(1, 100)
            userhigh = 100
            userlow = 1
        else:
            print("Goodbye!")
            break


    if userhigh != 0 and userlow != 0:
        user = int(input(f"guess a number betweet {userlow} and {userhigh}: "))
    elif userhigh !=0:
        user = int(input(f"Guess a number between 0 and {userhigh}: "))
    elif userlow != 0:
        user = int(input(f"Guess a number betweenm {userlow} and 100: "))
    else:
        user = int(input("Guess a number between 1-100: "))
    loopnum = loopnum + 1


