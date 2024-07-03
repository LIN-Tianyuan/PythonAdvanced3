print("Bienvenue au Zoo!")
height = int(input("Veuillez indiquer votre taille (cm): "))
if height > 120:
    print("Vous mesurez plus de 120 cm et n'est pas autorisé à entrer gratuitement.")
    print("Cependant, si votre niveau VIP est supérieur à 3, vous pouvez entrer gratuitement.")
    vip_level = int(input("Veuillez entrer votre niveau VIP(1~5): "))
    if vip_level > 3:
        print("Votre niveau vip est supérieur à 3 et vous pouvez entrer gratuitement.")
    else:
        print("Désolé, toutes les conditions ne sont pas remplies et un billet est nécessaire pour 10 euro.")

print("Bonne visite!")