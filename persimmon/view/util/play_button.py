from kivy.uix.image import Image, AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.loader import Loader
from kivy.graphics.context_instructions import Rotate, PushMatrix, PopMatrix


Builder.load_file('persimmon/view/util/play_button.kv')

class PlayButton(ButtonBehavior, AsyncImage):
    angle = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'persimmon/play.png'
        self.anim = Animation(angle=360, duration=2)
        self.anim += Animation(angle=360, duration=2)
        self.anim.repeat = True
        self.running = False

    def on_press(self):
        self.source = 'persimmon/play_blue.png'

    def start(self):
        self.running = True
        self.anim.start(self)
        self.source = 'persimmon/cog.png'
        self.disabled = True

    def ready(self):
        self.anim.cancel(self)
        self.disabled = False
        self.source = 'persimmon/play.png'
        self.angle = 0

    def on_angle(self, instance, values):
        """ Only needed so spinner goes after 360. """
        self.angle %= 360

