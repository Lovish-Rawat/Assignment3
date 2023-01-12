for a in range(11, 0, -2):
  print()
  print(" " * (5-a//2), end="")
  for j in range(65, 65 + a):
    print(chr(j), end="")