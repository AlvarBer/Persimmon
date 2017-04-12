Introduction
============

On this chapter Persimmon is introduced, along its main objectives and
motivations.
There is also a section about things that are close but outside the scope of
the project, and an overview of the project structure.


Description
-----------
Data Science has seen exponential growth in the market on recent years, with
some predictions stating that one million data scientist will be needed by
2018 [@onemillion].
Bubble or not data scientists find themselves on a golden age, for the Harvard
Business Review it is the sexiest job of the 21st century [@sexy].
Despite all the hype, there is a shortage of skilled data scientists, the field
is inherently multidisciplinary, as coding, statistics and domain knowledge are
required, making the path to mastery long and complex, leading to the so
called Unicorn hunts [@unicorn, @hunt].

Tools such as scikit-learn[^skl], Weka or Tableau provide a very high
level access to some of the required tools data scientist require, easing the
learning curve and widening the pool of available data scientists.
However this tools either require coding, focus on just preprocessing tasks
(cleaning of the data) or provide a very limited interface.

Persimmon aims to provide a visual interface for scikit-learn, giving the
ability to create pipelines without a single line of code, thus giving most of
the power of hand coding the pipelines with a helpful visual representation.

In order to accomplish this the project tackles the following topics,

* Dataflow Programming. This paradigm presents programs as a directed acyclic
    graph, pioneered on the 60 at MIT and Bell labs [@bell].
    It models programs as a stream of data that is run through a pipeline of
    instructions rather than a set of instructions that operates on external
    data, i.e. the instructions are flowing through data, not the other way
    around.
    This results in parallel programs by default, closer to the functional
    paradigm than imperative programming and the Von Neumann architecture, as
    mentioned in functional programming seminal paper [@backus1978can].
 <!-- Motherfucking backus had over 3000 citations -->

* Visual Programming. The natural fit for a dataflow representation is a visual
    interface, as we can present the graph visually [@shu1988visual].
    Further improvements include type-checking at write time, i.e. when
    connecting the blocks only allow for connections that are type safe.

* User Experience. The project is driven by the users feedback and engagement
    with the prototype.
    The interface needs to convey and give users hints in order to ease the
    difficulty curve.
<!-- Add citation -->

* Software Engineering. Interfacing with previous existing code, laying
    well-defined interfaces and organizing code though object-oriented
    techniques.
<!-- Add citation -->

* Machine Learning. Although there is no writing implementation of new
    algorithms extensive knowledge of current implementations is needed in
    order to surface all the available options, as sklearn provides many ways
    to modify their configuration through parameters [@scikitlearn].

* Data Wrangling. Some preconditions about the data have to be assumed or
    the user has to be provided with the tools to perform the transformation.

* Compilers. The graphical form of a workflow involving several steps is
    compiled down to Python source code (Transcompilation).

The hypothesis of the project is that the visual representation of the workflow
and the associated concepts can help to both learn and use Machine Learning
techniques and to accelerate early exploratory datascience work.

This hypothesis converges with the spirit of sklearn, [see @scikitlearn, pp29]
that also tries to bring the Machine Learning techniques out of PhD
dissertations and obscure libraries into the mainstream, providing high-level,
easy to use access to those resources.
This strategy seems to have worked for sklearn, becoming to become one of the
most important open source machine learning libraries in the process, with over
16000 stars on [Github](https://github.com/scikit-learn/scikit-learn), and is
being used on companies such as Spotify, Facebook or Evernote.


Motivation
----------
After learning about Machine Learning at university last year I got an
internship on an algorithmic trading company.

My main task was helping moving the existing codebase from `MATLAB` to
`Python`, and during that process some of my co-workers were having
struggles with the language switch.
They all came from backgrounds such as Maths, Physics, Electric Engineering,
Statistics or Aerospace Engineering.

But there were no Computer Scientists even though their role require, apart
from theoretical maths and stats knowledge, a very good level of programming
expertise.

Experts from these fields tend to have weaker programming skills,
as they mostly work with scientific computing oriented languages such as
`MATLAB`, `R` or `Julia`, and moving to a general purpose language such as
`Python` involves learning about a plethora of additional topics, such as
Object Oriented Programming, custom complex Data structures or cache
optimization.

The situation is even more complex for newcomers to Machine Learning, as
they not only have to deal with the programming barrier but also have to
overcome the difficulties of learning the algorithms themselves.


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
     they see fit without writing a single line of code.


What the project is not
-----------------------
The project is not concerned with the following:

* General Data Cleaning/Wrangling. Although there is some data manipulation
    that is necesary and included on sklearn it is outside the scope of the
    project, Persimmon only works with clean data. This is done because it is
    very hard to translate code-based data manipulation into a visual
    representation.
* Data Visualization. Since this kind of work is very hard to represent without
    requiring explict coding on a case by case basis, as it is highly dependant
    on the characteristics of the data to visualize.
* General Purpose Visual Programming. Since focusing on Machine Learning allows
    Persimmon to make assumptions about the possible programs that enable
    features such as type simplication (check type chapter) or removing
    explicit flow management (more on the literature review chapter).

Project Structure
-----------------
<!-- Do this when finished -->

[^skl]: Scikit-learn is a python library that aims to bring machine learning to
    a more general public, by providing a high-level API that allows the ease of
    use and interchange of different estimators.
