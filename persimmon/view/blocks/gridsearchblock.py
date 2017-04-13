from persimmon.view.blocks import Block
from persimmon.view.util import InputPin, OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder
from sklearn.model_selection import GridSearchCV


Builder.load_file('view/blocks/gridsearchblock.kv')

class GridSearchBlock(Block):
    est_in = ObjectProperty()
    params_in = ObjectProperty()
    est_out = ObjectProperty()
    score_out = ObjectProperty()

    def function(self):
        results = GridSearchCV(self.est_in.val, self.params_in.val,
                               n_jobs=-1)
        self.est_out, self.score_out = (results.best_estimators_,
                                        results.best_score_)
