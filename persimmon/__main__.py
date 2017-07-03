import sys
import os
if len(sys.argv) > 1 and sys.argv[1] in {'-d', '--debug'}:
    #import coloredlogs
    #coloredlogs.DEFAULT_DATE_FORMAT = '%H:%M:%S'
    #coloredlogs.DEFAULT_LOG_FORMAT = '[%(asctime)s] %(name)s - %(message)s'
    #coloredlogs.install(level='DEBUG')
    import logging
    logging.basicConfig(level=logging.DEBUG)
if sys.platform == 'win32':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
    # If running as executable this is necessary for finding resources
    if hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)  # type: ignore
KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui'))
#print(KV_PATH)
from kivy.resources import resource_add_path
# Necesary for finding .kv files and others
resource_add_path(os.path.dirname(os.path.dirname(__file__)))
from persimmon.view import ViewApp


def main():
    ViewApp().run()


if __name__ == '__main__':
    main()
