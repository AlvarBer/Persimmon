import sys
if (len(sys.argv) > 1 and
    (sys.argv[1] == '-d' or sys.argv[1] == '--debug')):
    import coloredlogs
    coloredlogs.DEFAULT_DATE_FORMAT = '%H:%M:%S'
    coloredlogs.DEFAULT_LOG_FORMAT = '[%(asctime)s] %(name)s - %(message)s'
    coloredlogs.install(level='DEBUG')
if hasattr(sys, '_MEIPASS'):
    import os
    os.chdir(sys._MEIPASS)
from persimmon.view import ViewApp

ViewApp().run()
