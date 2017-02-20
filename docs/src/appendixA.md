Appendix A: Package Organization
================================

Persimmon source code is written on the form of a typical python package,
on the following section the specifics of how the different subpackages
are distributed and what is on each of them.

![Persimmon package hierarchy](images/packages.pdf)

Backend
-------
The backend performs all the calls to sklearn, as it receives the graph
of execution and performs the desired calls to the estimators.

The backend does not know anything about the view, and as such the current
kivy frontend could be replaced by any other visual framework.


View
----
The view contains all of the kivy code, both python source files and kivy
lang files.
