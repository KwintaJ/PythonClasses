#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.1             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

# Przyklad 1
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Ten kod jest niepoprawny skladniowo. Znak ; w pythonie nie oznacza konca instrukcji


# Przyklad 2
for i in "axby": if ord(i) < 100: print (i)
# Ten kod jest niepoprawny skladniowo. Po dwukropku w tej samej 
# linii mozna umiescic tylko instrukcje prosta.


# Przyklad 3
for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Ten kod jest poprawny skladniowo. print() jest instrukcja prosta.
