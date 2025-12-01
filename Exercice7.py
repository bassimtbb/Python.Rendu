numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = sum(1 for number in numbers if number % 2 == 0)
odd_count = sum(1 for number in numbers if number % 2 != 0)

print("Nombre de nombres pairs :", even_count)
print("Nombre de nombres impairs :", odd_count)