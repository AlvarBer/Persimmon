Interface Design
================

The main way users interact with the system is trough the visual interface, and
as such is very important that all the information and operations available are
easily accessible on an intuitive manner, removing the need for extensive
training with the software.

Colour Palette
--------------
<!-- Talk about hsv and all that fluff, color brewer 2? -->

Typography
----------
The default font for kivy is Roboto, and for a good reason, as one of Kivy
targets is Android, which has Roboto as the most commonly used font.
Roboto is a neo-grotesque sans-serif with a modern robotic feel, it really
feels at home on mobile screens, and it is also used on other Google's products
and websites.
However on the desktop it feels a bit too cold and ubiquitous, as John Gruber
calls it "Google's Arial'.
The better solution would be platform-dependent, as Mac default choice,
Helvetica, has trouble rendering in some Window and Linux desktop enviroments.
For this reason Roboto was left as the choice for font rendering.


Sketches
--------
![Sketch of the first interface](images/sketch_1.png)

On the first interface there was a focus on getting a model done as soon as
possible. For this reason the interface had to be easy to implement and easy
to use, with the few navigations steps required to perform all possible actions
as to allow for quick debugging.
This meant sacrificing flexibility in favour of usability, because the
algorithms implement were so few the button-based interface worked as intended
for this prototype.
No special considerations were taken for color palettes,
shapes or any other kind of visual aid.

![Sketch of the second interface](images/sketch_2.png)
For the second iteration however the extensibility had to be present, meaning
the old interface was not reusable for the new functionality.
The block based interface gives a lot more of control to the final user, still
some underlying mechanisms such as optional parameters or saving into file were
not present.

<!-- Third interface: drag and drop blocks? Bubble? Code execution
     visualization? Type safety indicators? -->
