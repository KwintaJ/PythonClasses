#####################################
#                                   #
#  Zestaw 3             24.10.2023  #
#                                   #
#          Zadanie 3.10             #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8

# Funkcja tlumaczaca
def roman2int(N, D):
    Value = 0
    for i in range(len(N)):
        if i == len(N) - 1:
            Value += D[N[i]]
            continue
        if D[N[i]] < D[N[i + 1]]:
            Value -= D[N[i]]
        else:
            Value += D[N[i]]
    return Value


# Tworzenie slownika
# Sposob 1 - explicite
Roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Sposob 2 - petla for
keys = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]
Roman = {}
for (k, v) in zip(keys, values):
    Roman[k] = v

# Sposob 3 - funkcja zip w konstruktorze
keys = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]
Roman = dict(zip(keys, values))

Numeral = input("Wpisz liczbe w zapisie rzymskim:")
print("Jej wartosc wynosi: " + str(roman2int(Numeral, Roman)))
