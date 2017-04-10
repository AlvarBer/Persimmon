from persimmon.view.util import Pin, Connection
from kivy.properties import ObjectProperty


class InputPin(Pin):
    origin = ObjectProperty(allownone=True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            print('Creating connection')
            touch.ud['cur_line'] = Connection(start=self,
                                              color=self.color)
            self.origin = touch.ud['cur_line']
            # Add to blackboard
            self.block.parent.add_widget(touch.ud['cur_line'])
            return True
        else:
            return False

    def on_touch_up(self, touch):
        if ('cur_line' in touch.ud.keys() and touch.button == 'left' and
                self.collide_point(*touch.pos)):
            if self.typesafe(touch.ud['cur_line'].end):
                print('Establishing connection')
                touch.ud['cur_line'].finish_connection(self)
                self.origin = touch.ud['cur_line']
            else:
                print('Deleting connection')
                touch.ud['cur_line'].delete_connection(self.parent.parent.parent)
            return True
        else:
            return False

    def on_connection_delete(self, connection):
        self.origin = None

    def typesafe(self, other):
        return super().typesafe(other) and self.origin == None
