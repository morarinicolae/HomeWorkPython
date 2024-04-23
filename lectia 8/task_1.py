# import os

# os.system("python lectia\ 8/task_1.py")

# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(1, 11):
  lista.append(i)
print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in lista:
  if i % 2 == 0:
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i < 5:
  i += 1
  print(i)
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {"name": "Ion", "age": 43, "city": "Chisinau"}
for key, value in person.items():
  print(key, value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for rand in matrice:
  for element in rand:
    print(element)

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for b in range(1, 11):
  print("\n", b)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
lista = ["Ion", "Teodor", "Anton", "Maria"]
for index, element in enumerate(lista):
  print(index, element)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
lista1 = ["Ion", "Teodor", "Anton", "Maria"]
lista2 = ["Cristi", "Vasile", "Cristian", "Catalin"]
for element1, element2 in zip(lista1, lista2):
  print(element1, element2)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(1, 11):
  lista.append(i)
  print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
lista = [1, 2, 3, 4, 5]
while lista[0] < 50:
  lista[0] *= 2
  print(lista)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(1, 101):
  if i**2 < 100:
    lista.append(i**2)
    print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
  print(i, "x", 7, "=", i * 7)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(1, 6):
  for j in range(1, 6):
    lista.append((i, j))
    print(lista)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
lista = []
for i in range(1, 6):
  for j in range(1, 6):
    if i < j:
      lista.append((i, j))
      print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
import random

lista = []
for i in range(1, 11):
  lista.append(random.randint(1, 100))
  print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
n = int(input("Introduceti dimensiunea patratului: "))
for i in range(n):
  for j in range(n):
    print("*", end="")
  print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
  for j in range(1, i + 1):
    print(j, end="")
  print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
  for j in range(i, 0, -1):
    print(j, end="")
  print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
sir = "abcdefg"
for i in range(len(sir)):
  print(sir[i:])
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(1, 10):
  if i % 2 == 0:
    print("+-" * 10)
  #?????
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
for i in range(1, 9):
  for j in range(1, i + 1):
    print(j**i, end=" ")
  print()

  #?????????????
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
