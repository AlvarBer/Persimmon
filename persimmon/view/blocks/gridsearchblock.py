from persimmon.view.blocks.block import Block  # MYPY HACK
from persimmon.view.pins import InputPin, OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder
from sklearn.model_selection import GridSearchCV


Builder.load_file('persimmon/view/blocks/gridsearchblock.kv')

class GridSearchBlock(Block):
    data_in = ObjectProperty()
    est_in = ObjectProperty()
    params_in = ObjectProperty()
    est_out = ObjectProperty()
    score_out = ObjectProperty()

    def function(self):
        results = GridSearchCV(self.est_in.val, self.params_in.val)
        results.fit(self.data_in.val.iloc[:, :-1],
                    self.data_in.val.iloc[:, -1])
        self.est_out.val = results.best_estimator_
        self.score_out.val = (str(results.best_params_) + '->' +
                              str(results.best_score_ * 100) + '%')
