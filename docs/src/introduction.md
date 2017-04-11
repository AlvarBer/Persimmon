Introduction
============

On this chapter Persimmon is introduced, along its main objectives and
motivations.
It is also outlined what is outside the scope of the project.


Description
-----------
Data Science has seen exponential growth in the market on recent years, with
some predictions stating that One Million Data Scientist will be needed by
2018 [@onemillion]. Bubble or not Data Scientists find themselves on a golden
age, for the Harvard Business Review it is the sexiest job of the 21st century
[@sexy].
Despite all the boom, there is a shortage of skilled Data Scientists, the field
is inherently multidisciplinary, as coding, statistics and domain knowledge are
required, making the path to Data Science long and complex, leading to the so
called Unicorn hunts [@unicorn, @hunt].

Tools such as Scikit-learn[^skl], Weka or Tableau provide a very high
level access to some of the required tools data scientist require, easing the
learning curve and widening the pool of available data scientists.
However this tools either focus on preprocessing tasks (cleaning of the data)
or provide a very limited interface.

Persimmon aims to provide a visual interface for scikit-learn, giving the
ability to create pipelines without a single line of code.
Thus giving most of the power of hand coding the pipelines with a helpful
visual representation.

In order to accomplish this the project tackles the following topics,

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
    with the project. The interface needs to convey and give users hints in
    order to ease the difficulty curve.

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

The hypothesis of the project is that the visual representation of the workflow
and the associated concepts can help to both learn and use Machine Learning
techniques and the accelerate exploratory datascience work.

This hypothesis converges with the spirit of sklearn, [see @scikitlearn, pp29]
that also tries to bring the Machine Learning techniques out of phd
disertations and obscure libraries into the mainstream, providing high-level,
easy to use access to those resources.
This strategy worked, as sklearn has managed to become one of the most important
open source machine learning libraries, with over 16000 stars on Github, and
is being used on companies such as Spotify, Facebook or Evernote.


Motivation
----------
After learning about Machine Learning on university last year I got an
internship on an algorithmic trading company.

My main task was helping moving the existing codebase from `MATLAB` to
`Python`, and during that process some of my co-workers were having
struggles with the language switch. They all came from backgrounds such as
Maths, Physics, Electric Engineering, Statistics or Aerospace Engineering.

But there were no Computer Scientists even though their work requires, apart
from theoretical maths knowledge, a very good level of programming expertise.

Expert from these fields tend to not have a lot of general programming skills,
as they mostly work with scientific computing oriented languages such as
`MATLAB`, `R` or `Julia`, and moving to a general purpose language such as
`Python` involves learning about a plethora of additional topics, such as Object
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


What the project is not
-----------------------
The project is not concerned with the following:

* Data Visualization. Since this kind of work is very hard to represent without
    requiring explict coding on a case by case basis, and is outside the scope
    of the project.
* General Purpose Visual Programming. Since focusing on Machine Learning allows
    Persimmon to make assumptions about the possible programs that enable
    features such as type simplication or removing explicit flow management.
    This is further discussed on the workflows chapter.

Project Structure
-----------------
<!-- Do this when finished -->

[^skl]: Scikit-learn is a python library that aims to bring machine learning to
    a more general public, by providing a high-level API that allows the ease of
    use and interchange of different estimators.
