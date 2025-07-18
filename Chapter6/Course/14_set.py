# Définition d'une collection(set)
# dé-dupliqués et non ordonnés
# le set ne prend pas en charge l'accès à l'index
# 'set' object is not subscriptable
name = {"Python", "666", "Python", "y6"}
# print(name[0]) # error
print(name)
print("----------")
my_set = {"Leo", "Laurent"}
# Ajout d'un élément
my_set.add("Kevin")
print(my_set)
print("----------")
my_set2 = {"Leo", "Laurent", "Kevin"}
# Supprimer l'élément
my_set2.remove("Leo")
print(my_set2)
print("----------")
my_set3 = {"Leo", "Laurent", "Kevin"}
# Suppression aléatoire d'éléments
element = my_set3.pop()
print(element)
print(my_set3)
print("----------")
my_set4 = {"Leo", "Laurent", "Kevin"}
# Effacer le set
my_set4.clear()
print(my_set4)
print("----------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
# Prend que l'ensemble 1 possède et que l'ensemble 2 ne possède pas
set3 = set1.difference(set2)
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")
print("----------")
set4 = {1, 2, 3}
set5 = {1, 5, 6}
# Comparer l'ensemble 1 et l'ensemble 2, dans l'ensemble 1, retirer les mêmes éléments que dans l'ensemble 2
set4.difference_update(set5)
print(f"set4: {set4}")
print(f"set5: {set5}")
print("----------")
set7 = {1, 2, 3}
set8 = {1, 5, 6}
# Combiner l'ensemble 1 et l'ensemble 2
set9 = set7.union(set8)
print(f"set7: {set7}")
print(f"set8: {set8}")
print(f"set9: {set9}")
print("----------")
set10 = {1, 2, 3}
print(len(set10))
print("----------")
for i in set10:
    print(i)






