#####################################
#                                   #
#  Zestaw 8             05.12.2023  #
#                                   #
#           Zadanie 8.2             #
#          Plik testujacy           #
#          modul triangles          #
#                                   #
#  Jan Kwinta                       #
#                                   #
#####################################
 
# !/usr/bin/env/python
# coding = utf-8
from points import Point
from triangles import Triangle
import pytest

@pytest.fixture
def triangle():
    return Triangle(0, 0, 5, 2, -1, 4)

def test_from_points(triangle):
    point_list = [Point(0, 0), Point(5, 2), Point(-1, 4)]
    other_triangle = Triangle.from_points(point_list)
    assert triangle == other_triangle

def test_center(triangle):
    assert triangle.center == Point(1.3333333333333333, 2)

def test_top(triangle):
    assert triangle.top == 4

def test_left(triangle):
    assert triangle.left == -1

def test_bottom(triangle):
    assert triangle.bottom == 0

def test_right(triangle):
    assert triangle.right == 5

def test_width(triangle):
    assert triangle.width == 6

def test_height(triangle):
    assert triangle.height == 4

def test_topleft(triangle):
    assert triangle.topleft == Point(-1, 4)

def test_bottomleft(triangle):
    assert triangle.bottomleft == Point(-1, 0)

def test_topright(triangle):
    assert triangle.topright == Point(5, 4)

def test_bottomright(triangle):
    assert triangle.bottomright == Point(5, 0)

def test_area(triangle):
    assert triangle.area() == 11.0

def test_move(triangle):
    moved_triangle = triangle.move(1, 1)
    assert moved_triangle == Triangle(1, 1, 6, 3, 0, 5)

if __name__ == '__main__':
    pytest.main()
