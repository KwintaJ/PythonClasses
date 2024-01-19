######################################
#  Jan Kwinta            02.01.2024  #
#                                    #
#        Projekt zaliczeniowy        #
#    Plik do testowania ConvexHull   #
#                                    #
######################################

# !/usr/bin/env/python
# coding = utf-8
from points import Point
from HullModule import ConvexHull
from ReadPointsFileModule import read_points_from_file

def test_convex_hull(input_path, expected_output_path):
    points_list = read_points_from_file(input_path)
    expected_output = read_points_from_file(expected_output_path)

    if points_list is None or expected_output is None:
        return False

    convex_hull = ConvexHull(points_list)
    hull_points = convex_hull.getHull()

    return hull_points == expected_output

if __name__ == "__main__":
    for i in range(11):
        input_file_path = f'../tests/in/{i}.in'
        output_file_path = f'../tests/out/{i}.out'

        if test_convex_hull(input_file_path, output_file_path):
            print(f'Test {i}: PASS')
        else:
            print(f'Test {i}: FAIL')
