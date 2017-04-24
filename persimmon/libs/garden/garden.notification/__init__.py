'''
# Copyright (c) 2013 Peter Badida (KeyWeeUsr)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

.. |notification| replace:: notification
.. _notification: https://developer.mozilla.org/en-US/docs/Web/API/notification

This widget provides a browser-like |notification|_ with all of the Kivy
features available. You can use it either in its default state, where is
only basic title and message with some of the color configuration, or
you can input your own message layout in kv language. The message string
is available through ``app.message`` property.

Features:
- message scrolls
- available icon option
- title will be shortened if too long
- callback after the notification disappears
- stacking multiple notifs on top of each other
- markup turned on in title and message by default
- kv language input

TODO:
- Ubuntu's Unity & OSX window hide implementation
  (needed for hiding the window another python interpreter creates)
- grab window focus back - each notification steals focus from the main window
  (linux & OSX)
- position relatively to the taskbar (or at least not on top of it)
- forbid notification to print Kivy initialisation logs to output
  unless asked for it
'''

import os
import sys
import threading
from subprocess import Popen
from os.path import dirname, abspath, join
from kivy.app import App


class Notification(object):
    def open(self, title='Title', message='Message', icon=None,
             width=300, height=100, offset_x=10, offset_y=40,
             timeout=15, timeout_close=True, color=None,
             line_color=None, background_color=None, parent_title=None,
             stack=True, stack_offset_y=10, on_stop=None, kv=None):

        app = App.get_running_app()

        # set default colors
        if not color:
            color = (0, 0, 0, 1)
        if not line_color:
            line_color = (.2, .64, .81, .5)
        if not background_color:
            background_color = (.92, .92, .92, 1)

        # stacking on top of each other
        if stack and not hasattr(app, '_gardennotification_count'):
            app._gardennotification_count = 1
        elif stack and hasattr(app, '_gardennotification_count'):
            inc = app._gardennotification_count
            app._gardennotification_count += 1
            offset_y += (height + stack_offset_y) * inc
        else:
            app._gardennotification_count = 0

        # Window name necessary for win32 api
        if not parent_title:
            parent_title = app.get_application_name()

        self.path = dirname(abspath(__file__))

        # subprocess callback after the App dies
        def popen_back(callback, on_stop, args):
            # str(dict) is used for passing arguments to the child notification
            # it might trigger an issue on some OS if a length of X characters
            # is exceeded in the called console string, e.g. too long path
            # to the interpreter executable, notification file, etc.
            # https://support.microsoft.com/en-us/help/830473
            os.environ['KIVY_NO_FILELOG'] = '1'
            p = Popen([
                sys.executable,
                join(self.path, 'notification.py'),
                args
            ])
            p.wait()
            callback()
            if on_stop:
                on_stop()
            return

        # open Popen in Thread to wait for exit status
        # then decrement the stacking variable
        t = threading.Thread(
            target=popen_back, args=(
                self._decrement,
                on_stop,
                str({
                    'title': title,
                    'message': message,
                    'icon': icon,
                    'kv': kv,
                    'width': width,
                    'height': height,
                    'offset_x': offset_x,
                    'offset_y': offset_y,
                    'timeout': timeout,
                    'timeout_close': timeout_close,
                    'line_color': line_color,
                    'color': color,
                    'background_color': background_color,
                    'parent_title': parent_title,
                })))
        t.start()

    def _decrement(self):
        app = App.get_running_app()
        if hasattr(app, '_gardennotification_count'):
            app._gardennotification_count -= 1
