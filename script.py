def print_diagonally(number):
  for i in range(1, 11):
    print(f"{i * number:2}", end=" ")
    print()
number = int(input("pick a number : "))

print_diagonally(number)

