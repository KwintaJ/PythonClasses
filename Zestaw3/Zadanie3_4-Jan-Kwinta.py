#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.4             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

while True:
    reply = input("Wpisz liczbe:")
    if reply == "stop":
        break
        
    if reply.count('.') > 1 or reply.count('-') > 1:
        print("To nie jest liczba!")
    elif reply.count('-') == 1 and not reply.startswith('-'):
        print("To nie jest liczba!")
    elif not ((reply.replace('.', '0')).replace('-', '1')).isdecimal():
        print("To nie jest liczba!")
    else:
        print(reply + "^3 = " + str(float(reply) ** 3))
