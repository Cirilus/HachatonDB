from enum import Enum


class RatingChoice(int, Enum):
    A = 100
    A1 = 95
    A2 = 90
    AA = 80
    AA1 = 85
    AA2 = 75
    AAA = 70
    B = 65
    B1 = 60
    B2 = 55
    BB = 50
    BB1 = 45
    BB2 = 40
    BBB = 35
    BBB1 = 30
    BBB2 = 25
    C = 20
