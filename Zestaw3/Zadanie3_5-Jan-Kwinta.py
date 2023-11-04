#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.5             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

lengthTxt = input("Podaj dlugosc miarki:")
if not lengthTxt.isdigit():
    print("To nie jest liczba naturalna!")
    exit()

length = int(lengthTxt)
miarka = ""

for i in range(length):
    miarka += "|...."
miarka += "|\n0"

for i in range(length):
    miarka += str(i + 1).rjust(5)

print(miarka)
