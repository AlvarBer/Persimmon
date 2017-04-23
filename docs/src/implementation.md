Implementation
==============

On this chapter the implementation of the system is detailed, explained what
was done in each iteration.
After the iterations Persimmon intermediate representation is explained.
Finally, some of the most complex technical problems along their respective
solutions are detailed.


First Iteration
---------------
![Implementation of the first interface](images/interface.png)

For the first iteration, the priority was to get a proof of concept in order to
see where the difficulties can appear, with a few simple classifiers and
cross-validation techniques. As such a button-based interface with very limited
workflow creation was chosen.

The chosen classifiers were simple and well-understood methods such as K-Nearest
Neighbors, Logistic Regression, Naive Bayes, Support Vector Machines and Random
Forest, which a slightly more complex method that involves ensemble of Decision
Trees, but gives good results in wide variety of problems.

All these classifiers have few parameters on their respective sklearn
implementations, and for this prototype the interface did not allow modifying
any of them, as the it would have cluttered and it was not a necessary feature.
Also, all of them are classifiers, as it simplifies the interface, since
regression and clustering have some incompatibilities.

Apart from the temporary interface the backend had to be built. Since the
workflow was fixed the backend simply received the node as arguments and
executed those, meaning the previously explained execution algorithm was not
needed for this iteration.


Second Iteration
----------------
For the second iteration the drag and drop feel was the main priority.
As such after developing the tab panel draggable boxes were developed, these
boxes needed to be connected through pins.
The logic behind the pins and the blocks is quite heavy, as there is a tight
coupling between the blackboard[^blackboard], blocks and the pins on them, as
all of these parts relay information to each other while the user is
dragging a cable between two pins, this is further explained on the "Making a
connection" section.

![Second iteration implementation](images/iter2.png)

This tight coupling means there is a noticeable lag when moving the cable too
fast on low-end computers, there are several solutions to this, but the most
convenient is optimizing the method. If more optimization is needed for this
particular function tools such as `Numba`[^Numba] or `Cython` could be used.

Third Iteration
---------------
For the third and final iteration, the focus was on improving the visual aspect,
adding helpful aids to the user experience.
The main addition being adding a notification systems that gives feedback to
the user about the outcome of their actions and the type systems that prevents
creating malformed pipelines.
Other minor improvements to the system were the addition of a warning when
the intended connection is not possible, by changing the color line to red, and
a warning showing up when a block has only some of their inputs connected.

![Third iteration interface showing a warning](images/iter3.png)


Model View Controller
---------------------
Since the beginning of development separation of logic and presentation has
been a priority. For this reason, the Model View Controller[^MVC] pattern has
been applied, separating Model (represented by the subpackage backend), View
(represented by the `.py` files on view subpackage) and Controller
(corresponding to the `.kv` files on view subpackage).

This way coupling is kept as minimal as possible, enabling swapping
the current kivy framework for another one by just changed the view, no
modifications to the backend needed.

In order to avoid repetition extensive use of classes coupled with reusable
custom kivy Widgets were used. This for example meant that each individual pin
on each block is a class, this proved useful for defining matching pins in
different blocks (like when connection a pin that sends data to a pin that
receives it).

For more information about internal package distribution check appendix A.


Making a Connection
-------------------
One of the most complex parts of the system is starting, reconnecting and
deleting a connection between blocks, it involves several actors, asynchronous
callbacks and a very strong coupling between all elements.

![Widget Tree](images/hierarchical.pdf)

In order to understand how connections are made it is necessary to understand
how `Kivy` handles input.
At surface level `Kivy` follows the traditional event-based input management,
with the event propagating downwards from the root.
However, while traditionally inputs events are only passed down to components
that are on the event position `Kivy` passes the events to almost all children
by default, this is done because in phones (one of `Kivy` targets is Android)
gestures tend to start outside the actual widget they intend to affect.

On `Kivy` there are three main inputs events, `on_touch_down` that gets called
when a key is is pressed, `on_touch_move` that is notified when the touch is
moved, i.e. a finger moves across the screen, or on this cases when the mouse
moves, and `on_touch_up` that is fired when the touch is released.

Let's represent the possible actions as use cases, the outer \* represents
`on_touch_down`, - represents `on_touch_move`, and the inner \* `on_touch_up`:

* (On pin) Start a connection.
* (On connection) Modify a connection.
    - Follow cursor.
    - (On pin) Type check.
        * (On a pin) Establish connection if possible.
        * (Elsewhere) Remove connection.

Logic is split in two big cases, creating a connection and modifying an
existing one.
Creating a connection involves creating one end of the connection, both
visually and logically and preparing the line that will follow the cursor.
On the other hand, modifying a connection means removing the end that is being
touched.
These two cases can be handled by different classes, pin on the first case and
connection for the last.
Moving and finishing the connection use the same code for both.

![Connections between elements](images/logical.pdf)

