Literature Review
=================

<!-- Actual literature review, on visual progrraming, dataflow and machine
learning -->

State of the art
----------------

Before implementing the system it is necessary to take a look at the previous
works on the field of visual programming and visual Machine Learning tools for
inspiration and avoiding common pitfalls.


<!-- Microsoft Azure Machine Learning Studio -->
![Azure ML Studio web interface](images/azureML.jpg)

Microsoft Azure ML Studio is one of the most direct inspirations for this
project, there is plenty to like, lots of different preprocessing steps,
multitude of estimators, runs on the cloud, and a web interface.

But some of these features are also shortcomings, the web interface feels a
bit clunky, lack of native support means that dragging and dropping do not feel
as smooth as they should. Cloud support is very good, but for sensitive data
such as financial or medical data a self hosted version is a must.

The variety of algorithms is interesting, but the limited ability to extend
them is a pity, we know that azure is written on R, but because is closed
source we can't extend the code in any meaningful way.


![Weka Graphical User Interface](images/weka.jpeg)

Weka is a popular machine learning suite, written in `Java` and developed at
the University of Waikato. It provides both a command line interface and a
graphical interface.

However it starts to show its age, the interface feels dated and the
composition of algorithms on a graphical is very restricted. Because it is
written on Java it also means that it need the JVM, which is a bit of a
con, specially in productions servers where dependencies bring a long and
arduous process of review and approval.


![Unreal Engine 4 Blueprint system](images/unreal.png)

Epic's Unreal Engine 4 introduced Blueprints as an alternative way to `C++`
programming. It represents all the programming structures as blocks that
can be connected, for example an *"and"* is a block that takes to inputs and
returns one output.

The flow of the interface is very good, when one cable is dragged from a block
a prompt appears with only the blocks that make sense to be connected to the
previous block. Or different types are represented by different colors in both
pins and cables.

These small details improve the user experience, making it faster and easier
to use.

<!-- Add more -->
