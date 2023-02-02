print("Welcome to my computer quiz!")

playing = input("Do you want to play?(yes or no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

#output
Welcome to my computer quiz!
Do you want to play? yes
Okay! Let's play :)
What does CPU stand for? central processing unit
Correct!
What does GPU stand for? graphics processing unit
Correct!
What does RAM stand for? random access memory
Correct!
What does PSU stand for? power supply
Correct!
You got 4 questions correct!
You got 100.0%.

Process finished with exit code 0
