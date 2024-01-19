######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#     Plik do wyrysowania otoczki    #
#       wypuklej na plaszczyznie     #
#                                    #
######################################

import matplotlib.pyplot as plt
from points import Point
from HullModule import ConvexHull
from ReadPointsFileModule import read_points_from_file

def plot_points(points, hull_points):
    x = [point.x for point in points]
    y = [point.y for point in points]

    plt.scatter(x, y, color='blue', label='Punkty')

    hull_x = [point.x for point in hull_points]
    hull_y = [point.y for point in hull_points]

    plt.scatter(hull_x, hull_y, color='green', label='Otoczka')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Otoczka wypukla na plaszczyznie')
#   plt.legend()
    plt.show()

if __name__ == "__main__":
    input_file_path = '../tests/in/5.in'
    points_list = read_points_from_file(input_file_path)

    if points_list:
        convex_hull = ConvexHull(points_list)
        hull_points = convex_hull.getHull()

    plot_points(points_list, hull_points)
