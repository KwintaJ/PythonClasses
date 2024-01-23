################################################################################
#  Jan Kwinta                                                      23.01.2024  #
#  Projekt zaliczeniowy Jezyk Python                          Otoczka wypukla  #
################################################################################

================================================================================
*Zawartosc projektu*

Projekt/─┐                               | Folder glowny
         ├─scripts/─┐                    | Podfolder ze skryptami
         │          ├─ points.py         | Plik z modulem Point
         │          ├─ vectors.py        | Plik z modulem Vector
         │          ├─ HullModule.py     | Plik z klasa wyznaczajaca otoczke
         │          ├─ StdInOut.py       | Plik do obslugi klasy ConvexHull
         │          ├─ Read...Module.py  | Plik do obslugi plikow
         │          ├─ PlotPoints.py     | Program wyswietlajacy otoczke wypukla
         │          └─ tester.py         | Plik do testowania ConvexHull.py
         │                               |
         │                               |
         └─tests/───┐                    | Folder z testami
                    ├─in/──┐             | | Folder z danymi wejsciowymi
                    │      ├─ 0.in       | | |
                    │      ├─ 1.in       | | | Pliki z przygotowanymi 
                    │      ├─ 2.in       | | | danymi wejsciowymi programu
                    │      └─ ...        | | | (rozne zbiory punktow)
                    │                    | |
                    └─out/─┐             | | Folder z wynikami
                           ├─ 0.out      | | |
                           ├─ 1.out      | | | Pliki z wzorcowymi 
                           ├─ 2.out      | | | odpowiedziami to testowania
                           └─ ...        | | | programu
================================================================================


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*Dzialanie programu*

Program StdInOut.py tworzy klase ConvexHull i jako argumenty przekazuje jej
dowolny zbior punktow, ktory pobiera z wejscia. Nastepnie przez metode
klasy ConvexHull znajduje punkty bedace otoczka wypukla tego zbioru i
wypisuje je na standardowe wyjscie.

Wejsciem programu jest ciag par liczb, z ktorych kazda para to pierwsza i 
druga wspolrzedna kolejnego punktu.

Aby uruchomic program nalezy wykonac komende:
    python3 StdInOut.py
a nastepnie podac zbior punktow w postaci ciagu par liczb.


Aby przetestowac klase ConvexHull na danych znajdujacych sie w folderze tests 
trzeba wykonac komende:
    python3 tester.py


Aby wyswietlic polozenie punktow na plaszczyznie z zaznaczona otoczka 
wypukla nalezy wykonac:
         python3 PlotPoints.py
Do uruchomienia tego programu wymagana jest biblioteka matplotlib
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


--------------------------------------------------------------------------------
*Opis algorytmu*

W moim projekcie klasa ConvexHull uzywa algorytmu Grahama. 
Agorytm Grahama to efektywny algorytm wyszukiwania otoczki wypuklej skonczonego 
zbioru punktow na plaszczyznie dzialajacy w czasie O(n log(n)), gdzie n jest
liczba punktow w zbiorze.

Przebieg algorytmu jest nastepujący:
  Na poczatku wybieramy punkt o najmniejszej rzednej; jezeli istnieje wiele 
takich punktow wybieramy ten z nich ktory ma najmniejsza odcieta. 
Oznaczmy ten punkt O.
  Pozostale punkty P1, P1, P3... sortujemy wzgledem 1) kata wektora OPi do osi 
poziomej oraz 2) dlugosci odcinka OPi.
  Tworzymy liste dodajac na poczatek posortowanych punktow P punkt O.
  Nastepnie wykonujemy powtarzajac
    Bierzemy trzy poczatkowe jeszcze nieprzetworzone punkty z listy. Oznaczmy te
trojke jako (A, B, C)
    
    

Referencje:
Ronald Graham - "An efficient algorithm for determining the convex hull of a
finite planar set" - "Information Processing Letters"(1972), str. 132–133

wikipedia: https://pl.wikipedia.org/wiki/Algorytm_Grahama

--------------------------------------------------------------------------------