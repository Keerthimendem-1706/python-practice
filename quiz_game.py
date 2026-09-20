score = 0
total = 3
# Q1
answer1 = input("1. What does CPU stand for? \n a) Central Processing Unit \n b) Computer Personal Unit \n c) Central Processor Unit \n").lower()
if answer1 =="a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is a) Central Processing Unit.")
# Q2
answer2 = input("2. Python is a _______? (fill in: programming language/snake): ").lower()
if answer2 == "programming language":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'programming language'.")
# Q3
answer3 = input("3. What does HTML stand for? \n a) Hyper Text Markup Language \n b) High Text Markup Language \n c) Hyper Text Machine Language \n").lower()
if answer3 == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is a) Hyper Text Markup Language.")
#final score
percentage = (score / total) * 100
print(f"\nYou got {score}/{total} correct!")
print(f"Final score: {percentage}%")