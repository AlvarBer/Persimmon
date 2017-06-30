from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
import kivy.uix.filechooser


Builder.load_file('persimmon/view/util/filedialog.kv')

# TODO: firx for write csv
class FileDialog(Popup):
    """File Dialogs is a popup that gets a file"""
    file_chooser = ObjectProperty()
    #tinput = ObjectProperty()
    load_button = ObjectProperty()
    file_chosen = StringProperty()

    def __init__(self, dir='~', filters=None, **kwargs):
        super().__init__(**kwargs)
        self.file_chooser.path = dir
        if filters:
            self.file_chooser.filters=filters
        else:
            self.file_chooser.filters=[]

    def toggle_load_button(self, selection):
        if selection:
            #self.file_chosen = self.file_chooser.selection[0]
            self.tinput.text = self.file_chooser.selection[0]
            self.load_button.disabled = False
        elif self.tinput.text:
            self.load_button.disabled = False
        else:
            self.load_button.disabled = True

    def changed_dir(self, file_chooser, entry, _):
        #self.file_chosen = file_chooser.path
        self.tinput.text = file_chooser.path

