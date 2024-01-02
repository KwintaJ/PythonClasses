#####################################
#                                   #
#  Zestaw 4             03.11.2023  #
#                                   #
#           Zadanie 4.5             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

def odwracanieRekurencyjne(L, left, right):
    if left >= right:
        return

    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    
    odwracanieRekurencyjne(L, left + 1, right - 1)
    return

def odwracanieIteracyjne(L, left, right):
    for i in range(left, int(right / 2) + 1):
        temp = L[i]
        L[i] = L[right - (i - left)]
        L[right - (i - left)] = temp
    return


Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Poczatkowa lista:")
print(Lista)
print()

odwracanieRekurencyjne(Lista, 3, 7)
print("Lista po wykonaniu odwracanie(3, 7) rekurencyjnie:")
print(Lista)
print()

odwracanieIteracyjne(Lista, 1, 4)
print("Lista po wykonaniu odwracanie(1, 4) iteracyjnie:")
print(Lista)
print()

