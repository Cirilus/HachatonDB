from enum import Enum


class RatingChoice(int, Enum):
    AA = 100
    A = 90
    BB = 80
    B = 70
    CC = 60
    C = 50
    DD = 40
    D = 30
    EE = 20
    E = 10
