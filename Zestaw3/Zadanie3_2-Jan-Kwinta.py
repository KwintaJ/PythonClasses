#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.2             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

# Co zlego w kodzie?

L = [3, 5, 4] ; L = L.sort()
# Funkcja sort nie zwraca posortowanej listy. Powyzsza linijka powinna wygladac
# L = [3, 5, 4] ; L.sort()

x, y = 1, 2, 3
# Po lewej stronie = sa dwie zmienne a po prawej trzy wartosci, wiec nie mozna
# wykonac przyporzadkowania.

X = 1, 2, 3 ; X[1] = 4
# X jest krotka (tuple). Nie mozna zmienic wartosci krotki.
# Jezeli chcemy, zeby X byl lista musimy uzyc []
# X = [1, 2, 3]

X = [1, 2, 3] ; X[3] = 4
# X jest trzyelementowa lista. Posiada indeksy 0, 1, 2. Nie posiada indeksu 3.

X = "abc" ; X.append("d")
# X jest lancuchem znakow (str). Funkcja append nie jest funkcja str.
# Do laczenia stringow trzeba uzyc operatora +

L = list(map(pow, range(8)))
# Funkcja pow przyjmuje dwa argumenty, a w powyzszym przykladzie funkcja map daje 
# do pow tylko jedna liczbe.
