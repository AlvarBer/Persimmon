Implementation
==============

The system is implemented in python, using the `Kivy` framework for the
frontend and multiple scientific tools such as `Numpy`, `Scipy`, `Pandas` and
most important `scikit-learn` for the backend.


First Iteration
---------------
For the first iteration the priority was to get a proof of concept in order to
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
Also all of them are classifiers, as it simplifies the interface, since
regressors and clustering have some incompatibilities.

Apart from the temporary interface the backend had to be built. Since the
workflow was fixed the backend simply received the node as arguments and
executed those, menaing the previously explained execution algorithm was not
needed for this iteration.

![Implementation of the first interface](images/interface.png)


Second Iteration
----------------
For the second interface the drag and drop feel was the main priority.
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


Model View Controller
---------------------
Since the beginning of development separation of logic and presentation has
been a priority. For this matter the Model View Controller[^MVC] pattern has
been applied, separating Model (represented by the subpackage backend), View
(represented by the `.py` files on view subpackage) and Controller
(corresponding to the `.kv` files on view subpackage).

This way coupling is kept as minimal as possible, enabling swapping
the current kivy framework for another one by just changed the view, no
modifications to the backend needed.

In order to avoid repetition extensive use of classes coupled with reusable
custom kivy Widgets was used. This for example meant that each individual pin
on each block is a class, this proved useful for defining matching pins in
different blocks (Like when connection a pin that sends data to a pin that
receives it).

For more information about internal package distribution check appendix A.


Making a Connection
-------------------
One of the most complex part of the system is starting, reconnecting and
deleting a connection between blocks, it involves several actors, asynchronous
callbacks and a very strong coupling between all elements.

![Widget Tree](images/hierarchical.pdf)

In order to understand how connections are made it is necessary to understand
how `Kivy` handles input.
At surface level `Kivy` follows the traditional event-based input management,
with the event propagating downwards from the root.
However while traditionally inputs events are only passed down to components
that are on the event position `Kivy` passes the events to almost all children
by default, this is done because in phones (one of `Kivy` targets is Android)
gestures tend to start outside the actual widget they intend to affect.

On `Kivy` there are three main inputs events, `on_touch_down` that gets called
when a key is is pressed, `on_touch_move` that is notified when the touch is
moved, i.e. a finger moves across the screen, or on this cases when the mouse
moves, and `on_touch_up` that is fired when the touch is released.

Lets represent the possible actions as use cases, the outer \* represents
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
On the other hand modifying a connection means removing the end that is being
touched.
This two cases can be handled by different classes, pin on the first case and
connection for the last.
Moving and finishing the connection use the same code for both.

<!-- Add connection diagram -->
Without getting too deep into implementation details, ends cannot just be
removed, there are visual binds that have to be unbinded and removed from the
canvas, and when a connection is destroyed (this only happens inside
`on_touch_up`, but it can be either the pins or the blackboard `on_touch_up`
depending if the connection is destroyed because the pin violates type safety
or there is no pin under the cursor respectively) it has to unbind the logical
connections of the pins themselves.
For this reason connection has high-level functions that do the unbind, rebind
and deletion of ends, as long as the necessary elements are passed (dependency
injection pattern).

![Connections between elements](images/logical.pdf)


Intermediate Representation
---------------------------
The visual blocks represent a visual-dataflow language, however the backend
uses a simpler representation of the relations between the blocks, this in turn
helps decoupling backend and frontend.

The frontend blocks are translated on function `to_ir`, which merely performs
trivial transformations to achieve the desired intermediate representation
desired and runs on $\mathcal{O}(n)$ with n being the number of pins.

Let's represent the types on a more strongly typed language than Python.

~~~haskell
type Id = Int -- The hash is an integer
data Inputs = Inputs {origin :: Id, block :: Id}
data Blocks = Blocks {inputs :: [Id], function :: IO a -> IO a,
                      outputs :: [Id]}
data Outputs = Outputs {destinations :: [Id], block :: Id}
data IR = IR {inputs :: Map Id Inputs, blocks :: Map Id Blocks,
              outputs :: Map Id Outputs}
~~~

As we can see on the Haskell definition the intermediation representation is
just three Maps[^Map], one for blocks, one for input pins and one for output pins.
But the maps do not contains pins themselves, merely unique hashes (Int on
this case).
This reflects the fact that pins model only relationships, not state.
The only non-hash value on `IR` are the blocks functions.
This functions are indeed impure, but earlier on the literature review it was
established that dataflow programming was mainly side-effect free, so why do
they involve side effects?.

There are actually first two reasons, first on the actual python programs this
types do not exist, at least not on an enforceable way, so when translating
them to Haskell the `function` field represents the "worst case", that is to
say only a few functions will actually end up producing side-effects.
The second and more important reason is that blocks actually execute
themselves, meaning the block function does not has parameters, it relays on
getting the values from the pins values and sets the values of the output
values, leaving us with the work of setting those input pins and retrieving
results from the output pins.

This goes against the previously stated "pins represent relationships, not
state", in fact an alternative implementation was created in which the
function returned a tuple of results, and it's the compiler job to now
associate the output pins to each of the elements on the tuple. This was done
using the same current mechanism, saving into a dictionary, the difference
being that while currently the values appear on the output pins and have to be
moved into the dictionary (or otherwise a reference to the pin itself must be
kept on the dictionary) on this case the values were fed directly to the
algorithm.
However this proved limiting, as code became more complex since more checks have
to be done, there was no obvious advantage and side-effects did not disappeared
but merely were harder to do.

<!-- Talk about function composition -->

Binary Distribution
-------------------
<!-- Talk about CI, PyInstaller, alternatives, etc -->

[^blackboard]: Blackboard is how the canvas where the blocks and connections
    are lay down.
[^MVC]: Model View Controller is a software pattern.
[^Numba]: Numba is a python library that allows the compilation and jitting of
    functions into both the CPU and the GPU
    [http://numba.pydata.org/](http://numba.pydata.org/)
[^Map]: A Map is Haskell is called a dictionary in Python and Hashtable in other
    languages. It represents a data structure in which keys are used to
    retrieve values in a very efficient manner (on hashmap $\mathcal{O}(1)$).
