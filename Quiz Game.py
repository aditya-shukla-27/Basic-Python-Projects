def check_game(guess,answer):
    global score
    still_guess = True
    attempt = 0

    while(still_guess and attempt<3):
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score +=1
            still_guess = False

        else:
             if attempt<2:
                guess = input("Sorry Wrong Answer,.. Try Again")
             attempt+=1


    if attempt == 3:
        print(f"So the correct answer is {answer}")


score = 0
print("Guess the Person")
guess1 = input("Who is the founder of Microsoft")
check_game(guess1,"Bill Gates")
