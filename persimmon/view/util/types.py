from enum import Enum


class Type(Enum):
    ANY = 0.9, 0.9, 0.9
    DATAFRAME = .667, .224, .224
    CLASSIFICATOR = .667, .424, .224
    CROSS_VALIDATOR = .133, .4, .4

