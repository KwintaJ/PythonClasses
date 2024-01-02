#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.3             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

l = input("Podaj liczbe naturalna n: ")
if not l.isdigit():
    print("To nie jest liczba naturalna!")
    exit()

print("n! = " + str(factorial(int(l))))
