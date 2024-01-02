#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.4             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

def fibonacci(n):
    f1 = 1
    fn = 0
    for i in range(n):
        temp = fn
        fn += f1
        f1 = temp
    return fn

l = input("Podaj liczbe naturalna n: ")
if not l.isdigit():
    print("To nie jest liczba naturalna!")
    exit()

print("n-ta liczba Fibonacciego to " + str(fibonacci(int(l))))
