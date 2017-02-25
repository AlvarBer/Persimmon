Implementation
==============


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

All these classifiers have few parameters on their respective sklearn
implementations, and for this prototype the interface did not allow modifying
any of them, as the it would have cluttered and it was not a necessary feature.
Also all of them are classifiers, as it simplies the interface, since
regressors and clustering have some incompatibilities.

Apart from the temporary interface the backend had to be built. Since the
workflow was fixed the backend simply received the node as arguments and
executed those.
<!-- First backend algorithm? -->

![Implementation of the first interface](images/interface.png)


Second Iteration
----------------
![Sketch of the second interface](images/sketch_2.png)

For the second interface the drag and drop feel was the main priority.
As such after developing the tab panel draggable boxes were developed, these
boxes needed to be connected through pins.
The logic behind the pins and the blocks is quite heavy, as there is a tight
coupling between the blackboard[^blackboard], blocks and the pins on them, as
all of these parts relay information to each other while the user is
dragging a cable between two pins.

This tight coupling means there is a noticeable lag when moving the cable too
fast on low-end computers, there are several solutions to this, but the most
convenient is optimizing the method. If more optimization is needed for this
particular function tools such as `Numba`[^Numba] or `Cython` could be used.

Pins on the left side of a block are called input pins and each must come from
a single output pin. Pins on the right side are called output pins and one can
be connected to multiple input pins.

This kind of programming is called Dataflow Programming, which was already
introduced on the Introduction chapter. Now that we have a directed acyclic
graph, in order to compile and run the program (actually we can theoretically
have multiple parallel programs on the same blackboard) we have to
explore the graph from the input block until the whole graph has been executed.

![Graph Execution algorithm](images/graph_execution.pdf)

The implementation looks each input pin on the block. If the corresponding
value has already been computed (i.e. is already on a hashtable) it is assigned,
if not that block is processed first and then the execution of the current
block resumes. Then the function inside the block is executed and after that
the value of each output pin is saved on the hashtable.

There is an alternative way of doing the compilation, that is using topological
sort on the graph and then the graph can be processed on a single way, no
recursive step is needed, both approaches are $\mathcal{O}(N)$ on both time and
space, more closely they are $\mathcal{O}(n*m)$ where n is the number of nodes
and m the number of edges, since the graph is very sparse we can consider it
a constant factor.

<!-- Appendix on compilation? -->


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

In order to avoid repetition extensive use of classes coupled with reusable
custom kivy Widgets was used. This for example meant that each individual pin
on each block is a class, this proved usefull for defining matching pins in
different blocks (Like when connection a pin that sends data to a pin that
receives it).

For more information about internal package distribution check appendix A.

[^blackboard]: Blackboard is how the canvas where the blocks and connections
    are lay down.
[^MVC]: Model View Controller is a software pattern.
[^Numba]: Numba is a python library that allows the compilation and jitting of
    functions into both the CPU and the GPU
    [http://numba.pydata.org/](http://numba.pydata.org/)
