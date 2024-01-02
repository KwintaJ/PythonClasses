#####################################
#                                   #
#  Zestaw 11            02.01.2024  #
#                                   #
#           Zadanie 11.2            #
#          Plik testujacy           #
#         klase SingleList          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8
from SingleLists import SingleList, Node

# Tworzenie listy
my_list = SingleList()

# Dodawanie elementów na różne sposoby
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

my_list.insert_head(node1)
my_list.insert_tail(node2)
my_list.insert_tail(node3)

# Wyświetlanie listy
print("Initial list:", my_list)

# Szukanie elementu
searched_node = my_list.search(20)
if searched_node:
    print("Found node:", searched_node)
else:
    print("Node not found")

# Znajdowanie maksimum i minimum
max_node = my_list.find_max()
min_node = my_list.find_min()

print("Max node:", max_node)
print("Min node:", min_node)

# Odwracanie listy
my_list.reverse()
print("Reversed list:", my_list)