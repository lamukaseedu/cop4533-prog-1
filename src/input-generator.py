import random

n = int(input("Enter n: "))
with open("../data/generated.in", "w") as file:
  file.write(str(n))
  file.write("\n")
  numbers = list(range(1, n + 1))
  for i in range(0, 2 * n):
    random.shuffle(numbers)
    for j in range(0, n):
      file.write(str(numbers[j]))
      if (j != n - 1):
        file.write(" ")
    if (i != 2 * n - 1):
      file.write("\n")