import sys
if len(sys.argv) > 1 and sys.argv[1] in {'-d', '--debug'}:
    #import coloredlogs
    #coloredlogs.DEFAULT_DATE_FORMAT = '%H:%M:%S'
    #coloredlogs.DEFAULT_LOG_FORMAT = '[%(asctime)s] %(name)s - %(message)s'
    #coloredlogs.install(level='DEBUG')
    import logging
    logging.basicConfig(level=logging.DEBUG)
if hasattr(sys, '_MEIPASS'):
    import os
    os.chdir(sys._MEIPASS)
from persimmon.view import ViewApp

ViewApp().run()
