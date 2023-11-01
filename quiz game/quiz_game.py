print("Welcome to my country quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What's the capital of England? ")
if answer.lower() == "london":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Germany? ")
if answer.lower() == "berlin":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Spain? ")
if answer.lower() == "madrid":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")