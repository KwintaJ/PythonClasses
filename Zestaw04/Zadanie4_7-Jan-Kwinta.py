#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.7             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

def flatRec(flatList, S):
    if not isinstance(S, (list, tuple)):
        flatList.append(S)
    else:
        for i in S:
            flatRec(flatList, i)

def flatten(S):
    flatList = []
    for i in S:
        flatRec(flatList, i)
    return flatList

Seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Sekwencja:")
print(Seq)
print()
print("Sekwencja po splaszczeniu:")
print(flatten(Seq))
