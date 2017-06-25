from persimmon.view.blocks.block import Block
from persimmon.view.pins import OutputPin

from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder


Builder.load_file('persimmon/view/blocks/dictblock.kv')

class DictBlock(Block):
    dict_out = ObjectProperty()
    string_in = StringProperty()
    tinput = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tainted = True
        self.tainted_msg = ('Dictionary not inputed on block {}!'
                            .format(self.title))

    # TODO: Perform this check at unfocus time
    @Block.tainted.getter  # type: ignore  # Soon guido, soon
    def tainted(self):
        try:
            string = eval(self.tinput.text)
            if type(string) == dict:
                self.tainted = False
            else:
                self.tainted = True
                self.tainted_msg = ('Block {} requires a dictionary, not a {}!'
                                    .format(self.title,
                                            type(string).__name__))
        except Exception:
                self.tainted = True
                self.tainted_msg = ('Invalid input on block {}'
                                    .format(self.title))
        return self._tainted

    def function(self):
        self.dict_out.val = eval(self.tinput.text)

