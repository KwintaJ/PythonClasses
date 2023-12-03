#####################################
#                                   #
#  Zestaw 7             28.11.2023  #
#                                   #
#           Zadanie 7.6             #
#       Iteratory nieskonczone      #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

from itertools import cycle
from random import choice

print("(a) Iterator 0, 1, 0, 1, 0, 1, ...:")
BinaryIterator = cycle([0, 1])
for i in range(10):
    print(next(BinaryIterator))
print()


print("(b) Przypadkowe bladzenie po dwuwymiarowej sieci kwadratowej:")
RandomNESW = (choice(['N', 'E', 'S', 'W']) for _ in iter(int, 1))
for i in range(15):
    print(next(RandomNESW))
print()


print("(c) Iterator zwracajacy numery dni tygodnia:")
WeekIterator = cycle([0, 1, 2, 3, 4, 5, 6])
for i in range(18):
    print(next(WeekIterator))
print()
