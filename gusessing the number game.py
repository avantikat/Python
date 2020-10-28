n=9
number_of_guesses= 1
print("welcome in the game of guessing number.\n")
print("you have only 5 chances to guess the correct number:")
while(number_of_guesses<=5):
    guess_number = int(input(" plz guess the number:\n"))
    if guess_number < 9:
      print("you entered small number plz try anoter one.\n")
    elif guess_number > 9:
        print("you entered greater number plz try another.\n")
    else:
        print(" congrts you won the game.\n")
        print(number_of_guesses,"number of guesses you use to guess  the number.")
        break
    print(5-number_of_guesses,"no.of guesses left")
    number_of_guesses = number_of_guesses + 1
    if(number_of_guesses>5):
          print(" sorry you are use your all chances \n better luck next time \n game over")

       
