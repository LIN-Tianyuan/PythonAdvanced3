count = 0
for element in range(1, 100):
    if element % 2 == 0:
        count += 1
print(f"{count} nombres pairs dans l'intervalle de 1 à 100 (à l'exception de 100 lui-même).")