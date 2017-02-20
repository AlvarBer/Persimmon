Implementation
==============

How does it actually work?
--------------------------
A graph is drawn on screen using the provided blocks and their respective
connections (called pins). Pins on the left side of a block are called
input pins and each must come from a single output pin. Pins on the right side
are called output pins and one can be connected to multiple input pins.

<!-- Talk about compilation, topological sort and abstract syntax tree. -->
Then when the user press play this graph is sent to the backend,
where, starting from a random block, the backend tries to execute the
current block function and send the result towards the output pins, if an input
pin from a non-executed block is detected this block is executed first and
recursively.

![Graph Execution algorithm](images/graph_execution.pdf)


This algorithm is the most important piece of code, and is independent of
the view.


First Iteration
---------------
![Sketch of the first interface](images/sketch_1.png)

For the first iteration the priority was to get a proof of concept in order to
see where the difficulties can appear, with a few simple classifiers and
cross-validation techniques. As such a button-based interface with very limited
workflow creation was chosen.

The chosen classifiers were simple and well-understood methods such as K-Nearest
Neighbors, Logistic Regression, Naive Bayes, Support Vector Machines and Random
Forest, which a slightly more complex method that involves ensemble of Decision
Trees, but gives good results in wide variety of problems.

Apart from the temporary interface the backend had to be built, because only
the simplest workflows were being supported no remarkable difficulties were
found. However estimators were limited to classifiers only, as including
regressors and clusterings complicated things since interfaces are not
compatible.

![Implementation of the first interface](images/interface.png)


Second Iteration
----------------
![Sketch of the second interface](images/sketch_2.png)

For the second interface the drag and drop feel was the main priority.
As such after developing th tab panel draggable boxes were developed, with these
connections could be made using the pins on them, the logic behind the pins and
the blocks is quite heavy, as there is a tight coupling between the *Blackboard*
(The underlying canvas were boxed are drop and dragged), the Blocks themselves
and the pins on the blocks, as all of these parts relay information to each
other while the user is dragging a cable between two pins.

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

This way we reduce coupling as much as possible, enabling swapping
the current kivy framework for another one by just changed the view, no
modifications to the backend.

For more information about internal package distribution check appendix A.


[^MVC]: Model View Controller is a software pattern.
[^Numba]: Numba is a python library that allows the compilation and jitting of
    functions into both the CPU and the GPU
    [http://numba.pydata.org/](http://numba.pydata.org/)
