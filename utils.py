import math


def dist(pt1, pt2):
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))