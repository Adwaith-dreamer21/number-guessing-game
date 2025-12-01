import random
number=random.randrange(1,101)
print("WELCOME TO THE NUMBER GUESSING GAME","You have to guess the number that computer has in it's mind!","Lets gooo!!",sep="\n")
user_input=int(input("Enter a number between 1 and 100: "))
times=0
game=True
while game:
    if user_input<number:
        user_input=int(input("Try a bigger number: "))
    elif user_input>number:
        user_input=int(input("Try a smaller number: "))
    elif user_input==number:
        print(f"Yayyy!!\nYou've guessed the number in {times} guesses")
        game=False
    times+=1
print("Thankyou!")