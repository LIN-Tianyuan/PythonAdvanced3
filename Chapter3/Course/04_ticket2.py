print("Bienvenue au Zoo!")
height = int(input("Veuillez indiquer votre taille (cm): "))
vip_level = int(input("Veuillez entrer votre niveau VIP(1~5): "))
day = int(input("Veuillez entrer la date du jour(1~31): "))
if height <= 120:
    print("Vous pouvez entrer gratuitement si vous mesurez moins de 120 cm.")
elif vip_level > 3:
    print("Votre niveau vip est supérieur à 3 et vous pouvez entrer gratuitement.")
elif day == 1:
    print("Aujourd'hui est le 1er jour libre pour visiter.")
else:
    print("Désolé, toutes les conditions ne sont pas remplies et un billet est nécessaire pour 10 euro.")

print("Bonne visite!")