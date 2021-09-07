print("Welkom bij mijn quizje! ")

playing = input("Wil je spelen? ")

if playing != "ja":
    print("Dat is jammer :( ")
    quit()

else:
    print("Okay laten we spelen: ")

#vraag 1
answer = input("Hoeveel is 1+1? ")
if answer != "2":
    print("Incorrect! ")
else:
    print("Correct! ")

#vraag 2
answer = input("Hoeveel is 3*3? ")
if answer != "9":
    print("Incorrect! ")
else:
    print("Correct! ")

#vraag 3
answer = input("In welke provincie ligt Almere? ")
if answer != "Flevoland":
    print("Incorrect! ")
else:
    print("Correct! ")

print("\nGoed gedaan dit is het einde van de quiz! ")