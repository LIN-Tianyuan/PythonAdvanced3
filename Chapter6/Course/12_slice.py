"""
séquence: Une classe de conteneurs de données avec un contenu
continu et ordonné et un support pour l'indexation (index).

list, tuple, string

séquence[début:fin:étape]
"""
my_list = [1, 2, 3, 4, 5]
# Découpage: sequence
print(my_list[1:4])
print(my_list[1:])      # my_list[1:5]
print(my_list[:3])     # my_list[0:3]
print(my_list[:])
print("-----------")
# list[begin:end:step]
print(my_list[1::2])    # print(my_list[1:5:2])
print(my_list[::2])
print("-----------")
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])
print(my_tuple[:1:-2])
print("-----------")
my_str = "12345"
print(my_str[:4:2])
print(my_str[::-1])
print(my_str[3:1:-1])