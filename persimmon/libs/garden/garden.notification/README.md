# garden.notification
:name_badge: A floating popup-like notification

<img src="https://raw.githubusercontent.com/kivy-garden/garden.notification/master/screenshot.png"></img>

This widget provides a browser-like
<a href="https://developer.mozilla.org/en-US/docs/Web/API/notification">
notification</a> with all of the basic Kivy features available. You can use it
either in its default state, where is only basic title and message with some of
the color configuration, or you can input your own message layout in kv
language. The message string is available through ``app.message`` property.
For more such properties, read the code.

## Features:

- message scrolls
- available icon option
- title will be shortened if too long
- callback after the notification disappears
- stacking multiple notifs on top of each other
- markup turned on in title and message by default
- kv language input

## TODO:

- Ubuntu's Unity & OSX window hide implementation
  (needed for hiding the window another python interpreter creates)
- grab window focus back - each notification steals focus from the main window
  (linux & OSX)
- position relatively to the taskbar (or at least not on top of it)
- forbid notification to print Kivy initialisation logs to output
  unless asked for it

## Example:

```
from kivy.app import App
from functools import partial
from kivy.uix.button import Button
from kivy.resources import resource_find
from kivy.garden.notification import Notification


class Notifier(Button):
    def __init__(self, **kwargs):
        super(Notifier, self).__init__(**kwargs)
        self.bind(on_release=self.show_notification)

    def printer(self, *args):
        print(args)

    def show_notification(self, *args):
        # open default notification
        Notification().open(
            title='Kivy Notification',
            message='Hello from the other side?',
            timeout=5,
            icon=resource_find('data/logo/kivy-icon-128.png'),
            on_stop=partial(self.printer, 'Notification closed')
        )

        # open notification with layout in kv
        Notification().open(
            title='Kivy Notification',
            message="I'm a Button!",
            kv="Button:\n    text: app.message"
        )


class KivyNotification(App):
    def build(self):
        return Notifier()


if __name__ == '__main__':
    KivyNotification().run()
```
