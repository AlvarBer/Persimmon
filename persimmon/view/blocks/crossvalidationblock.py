from persimmon.view.util import InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder

from sklearn.model_selection import cross_val_score


Builder.load_file('view/blocks/crossvalidationblock.kv')

class CrossValidationBlock(Block):

    def function(self):
        X = self.data_input.val.iloc[:, :-1]
        y = self.data_input.val.iloc[:, -1]
        self.output.val = cross_val_score(self.estimator_input.val, X,
                                          y,
                                          cv=self.cross_val_input.val)
