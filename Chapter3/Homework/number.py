import random
num = random.randint(1, 10)
print(num)
number = int(input("Veuillez saisir le numéro que vous souhaitez deviner: "))
if number < num:
    print("Vous avez deviné un plus petit nombre.")
    number = int(input("Veuillez saisir le numéro que vous voulez deviner à nouveau: "))
    if number == num:
        print("Félicitations pour votre bonne réponse!")
    elif number < num:
        print("Vous avez deviné un plus petit nombre.")
        number = int(input("Veuillez saisir le numéro que vous voulez deviner une troisième fois: "))
        if number == num:
            print("Félicitations, dernière chance, vous l'avez deviné!")
        else:
            print("Les trois chances sont épuisées, vous n'avez pas devinéet le jeu a échoué.")
    elif number > num:
        print("Vous avez deviné un plus grand nombre.")
        number = int(input("Veuillez saisir le numéro que vous voulez deviner une troisième fois: "))
        if number == num:
            print("Félicitations, dernière chance, vous l'avez deviné!")
        else:
            print("Les trois chances sont épuisées, vous n'avez pas devinéet le jeu a échoué.")
elif number > num:
    print("Vous avez deviné un plus grand nombre.")
    number = int(input("Veuillez saisir le numéro que vous voulez deviner à nouveau: "))
    if number == num:
        print("Félicitations pour votre bonne réponse!")
    elif number < num:
        print("Vous avez deviné un plus petit nombre.")
        number = int(input("Veuillez saisir le numéro que vous voulez deviner une troisième fois: "))
        if number == num:
            print("Félicitations, dernière chance, vous l'avez deviné!")
        else:
            print("Les trois chances sont épuisées, vous n'avez pas devinéet le jeu a échoué.")
    elif number > num:
        print("Vous avez deviné un plus grand nombre.")
        number = int(input("Veuillez saisir le numéro que vous voulez deviner une troisième fois: "))
        if number == num:
            print("Félicitations, dernière chance, vous l'avez deviné!")
        else:
            print("Les trois chances sont épuisées, vous n'avez pas devinéet le jeu a échoué.")
else:
    print("Félicitations, vous avez réussi du premier coup!")
