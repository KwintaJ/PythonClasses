#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.6             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

tallTxt = input("Podaj wysokosc prostokata:")
if not tallTxt.isdigit():
    print("To nie jest liczba naturalna!")
    exit()
tall = int(tallTxt)

wideTxt = input("Podaj szerokosc prostokata:")
if not wideTxt.isdigit():
    print("To nie jest liczba naturalna!")
    exit()
wide = int(wideTxt)

rowA = "+"
rowB = "|"

for i in range(wide):
    rowA += "---+"
    rowB += "   |"

prostokat = rowA

for i in range(tall):
    prostokat += "\n" + rowB + "\n" + rowA
    
print(prostokat)
