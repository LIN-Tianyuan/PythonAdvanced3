# str: ne peut pas être modifié
name = "Alex"
print(name[0])
print(name[-1])
print(len(name))
print(name.index('l'))
print('---------')

name_string = 'Leo and laurent'
# Trouver la valeur de l'indice
print(name_string.index('a'))       # 4
print(name_string.index('and'))     # 4

name_string2 = 'Leo and laurent'
# Remplacer old, new
new_name_string2 = name_string2.replace('Leo', 'Kevin')
print(new_name_string2)
print(name_string2)

# Diviser la chaîne de caractères en plusieurs selon la chaîne de séparation spécifiée
name_list = name_string2.split(' ')
print(name_list)

name_string3 = '  Leo and laurent  '
# Suppression des espaces avant et arrière
new_name_string3 = name_string3.strip()
print(new_name_string3)

name_string4 = '12Leo and laurent21'
# Suppression de la chaîne spécifiée avant et arrière
new_name_string4 = name_string4.strip('12')
print(new_name_string4)

name_string5 = "Jean-Lucas and Lucas"
# Compter le nombre d'occurrences d'une chaîne de caractères
print(name_string5.count('Lucas'))
print(len(name_string5))

name_string6 = "  "
print(len(name_string6))

