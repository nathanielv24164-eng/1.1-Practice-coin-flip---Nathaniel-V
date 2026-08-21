import random

def heads_tails():
    user_score=0
    computer_score=0
    options=("Heads", "Tails")
    while user_score!=2 and computer_score!=2:
        choice=random.randint(0,1)
        computer_guess=options[choice]
        user_guess=str(input("Heads or Tails"))
        if user_guess == computer_guess:
            print("it was {}, you huesses {}, you won the round".format(computer_guess, user_guess))
        else:
            print("It was {}, you guessed {}, you lost that round".format (computer_guess, user_guess))
            computer_score +=1
    #loop now ended and it will output winner of beat of 3
    if user_score==2:
        print("{}, you won that game".format(first_name))
    else:
        print("{}, you lost that game".format(first_name))

    #main program
    print("Welcome to Heads or Tails")
    first_name=str(input("what is your name"))
    heads_tails() #this calls up the function