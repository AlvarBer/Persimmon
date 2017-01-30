Introduction
============


Description
-----------
Persimmon is a visual programming interface for sklearn.

This projects involves a variety of Computer Science topics, such as User
Experience (Main topic as the project is driven by the users feedback and
engagement with the project), Machine Learning (We don't write the algorithms,
but need extensive knowledge of them to surface all their options) Software
Engineering (We have to interact with already built software, using interfaces
and organizing code through object-oriented techniques), Compilers (Language
parsing and transpilers) and a number of tangentially related topics such as
Machine Learning, I/O, preprocessing of data, etc.


Motivation
----------
After learning about Machine Learning on university last year I was able to get
an internship working for a company on the algorithmic trading sector..

There, amongst other duties, I aided with moving the codebase from MATLAB to
Python, and during that process I realised many of my co-workers struggled with
the switch. All of the were not computer scientists, but instead came from a
variety of backgrounds such as Maths, Physics, Electric Engineering,
Statistics or Aerospacial Engineering.

Yet they were the whole of the department, their work requires a very high
level of theoretical maths knowledge, and so happens that these experts from
these fields tend to not have a lot of general programming skills, they mostly
work with specialized languages, tailored to these tasks such as MATLAB, R,
Julia, etc, and moving to a general purpose language such as Python involves
learning about a plethora of additional topics, such as Object Oriented
Programming, custom complex Datastructures or CPU cache optimization.

The situation is even more complicated for newcomers to Machine Learning, as
they not only have the programming barrier but also have to overcome the
difficulties of the algorithms themselves, something Computer Scientists also
struggle with (In many cases even more because their weaker maths skills).

So this project serves a double purpose, it helps with the programming barrier,
and it aids with the Machine Learning process as it allows the learner to focus
on the connections, intuitions and mathematical basis and not on the
implementation details and the quirks of the concrete language.

This hypothesis that visual learning can improve understanding is supported by
numerous sources such as [@fry2007visualizing] and [@principles].


Open Source DNA
---------------
Here is where we thought about contacting the *"e-learning UCM"* research group
at Complutense University because we saw an opportunity to bring the power of
the datascience to the educational world, in this case via the educative games.

We thought this would be a good stress test for the software, and giving
investigators that may not be datascience experts the ability to measure if
serious games were archieving their purposes, meaning if they are really
helping to teach their users what they are supposed to.

It was an obvious decision to make it Open Source, many of the tools we use are
Open source, and it was the ability to enange with them the reason that we
have become Computer Scientist.

This helps many educational games do not have a big budget and in this
way our program would be accessible to all of them and they can even tweak some
parts of the software if they really need to.

Here is where we started thinking about which technology to use and Python was
the obvious choice in order to keep all the project on the same language.

So after looking for several Python UI libraries `kivy` seemed the most
appropiate UI framework.

