#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.2             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

# 3.5
def miarka(N):
    m = ""
    
    for i in range(N):
        m += "|...."
    m += "|\n0"

    for i in range(N):
        m += str(i + 1).rjust(5)

    return m

length = input("Podaj dlugosc miarki:")
if not length.isdigit():
    print("To nie jest liczba naturalna!")
    exit()

print(miarka(int(length)))
print()


# 3.6
def prostokat(T, W):
    rowA = "+"
    rowB = "|"

    for i in range(W):
        rowA += "---+"
        rowB += "   |"

    p = rowA

    for i in range(T):
        p += "\n" + rowB + "\n" + rowA

    return p

tall = input("Podaj wysokosc prostokata:")
if not tall.isdigit():
    print("To nie jest liczba naturalna!")
    exit()

wide = input("Podaj szerokosc prostokata:")
if not wide.isdigit():
    print("To nie jest liczba naturalna!")
    exit()
    
print(prostokat(int(tall), int(wide)))
