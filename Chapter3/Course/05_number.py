import random
computer = random.randint(1, 5)
number1 = int(input("Veuillez deviner un numéro: "))
if number1 == computer:
    print("Félicitations, vous avez réussi du premier coup! ")
else:
    number2 = int(input("Mauvaise réponse, encore une fois: "))
    if number2 == computer:
        print("Félicitations pour votre bonne réponse!")
    else:
        number3 = int(input("Mauvaise réponse, encore une fois: "))
        if number3 == computer:
            print("Félicitations pour votre bonne réponse!")
        else:
            print("Désolé, vous avez mal deviné.")

