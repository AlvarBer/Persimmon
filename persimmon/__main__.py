import os
import sys
if hasattr(sys, '_MEIPASS') or getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
from persimmon.view import ViewApp


ViewApp().run()
