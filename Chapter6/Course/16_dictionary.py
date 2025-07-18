# Définir un dict
stu_score = {
    "Leo": 90,
    "Laurent": 80,
    "Lucas": 70
}
print(stu_score)
print(type(stu_score))

print(stu_score["Leo"])

stu_total_score = {
    "Leo": {"English": 77, "Math": 66, "Physic": 33},
    "Laurent": {"English": 88, "Math": 86, "Physic": 55},
    "Lucas": {"English": 99, "Math": 96, "Physic": 66}
}

print(stu_total_score["Laurent"]["Math"])
print("----------")
stu_score1 = {
    "Leo": 90,
    "Laurent": 80,
    "Lucas": 70
}
# Modifier le dict
stu_score1["Leo"] = 100
print(stu_score1)
# Ajout d'un élément
stu_score1["Kevin"] = 60
print(stu_score1)
# Suppression d'un élément
value = stu_score1.pop("Kevin")
print(value)
print(stu_score1)

stu_score1.clear()
print(stu_score1)

print("----------")
stu_score2 = {
    "Leo": 90,
    "Laurent": 80,
    "Lucas": 70
}
# Obtenir toutes les clés(keys)
keys = stu_score2.keys()
print(keys)

for key in keys:
    print(f"{key}: {stu_score2[key]}")

