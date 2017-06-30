from persimmon.view.pins import InputPin, OutputPin
from persimmon.view.blocks.block import Block  # MYPY HACK

from kivy.properties import ObjectProperty
from kivy.lang import Builder

from sklearn.model_selection import cross_val_score


Builder.load_file('persimmon/view/blocks/crossvalidationblock.kv')

class CrossValidationBlock(Block):
    data_input = ObjectProperty()
    estimator_input = ObjectProperty()
    cross_val_input = ObjectProperty()
    cross_out = ObjectProperty()


    def function(self):
        X = self.data_input.val.iloc[:, :-1]
        y = self.data_input.val.iloc[:, -1]
        self.cross_out.val = cross_val_score(self.estimator_input.val, X,
                                             y,
                                             cv=self.cross_val_input.val)
