Literature Review
=================

On this chapter the main sources used for the project are explained and some of
the learning needed in order to build the project.

On Machine Learning
-------------------
Although the project aims to provide a very high-level tool for machine
learning without needing to get too deep into the algorithms, it is necessary to
understand the library that is used for performing the actual ML.

While from the conception of the project `python` was set as the main language
a comparison between ml libraries was done in order to evaluate scikit-learn
against the competitors.
A good comparison is seen at [@mlcomparison], but it mostly shows deep learning
frameworks, which are not exactly what sklearn is.
In fact while deep learning is going through a boom right now (no doubt helped
by the marketing team at Google) it is a bleeding edge field [@dlmature].
Neural networks with many layers and complex connections between them are also
very difficult to visually represent compared to traditional statistical
methods that can be represented as functions more easily, and whole frameworks
are dedicated just to represent them (Tensorflow [@abadi2016tensorflow]).

On the other hand traditional machine learning libraries are either embedded on
purpose-specific languages (such as `R`, `Matlab`, `Julia`) or have less users
than others ([Torch](https://github.com/torch/torch7) has only 7k Github
starts).

And finally cluster-oriented computing frameworks like Spark or Hadoop are
usually in compiled languages like `Java` or `C++` for performance reasons.

The main paper of sklearn is [@scikitlearn], scikit-learn is based on Numpy (a
n-dimensions array for `Python` [@numpy]) and scipy (a scientific computing
framework [@scipy]).
Persimmon also uses pandas [@pandas] for input and output handling.

Others papers related to the pitfalls of machine learning that proved useful
when analyzing workflows were [@hughes1968mean], [@pitfalls].


On Dataflow Programming
-----------------------
After reviewing dataflow seminal paper [@bell], and [@sousa2012dataflow] it was
clear then fundamental step to have a working system was to write a compilation
algorithm from the visual representation to `python code`.

There are different ways to implement dataflow programming compilers, for now
let's just consider the language representation as formed by blocks that have
pins.
Pins on the left side of a block are called input pins and each must come from
a single output pin.
Pins on the right side are called output pins and one can be connected to
multiple input pins.

This results in what is effectively a directed acyclic graph, in order to
compile and run the program (actually it is theoretically possible to have
multiple parallel programs on the same blackboard) the graph has to be
explored, checking the dependencies of each block, executing them if necessary,
executing the function and adding the next blocks to be executed until there is
no block left to be executed.

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
closely they are $\mathcal{O}(n*m)$ where n is the number of blocks and m the
number of pins.


On Visual Programming
---------------------
For designing the interface many notes were taken from [@shu1988visual], but
most importantly from the blueprint system [@shah2014mastering] and Azure ML
studio web interface [@barga2015predictive], all these influences are discussed
on the state of the art section, and the interface design itself along with
the sketches can be seen on the Interface Design chapter.


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

Weka [@weka] is a popular machine learning suite, written in `Java` and
developed at the University of Waikato.
It provides both a command line interface and a graphical interface.

However it starts to show its age, the interface feels dated and the
composition of algorithms on a graphical is very restricted.
Because it is written on Java it also means that it need the JVM[^JVM], which
is a bit of a con, specially in production servers where dependencies bring a
long and arduous process of review and approval [@zmud1980management].

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
With this knowledge it is clear that in order to not have an explicit flow line
the visual language represented must be pure, constraining side effects to
either the start or the end of a pipeline [@mcbride2008applicative].

![Unreal Engine 4 Blueprint system](images/unreal.png)

Blueprints provides an intuitive interface, when one cable is dragged from a
block and a prompt appears with only the blocks that make sense to be connected
to the previous block.
Another example is how different types are represented by different colors in
both pins and cables, making it easier to predict whether a connection makes
sense or not without even trying to create it.

These small details improve the user experience, making it faster and easier
to use.


[^JVM]: The Java Virtual Machine is the underlying platform where the Java
    language is usually run on top of. It provides a single platform in which
    is abstracted of the underlying hardware architecture at the cost of paying
    some performance overhead.
