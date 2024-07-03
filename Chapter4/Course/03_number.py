import random
num = random.randint(1, 100)
count = 0
while True:
    my_num = int(input("Veuillez saisir le numéro que vous souhaitez deviner: "))
    count += 1
    if my_num > num:
        print("Vous avez deviné un plus grand numbre.")
    elif my_num < num:
        print("Vous avez deviné un plus petit numbre.")
    else:
        print("Félicitations pour votre bonne réponse!")
        break
print(f"Vous avez deviné un total de {count} fois!")