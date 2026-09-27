import random
words = ["python","computer","programming","developer"]
word = random.choice(words)
guessed =[]
wrong = 0
print("=== HANGMAN GAME ===")
while wrong <6:
    display =""
    for letter in word:
        if letter in guessed:
            display += letter +""
        else:
            display += "_"
    print("\nWord:",display)
    print("Wrong guesses:",wrong,"/6")
    if "_" not in display:
        print("You won!")
        break
    guess = input("Guess a letter:").lower()
    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        wrong += 1
        print("Wrong guess!")
else:
    print("\nGame Over!")
    print("The word was:",word)

