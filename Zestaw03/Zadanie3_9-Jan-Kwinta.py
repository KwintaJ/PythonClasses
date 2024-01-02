#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#           Zadanie 3.9             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

seq = [[], [4], (1, 2), [3,4], (5, 6, 7)]
sumList = []

for i in seq:
    sumList.append(sum(i))
    
print(sumList)
