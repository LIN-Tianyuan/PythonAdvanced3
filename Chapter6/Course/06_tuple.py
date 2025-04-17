# Définir un tuple
t1 = (1, 2, "hello")
# 'tuple' object does not support item assignment
# t1[0] = 5
# Récupération des données par indice(index)
print(t1[2])
# tuple
print(type(t1))
print('----------')
t2 = (1, 2, "hello", 3, 4, "hello")
# Trouver l'indice(index)
print(t2.index("hello"))
# Compter le nombre de fois qu'une donnée apparaît dans un tuple
print(t2.count("hello"))
# La longueur
print(len(t2))
print('----------')
# On peux modifier le contenu d'une liste à l'intérieur d'un tuple
t3 = (1, 2, ['leo', 'laurent'])
t3[2][0] = 'alex'
print(t3)
print('----------')
t4 = (1, 2, ['leo', 'laurent'])
# 'tuple' object does not support item assignment
# t4[2] = [1, 2, 3]
print(t4)

