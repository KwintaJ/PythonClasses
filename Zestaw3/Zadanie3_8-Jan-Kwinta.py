#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.8             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

seq1 = ["alpha", -2, 3.1415, "nomnom", 0]
seq2 = ["beta", 4, "mlem", 0, 3.1415, 0]

print("Dla dwoch sekwencji:")
print(seq1)
print(seq2)

intersec = []
union = []

for i in seq1:
    if not i in union:
        union.append(i)

for i in seq2:
    if i in seq1 and not i in intersec:
        intersec.append(i)
    if not i in union:
        union.append(i)



print()
print("Ich przeciecie jest rowne:")
print(intersec)
print()
print("Ich suma jest rowna:")
print(union)