Without getting too deep into implementation details, ends cannot just be
removed, there are visual binds that have to be unbinded and removed from the
canvas, and when a connection is destroyed (this only happens inside
`on_touch_up`, but it can be either the pins or the blackboard `on_touch_up`
depending if the connection is destroyed because the pin violates type safety
or there is no pin under the cursor respectively) it has to unbind the logical
connections of the pins themselves.
For this reason, connection has high-level functions that do the unbind, rebind
and deletion of ends, as long as the necessary elements are passed (dependency
injection pattern).

This is the reconnecting logic, notice how the reconnecting is *forward* or
*backwards* depending on which edge the touch has happened, of course if neither
has been touched the touch event is not handled.


~~~python
def on_touch_down(self, touch):
    """ On touch down on connection means we are modifying an already
        existing connection, not creating a new one. """
    if self.start.collide_point(*touch.pos):
        self.forward = False
        self.unbind_pin(self.start)
        self.uncircle_pin(self.start)
        self.start.on_connection_delete(self)
        touch.ud['cur_line'] = self
        self.start = None
        return True
    elif self.end.collide_point(*touch.pos):
        self.forward = True
        self.unbind_pin(self.end)
        self.uncircle_pin(self.end)
        self.end.on_connection_delete(self)
        touch.ud['cur_line'] = self
        self.end = None
        return True
    else:
        return False
~~~
\begin{figure}
\caption{Connection modification handling}
\end{figure}

Visualizing the Data Flow
-------------------------
One of the latest features that made it into Persimmon is the visualization
of the data flowing through the cables between blocks, this was an interesting
technical problem, since it involving relaying data back from the backend into
the frontend (previously the communication between front and backend was
unidirectional).
But in order to preserve the decoupling between both the backend IR had to
remain untouched.
For this reason it was decided that the backend has an event where it announces
it has finished executing a block and the frontend has to subscribe to it.

But the frontend does not receive the block, only the hash, since that is all
the backend has, and it has to compare with all block hashes to find the actual
block.

After this, the backend has to make the outgoing connections of that block
pulse, meaning for example changing the value of the width of the line between
certain values, a function that works well for this is the sin function.
The tricky part is that each time the function is called it has to remember the
previous value in order to grow or decrease the width accordingly, this cannot
be done on a regular function since using `sleep` would freeze the entire
application, and the best way to maintain state between executions is using a
generator (also known as semi-coroutines).

But what happens when coroutine needs to be stopped from being called? Kivy
has a mechanism where if the scheduled function returns `False` it will stop
calling, by default our coroutine does not return any meaningful value, but
it is possible to yield a final `False` that will stop the calls.
But how is that yield triggered? The proper solution solution is using
a full coroutine (either a generator-based one of the newer asyncio ones), but
then concurrency issues appears, such that since the coroutine is being called
20 times per second if the coroutine is called while it is executing the
scheduled interval it will ignore the second call.

The solutions comes from executions, similar to a fast interrupt in hardware it
is possible to throw a execution on a coroutine that (maybe) is running, this
also mean that the throwing hijacks the current execution, leading to two
different returns needed, one for the interrupt execution and another for the
previous running execution (if it was running, if not it will be on the next
scheduled call).

With the throw solution there is no need for a full coroutine anymore, and a
generator can be used again.

~~~python
def pulse(self):
    self.it = self._change_width()  # Create iterator
    Clock.schedule_interval(lambda _: next(self.it), 0.05) # 20 FPS

def stop_pulse(self):
    self.it.throw(StopIteration)  # Hijacking execution

def _change_width(self):
    try:
        for value in self._width_gen():
            self.lin.width = value
            yield
    except StopIteration:
        self.lin.width = 2  # Return width back to default
        yield  # This yield is for the hijacking execution
        yield False  # And this for the regular execution

def _width_gen(self):
    """ Infinity oscillating generator (between 2 and 6) """
    val = 0
    while True:
        yield 2 * np.sin(val) + 4
        val += pi / 20
~~~


Binary Distribution
-------------------
The interpretative nature of Python does not make creating an executable binary
easy, particularly `cPython` the standard implementation and reference provides
no tooling to create an executable binary.

For this task `PyInstaller` was chosen, the process of creating a binary is
mostly automated, given a script it tries to read the imports and include them,
finally it embeds a small interpreter to run this code.
The problem with this approach is that Python allows for alternative ways of
importing, it also breaks resource loading at execution time (since it has to
create a temporary folder). This results in manually specifying hidden
dependencies and non python files (on this case mostly `kv` files).

Unfortunately, this process has to be done on a windows system, and as such
cannot be done on the CI[^CI] server, to see how Persimmon utilizes CI check
the appendix B.


[^blackboard]: Blackboard is where the blocks and connections reside.
[^MVC]: Model View Controller is a software pattern.
[^Numba]: Numba is a python library that allows the compilation and jitting of
    functions into both the CPU and the GPU
    [http://numba.pydata.org/](http://numba.pydata.org/)
[^Map]: A Map is Haskell is called a dictionary in Python and Hashtable in other
    languages. It represents a data structure in which keys are used to
    retrieve values in a very efficient manner (on hashmap $\mathcal{O}(1)$).
[^CI]: Continuous Integration is a term that refers to the idea of testing,
    building, generating documentation and even deploying automatically through
    a commit on the version control system.
