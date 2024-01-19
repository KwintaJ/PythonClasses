#############################################################################
#  Jan Kwinta                                                   02.01.2024  #
#  Projekt zaliczeniowy Jezyk Python                       Otoczka wypukla  #
#############################################################################


====================================================================================================
*Zawartosc projektu*

Projekt/─┐                                         | Folder glowny
         ├─scripts/─┐                              | Podfolder ze skryptami
         │          ├─ points.py                   | Plik z modulem Point
         │          ├─ vectors.py                  | Plik z modulem Vector         
         │          ├─ HullModule.py               | Plik z klasa wyznaczajaca otoczke
         │          ├─ StdInOut.py                 | Plik do obslugi klasy ConvexHull
         │          ├─ ReadPointsFileModule.py     | Plik do obslugi plikow
         │          ├─ PlotPoints.py               | Program wyswietlajacy otoczke wypukla
         │          └─ tester.py                   | Plik do testowania ConvexHull.py
         │                                         |
         └─tests/───┐                              | Folder z testami
                    ├─in/──┐                       | | Folder z danymi wejsciowymi
                    │      ├─ 0.in                 | | |
                    │      ├─ 1.in                 | | | Pliki z przygotowanymi 
                    │      ├─ 2.in                 | | | danymi wejsciowymi programu
                    │      └─ ...                  | | | (rozne zbiory punktow)
                    │                              | |
                    └─out/─┐                       | | Folder z wynikami
                           ├─ 0.out                | | |
                           ├─ 1.out                | | | Pliki z wzorcowymi 
                           ├─ 2.out                | | | odpowiedziami to testowania
                           └─ ...                  | | | programu
====================================================================================================


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
