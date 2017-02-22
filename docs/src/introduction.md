Introduction
============


Description
-----------
Scikit-learn[^skl] is a python library that aims to bring machine learning to
a more general public, by providing a high-level API that allows the ease of use
and interchange of different estimators.
<!-- Cite scikit-learn paper -->

This projects involves a variety of Computer Science topics,

* Dataflow Programming. This paradigm presents programs as a directed graph,
    pioneered on the 60 at MIT and Bell labs [@bell]. It presents programs
    as a stream of data that is run through a pipeline of instructions
    rather than a set of instructions that operates on external data, i.e.
    instructions flowing through data. This results in parallel programs by
    nature, closer to the functional paradigm than imperative programming and
    the Von Neumann architecture.

* Visual Programming. The natural fit for a dataflow representation is a visual
    interface, as we can present the graph visually. Further improvements
    include type-checking at write time, i.e. when connecting the blocks only
    allow for connections that are type safe.

* User Experience. The project is driven by the users feedback and engagement
    with the project.

* Software Engineering. Interfacing with previous existing code, laying
    well-defined interfaces and organizing code though object-oriented
    techniques.

* Machine Learning. Although there is no writing implementation of new
    algorithms extensive knowledge of current implementations is needed in
    order to surface all the available options.

* Data Wrangling. Some preconditions about the data have to be assumed or
    the user has to be provided with the tools to perform the transformation.

* Compilers. The graphical form of a workflow involving several steps is
    compiled down to Python source code (Transcompilation).

The hypothesis is that the visual representation of the workflow and the
associated concepts can help to both learn and use Machine Learning techniques
and the faster iteration of exploratory datascience work.


Motivation
----------
After learning about Machine Learning on university last year I got an
internship on an algorithmic trading company.

My main task was helping moving the existing codebase from `MATLAB` to
`Python`, and during that process some of my co-workers were having
some struggles with the language switch. They came from backgrounds such as
Maths, Physics, Electric Engineering, Statistics or Aerospace Engineering.

But there were no Computer Scientists even though their work requires, apart
from theoretical maths knowledge, a very good level of programming expertise.

Expert from these fields tend to not have a lot of general programming skills,
as they mostly work with scientific computing oriented languages such as
`MATLAB`, `R` or `Julia`, and moving to a general purpose language such as
Python involves learning about a plethora of additional topics, such as Object
Oriented Programming, custom complex Data structures or cache optimization.

The situation is even more complicated for newcomers to Machine Learning, as
they not only have the programming barrier but also have to overcome the
difficulties of the algorithms themselves.


Objectives
----------
Learning:

:   It helps both with the programming barrier, easing the learning curve of
    Machine Learning as it allows the learner to focus on the connections,
    intuitions and mathematical basis and not on the implementation details
    and the quirks of the concrete language.

Faster exploratory work:

:    By providing an easy to use, drag and drop interface the user can try a
     plethora of different estimators and adjusting the hyper-parameters as
     they see fit.

<!-- Justify these sources. -->
The hypothesis is supported by numerous sources such as [@fry2007visualizing]
and [@principles].


What the project is not
-----------------------
The project is not concerned with the following:

* Data Visualization
* General Purpose Visual Programming

[^skl]: [Scikit-learn](http://scikit-learn.org/) is one of the most widely used
        machine learning frameworks, with more than 16 thousand starts on Github
        and endorsed by companies such as Spotify, EverNote or Booking.com.
