from enum import Enum
from abc import ABCMeta
from kivy.uix.widget import WidgetMetaclass


class AbstractWidget(ABCMeta, WidgetMetaclass):
    """ Necessary because python meta classes do not support multiple
    inheritance. """
    pass

class Type(Enum):
    ANY = 0.9, 0.9, 0.9
    DATAFRAME = .667, .224, .224
    CLASSIFICATOR = .667, .424, .224
    CROSS_VALIDATOR = .133, .4, .4
    STATE = .667, .667, .224
    STR = .408, .624, .608

class BlockType(Enum):
    IO = .667, .224, .224
    CLASSIFICATOR = .667, .424, .224
    MODEL_SELECTION = .176, .533, .176
    CROSS_VALIDATOR = .133, .4, .4
    STATE = .667, .667, .224
    FIT_AND_PREDICT = .345, .165, .447
