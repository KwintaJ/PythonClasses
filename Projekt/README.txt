############################################################################
#  Jan Kwinta                                                  02.01.2024  #
#  Projekt zaliczeniowy Jezyk Python                      Otoczka wypukla  #
############################################################################


============================================================================
*Zawartosc projektu*

Projekt/─┐                                | Folder glowny
         ├─scripts/─┐                     | Podfolder ze skryptami
         │          ├─ points.py          | Plik z modulem Point
         │          ├─ vectors.py         | Plik z modulem Vector
         │          ├─ ConvexHull.py      | Plik glowny wyznaczajacy otoczke
         │          └─ tester.py          | Plik do testowania ConvexHull.py
         │                                |
         └─tests/───┐                     | Folder z testami
                    ├─in/──┐              | | Folder z danymi wejsciowymi
                    │      ├─ 0.in        | | |
                    │      ├─ 1.in        | | | Pliki z przygotowanymi 
                    │      ├─ 2.in        | | | danymi wejsciowymi programu
                    │      └─ ...         | | | (rozne zbiory punktow)
                    │                     | |
                    └─out/─┐              | | Folder z wynikami
                           ├─ 0.out       | | |
                           ├─ 1.out       | | | Pliki z wzorcowymi 
                           ├─ 2.out       | | | odpowiedziami to testowania
                           └─ ...         | | | programu
============================================================================


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*Dzialanie programu*

Program ConvexHull.py przyjmuje dowolny zbior punktow jako wejscie i 
wypisuje punkty bedace otoczka wypukla tego zbioru.

Wejsciem programu jest ciag par liczb, z ktorych kazda para to pierwsza i 
druga wspolrzedna kolejnego punktu.

Aby uruchomic program nalezy wykonac komende
    python3 ConvexHull.py
a nastepnie podac zbior punktow w postaci ciagu par liczb.




Aby przetestowac program na danych znajdujacych sie w folderze tests trzeba
wykonac komende 
    python3 tester.py

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
