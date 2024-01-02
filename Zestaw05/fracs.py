#####################################
#                                   #
#  Zestaw 5             07.11.2023  #
#                                   #
#           Zadanie 5.2             #
#       Plik z modulem fracs        #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

from math import gcd as Fgcd

def normalize(frac):
    normalizedFrac = [0, 0]
    if frac[0] == 0:
        return normalizedFrac
    normalizedFrac[0] = int(frac[0] / Fgcd(frac[0], frac[1]))
    normalizedFrac[1] = int(frac[1] / Fgcd(frac[0], frac[1]))
    if frac[1] < 0:
        normalizedFrac[0] *= -1
        normalizedFrac[1] *= -1
    return normalizedFrac

def add_frac(frac1, frac2):
    N = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    D = frac1[1] * frac2[1]
    return normalize([N, D])

def sub_frac(frac1, frac2):
    N = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    D = frac1[1] * frac2[1]
    return normalize([N, D])

def mul_frac(frac1, frac2):
    N = frac1[0] * frac2[0]
    D = frac1[1] * frac2[1]
    return normalize([N, D])

def div_frac(frac1, frac2):
    N = frac1[0] * frac2[1]
    D = frac1[1] * frac2[0]
    return normalize([N, D])

def is_positive(frac):
    if frac[0] * frac[1] < 0:
        return False
    return True

def is_zero(frac):
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2):
    A = normalize(frac1)
    B = normalize(frac2)
    if A[0] * B[1] == A[1] * B[0]:
        return 0
    if A[0] * B[1] > A[1] * B[0]:
        return 1
    return -1

def frac2float(frac):
    return float(frac[0] / frac[1])
