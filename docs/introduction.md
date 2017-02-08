Introduction
============


Description
-----------
Persimmon is a visual programming interface for scikit-learn[^skl].

This projects involves a variety of Computer Science topics,

* User Experience. Main topic as the project is driven by the users feedback
	and engagement with the project.

* Software Engineering. Interfacing with previous existing code, laying
	well-defined interfaces and organizing code though object-oriented
	techniques.

* Machine Learning. Although there is no writing implementation of new
	algorithms extensive knowledge of current implementations is needed in
	order to surface all the available options.

* Data Wrangling. Some preconditions about the data have to be assumed or
	the user has to be provided with the tools to perform the transformation.

* Compilation. The graphical form of a workflow involving several steps is
	compiled down to Python source code (Transpilation).

The hypothesis is that the visual representation of the workflow and the
associated concepts can help to both learn and use Machine Learning techniques
and the faster iteration of exploratory datascience work.


Motivation
----------
After learning about Machine Learning on university last year I got an
internship on an algorithmic trading company.

There, amongst other duties, I aided with moving the codebase from `MATLAB` to
`Python`, and during that process I realised some of my co-workers were having
some struggles switching. The whole of the department were not computer scientists, but
instead came from a variety of backgrounds such as Maths, Physics, Electric
Engineering, Statistics or Aerospace Engineering.

Yet they were the whole of the department, their work requires a very high
level of theoretical maths knowledge, and so happens that these experts from
these fields tend to not have a lot of general programming skills, they mostly
work with specialized languages, tailored to these tasks such as MATLAB, R,
Julia, etc, and moving to a general purpose language such as Python involves
learning about a plethora of additional topics, such as Object Oriented
Programming, custom complex Data structures or CPU cache optimization.

The situation is even more complicated for newcomers to Machine Learning, as
they not only have the programming barrier but also have to overcome the
difficulties of the algorithms themselves, something Computer Scientists also
struggle with (In many cases even more because their weaker maths skills).

So this project serves a double purpose, it helps with the programming barrier,
and it aids with the Machine Learning process as it allows the learner to focus
on the connections, intuitions and mathematical basis and not on the
implementation details and the quirks of the concrete language.

Our hypothesis is supported by numerous sources such as [@fry2007visualizing]
and [@principles].


[^skl]: [Scikit-learn](http://scikit-learn.org/) is one of the most widely used
	machine learning frameworks, with more than 16 thousand starts on Github
	and endorsed by companies such as Spotify, EverNote or Booking.com.
