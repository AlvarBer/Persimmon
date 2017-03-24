from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from copy import deepcopy


kv = """
BoxLayout:
    orientation: 'vertical'
    id: r00t
    TabbedPanel:
        size_hint_y: 20
        do_default_tab: False
        tab_width: '200dp'
        TabbedPanelItem:
            text: 'I/O'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                DragableThing:
                    text: '.csv ->'
                    valid_backdrop: root
                DragableThing:
                    text: '-> .csv'
        TabbedPanelItem:
            text: 'Estimators'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                DragableThing:
                    text: 'Log reg'
                DragableThing:
                    text: 'Rand Forest'
        TabbedPanelItem:
            text: 'Cross Validation'
            BoxLayout:
                spacing: '15dp'
                padding: '15dp'
                DragableThing:
                    text: 'K-Folds'
    Label:
        size_hint_y: 80
        text: 'Content'

<DragableThing>:
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0
    #valid_backdrop: valid_backdrop
    canvas.before:
        Color:
            rgb: .5, .5, .5
        Rectangle:
            pos: self.pos
            size: self.size
"""

class SpawnTabPanelApp(App):
    def build(self):
        return Builder.load_string(kv)

class DragableThing(DragBehavior, Label):
    valid_backdrop = ObjectProperty()
    """
    def on_touch_down(self, touch):
        old_par, old_idx = self.parent, self.parent.children.index(self)
        self.parent.remove_widget(self)
        print(self)
        print('>>>')
        old_par.add_widget(deepcopy(self), index=old_idx)
        print(self.valid_backdrop)
        self.valid_backdrop.add_widget(self)
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            pass
            #self.parent.remove_widget(self)
    """
    def __deepcopy__(self, dumb):
        return DragableThing(text=self.text,
                             drag_rectangle=self.drag_rectangle,
                             drag_timeout=self.drag_timeout,
                             drag_distance=self.drag_distance)

if __name__ == '__main__':
    SpawnTabPanelApp().run()
