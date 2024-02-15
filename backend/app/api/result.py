from enum import IntEnum

class Result(IntEnum):
    WIN = 1
    LOOSE = 0
    DRAW = 2
    NONE = 3

class CardType(IntEnum):
    Soldier = 1
    Clown = 2
    Knight = 3
    Monk = 4
    Magician = 5
    General = 6
    Minister = 7
    Princess = 8