######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#    Plik do obslugi standardowego   #
#     wejscia i wyjscia ConvexHull   #
#                                    #
######################################

from points import Point
from HullModule import ConvexHull

def read_points_from_input():
    points = []
    print("Podaj pary liczb (x, y) oddzielone spacja. Wpisz 'koniec', aby zakonczyc:")

    while True:
        input_str = input()
        if input_str.lower() == 'koniec':
            break

        try:
            x, y = map(float, input_str.split())
            points.append(Point(x, y))
        except ValueError:
            print("Nieprawidlowy format. Sprobuj ponownie.")

    return points

if __name__ == "__main__":
    points_list = read_points_from_input()

    convex_hull = ConvexHull(points_list)
    hull_points = convex_hull.getHull()

    print("Punkty na otoczce wypuklej:")
    for point in hull_points:
        print(point)