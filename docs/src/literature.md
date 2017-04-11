Literature Review
=================


On Visual Programming
---------------------

On Machine Learning
-------------------
Machine Learning [@hughes1968mean].

On Dataflow Programming
-----------------------
After reviewing dataflow seminal paper [@bell], and [@sousa2012dataflow] it was
clear it was necessary to write the compilation algorithm in pseudo code.

There are different ways to implement dataflow programming compilers, for now
let's just consider the language representation as formed by blocks that have
pins.

Pins on the left side of a block are called input pins and each must come from
a single output pin.
Pins on the right side are called output pins and one can be connected to
multiple input pins.

This results in what is effectively a directed acyclic graph, in order to
compile and run the program (actually we can theoretically have multiple
parallel programs on the same blackboard) we have to explore the graph from the
input block until the whole graph has been executed.

![Graph Execution algorithm](images/graph_execution.pdf)

The algorithm looks each input pin on the block.
If the corresponding value has already been computed (i.e. is already on a
hashtable) it is assigned, else that block is processed first and then the
execution of the current block resumes.
Then the function inside the block is executed and after that the value of each
output pin is saved on the hashtable.

There is an alternative way of doing the compilation without needing to check
dependencies when compiling/executing.
Through a topological sort on the graph the graph can be processed "forward
only", no recursive step is needed, both approaches are $\mathcal{O}(N)$, more
closely they are $\mathcal{O}(n*m)$ where n is the number of nodes and m the
number of edges, since the graph is very sparse we can consider it a constant
factor.


State of the art
----------------
Before implementing the system it is necessary to look at existing solutions
on the field of visual programming and visual Machine Learning for
inspiration and avoiding common pitfalls.

![Azure ML Studio web interface](images/azureML.jpg)

Microsoft Azure ML Studio [@barga2015predictive] is one of the most direct
inspirations for this project, it is Microsoft cloud-based platform for
creating predictive analytic solutions on data using a drag and drop interface.

There is plenty to like, lots of different preprocessing steps, multitude of
estimators, runs on the cloud, and a web interface that runs on any platform.
However some of these features are also shortcomings, the web interface feels
basic, especially on the classificators parameters view, lack of native support
means that dragging and dropping do not feel as smooth as they should.
Cloud support is very good, as it integrates with the rest of Microsoft's Azure
platform, but for sensitive data such as financial or medical records a self
hosted version is a must.

The variety of algorithms is interesting, but the limited ability to extend
them is a big shortcoming, azure is written on compiled languages [@azureFAQ],
unlike most ml that is written on either `R` or `Python` [@datasciencelang],
and running custom code is very limited, as scrips are treated as black boxes.
This in turns severely handicaps the extensibility of the given primitives in
any meaningful way.

Weka [@weka] is a popular machine learning suite, written in `Java` and developed at
the University of Waikato. It provides both a command line interface and a
graphical interface.

![Weka Graphical User Interface](images/weka.jpeg)

However it starts to show its age, the interface feels dated and the
composition of algorithms on a graphical is very restricted. Because it is
written on Java it also means that it need the JVM[^JVM], which is a bit of a
con, specially in productions servers where dependencies bring a long and
arduous process of review and approval.


Epic's Unreal Engine 4 [@shah2014mastering] introduced Blueprints as an
alternative to `C++` programming.
It represents all the programming structures as blocks that can be connected,
for example an *"and"* is a block that takes to inputs and returns one output.
Because it provides what is essentially a general-purpose programming language
it has constructs to represent state, because of this it also needs a explicit
flow mechanism, meaning that blocks do not only need to be connected through
data but also by execution order, this is necessary because the order in which
side-effects are performed is important, and many procedures do not return
meaningful values.
<!-- Why is the white line necessary? -->

![Unreal Engine 4 Blueprint system](images/unreal.png)

This provides an intuitive interface, when one cable is dragged from a block
a prompt appears with only the blocks that make sense to be connected to the
previous block.
Another example is how different types are represented by different colors in
both pins and cables, making it easier to predict whether a connection makes
sense or not without even trying to create it.

These small details improve the user experience, making it faster and easier
to use.

<!-- Add more -->

[^JVM]: The Java Virtual Machine is the underlying platform where the Java
    language is usually run on top of. It provides a single platform in which
    is abstracted of the underlying hardware architecture at the cost of paying
    some performance overhead.
