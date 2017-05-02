import sys
if hasattr(sys, '_MEIPASS'):
    import os
    os.chdir(sys._MEIPASS)
import logging
logging.basicConfig(level=logging.INFO)
from persimmon.view import ViewApp

ViewApp().run()
