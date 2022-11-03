import random
print("Totally Random One-Million-To-One")
print()
print("Guess a number betweem 1 and 1,000,000 and I will tellyou if you are too low, too high, or get it correct.")
print()
print("Let's play!")
print()
correctNumber = random.randint(1,1000000)
attempt = 0
while True:
  userGuess = int(input("What is your guess?"))
  if userGuess < 0:
    print("Now we'll never know what the answer is...")
    exit()
  attempt += 1
  if userGuess < correctNumber:
    print("Too low, please try again")
    print()
  elif userGuess > correctNumber:
    print("Too high, please try again")
    attempt += 1
    print()
    continue
  if userGuess ==correctNumber:
    print("That right!!🥳🥳")
    break
print("It took you",attempt,"guesses to get it correct!")   
print('''Click 'run' to try again with a different number''')
  
    