#####################################
#                                   #
#  Zestaw 2             17.10.2023  #
#                                   #
#        Zadania 2.10 - 2.19        #
#                                   #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################

# !/usr/bin/env/python
# coding = utf-8

line = """Lorem ipsum dolor\tsit amet,\nconsectetur adipiscing elit,\nGvR\nsed\tdo eiusmod tempor incididunt\nut labore et dolore magna aliqua."""
print(line)


# Zadanie 2.10
words = line.split()

print()
print('Zadanie 2.10')
print('Liczba wyrazow w napisie jest rowna: ' + str(len(words)))


# Zadanie 2.11
word = words[6]
w_o_r_d = word[0]
for i in range(1, len(word)):
    w_o_r_d += "_"
    w_o_r_d += word[i]

print()
print('Zadanie 2.11')
print(w_o_r_d)


# Zadanie 2.12
wordFirst = ""
wordLast = ""
for i in range(len(words)):
    wordFirst += words[i][0]
    wordLast += words[i][len(words[i]) - 1]

print()
print('Zadanie 2.12')
print(wordFirst)
print(wordLast)


# Zadanie 2.13
wordsLength = [len(words[i]) for i in range(len(words))]

print()
print('Zadanie 2.13')
print('Laczna dlugosc wyrazow wynosi: ' + str(sum(wordsLength)))

# Zadanie 2.14
print()
print('Zadanie 2.14')
print('(a) Najdluzszym wyrazem jest: ' + words[wordsLength.index(max(wordsLength))])
print('(b) Jego dlugosc wynosi: ' + str(max(wordsLength)))


# Zadanie 2.15
L = [120, 491, 502, 1, 456, 999, 26, 551, 700, 4, 78, 91, 67]
napisL = ""
for i in L:
    napisL += str(i)

print()
print('Zadanie 2.15')
print(napisL)


# Zadanie 2.16
line = line.replace("GvR", "Guido van Rossum")

print()
print('Zadanie 2.16')
print(line)


# Zadanie 2.17
words = line.split()
words.sort(key = str.lower)

print()
print('Zadanie 2.17')
print(words)

words.sort(key = len)

print()
print(words)


# Zadanie 2.18
N = 1120398471027836051203000
napisN = str(N)
zeroCount = 0

for i in napisN:
    if i == '0':
        zeroCount += 1

print()
print('Zadanie 2.18')
print('W liczbie ' + napisN + ' znajduje sie ' + str(zeroCount) + ' zer.')


# Zadanie 2.19
napisL = ""
for i in L:
    napisL += str(i).zfill(3)

print()
print('Zadanie 2.19')
print(napisL)
