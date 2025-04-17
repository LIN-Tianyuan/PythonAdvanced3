list_total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_only_even_for = []
list_only_even_while = []

for x in list_total:
    if x % 2 == 0:
        list_only_even_for.append(x)
print(list_only_even_for)

i = 0
while i < len(list_total):
    if list_total[i] % 2 == 0:
        list_only_even_while.append(list_total[i])
    i = i + 1
print(list_only_even_while)