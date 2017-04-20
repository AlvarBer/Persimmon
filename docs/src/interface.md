Interface Design
================

The main way users interact with the system is trough the visual interface, and
as such is very important that all the information and operations available are
easily accessible on an intuitive manner, removing the need for extensive
training with the software.

Sketches
--------
![Sketch of the first interface](images/sketch_1.png)

On the first interface there was a focus on getting a prototype done as soon as
possible.
For this reason the interface had to be easy to implement and easy to use, with
the few navigations steps required to perform all possible actions as to allow
for quick debugging.
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

Finally on the third iteration the proposed improvements to the interface were:

* Adding a smart bubble[^bubble] that shows the blocks that make sense to spawn
    according to the connection.
* Optional parameters.
* Hide/Toggle parameters.
* Data transfer visualization, meaning that the connection between two blocks
    starts signaling when data from one is moved onto the other.
* Type safety indicator while dragging a connection, such as turning the
    connection cable to a bright red to signal that if the cursor is unpressed
    at that location a connection will not form.
* Make connections bézier curves instead of straight lines.

Some of these points are not realistic goals to be achieved during the short
development time, but they are possible further improvements of the interface.

Colour Palette
--------------
One of the most important parts of the system where colour played a vital role
was connections, symbolizing types with colours.
The relations goes as far as each types has a colour associated with it on
code, meaning that pins are not coloured, their type is specified and their
colour is derived from the type.

The color palette is based on [@stanivcekpaletton], on a tetrad (4-colours)
scheme plus additional primary colours for representing additional types, the
$Any$ colour is represented as almost white to symbolize it is consistent with
any other type.

![Types colors](images/types.pdf)

Typography
----------
The default font for kivy is Roboto, and for a good reason, as one of Kivy
targets is Android, which has Roboto as the most commonly used font.
Roboto is a neo-grotesque sans-serif with a modern robotic feel, it really
feels at home on mobile screens, and it is also used on other Google's products
and websites.
However on the desktop it feels a bit too cold and ubiquitous, as
[John Gruber](http://daringfireball.net/linked/2011/10/19/roboto-v-helvetica)
calls it "Google's Arial'.
The better solution would be platform-dependent, but since Mac default choice,
Helvetica, has trouble rendering in some Window and Linux desktop environments,
Roboto was left as the choice for font rendering.


[^bubble]: A bubble is a form of menu or a small popup where the menu options
    are stacked either vertically or horizontally. They are usually associated
    with the right click action.
