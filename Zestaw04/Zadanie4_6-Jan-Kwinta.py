#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.6             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

def sum_seq(S):
    if not isinstance(S, (list, tuple)):
        return S

    out = 0
    for i in S:
        out += sum_seq(i)

    return out

Seq = [6, 4, (4, 5, 1), [5, [3, 4], (1, 0)], [], (1, [2, 4, (1, 5, 3, 1)], 0)]
print("Sekwencja:")
print(Seq)
print()
print("Suma wszystkich liczb w niej zawartych jest rowna " + str(sum_seq(Seq)))
