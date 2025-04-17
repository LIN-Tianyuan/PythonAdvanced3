name_list = ['Leo', 'Lucas', 'Laurent']
print('Leo' in name_list)
print('----------')
# Trouver l'indice(index) d'un élément
print(name_list.index('Leo'))
print('----------')
# Modifier la valeur
name_list[0] = 'Thibault'
print(name_list)
name_list[-2] = 'Luna'
print(name_list)
print('----------')
# Insertion d'un élément
name_list.insert(1, 'Kevin')
print(name_list)
print('----------')
# Ajouter un élément
name_list.append('Alex')
print(name_list)
my_list = [1, 2, 3]
my_list.append([4, 5, 6])
print(len(my_list))
print(my_list)
print('----------')
# Ajouter un élément 2
my_list2 = [1, 2, 3]
my_list2.extend([4, 5, 6])
print(my_list2)
print('----------')
# Supprimer l'élément(1)
my_list3 = [1, 2, 3]
del my_list3[0]
print(my_list3)
print('----------')
# Supprimer l'élément(2)
my_list4 = [1, 2, 3]
my_list4.pop(0)
print(my_list4)
print('----------')
# Supprimer l'élément(3)
my_list4 = [1, 2, 3]
my_list4.remove(1)
print(my_list4)
print('----------')
# Supprimer la première correspondance d'un élément
my_list5 = [1, 2, 3, 2, 3]
my_list5.remove(2)
print(my_list5)
print('----------')
# Effacer le contenu de la liste
my_list6 = [1, 2, 3]
my_list6.clear()
print(my_list6)
print('----------')
# Compte le nombre d'élément dans une liste
my_list7 = [1, 1, 1, 2, 3]
print(my_list7.count(1))
# Compte le nombre d'élément dans une liste
print(len(my_list7))


