from persimmon.view.util import Pin, Connection
from kivy.properties import ObjectProperty, ListProperty


class OutputPin(Pin):
    destinations = ListProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.button == 'left':
            print('Creating connection')
            touch.ud['cur_line'] = Connection(end=self,
                                              color=self.color)
            self.destinations.append(touch.ud['cur_line'])
            # Add to blackboard
            self.block.parent.parent.parent.add_widget(touch.ud['cur_line'])
            return True
        else:
            return False

    def on_touch_up(self, touch):
        #print('on touch up')
        if ('cur_line' in touch.ud.keys() and touch.button == 'left' and
                self.collide_point(*touch.pos)):
            if touch.ud['cur_line'].start and self.typesafe(touch.ud['cur_line'].start):
                print('Establishing connection')
                touch.ud['cur_line'].finish_connection(self)
                self.destinations.append(touch.ud['cur_line'])
            else:
                print('Deleting connection')
                touch.ud['cur_line'].delete_connection(self.block.parent.parent)
            return True
        else:
            return False

    def on_connection_delete(self, connection):
        if connection in self.destinations:
            self.destinations.remove(connection)
        
    def typesafe(self, other):
        return super().typesafe(other)
