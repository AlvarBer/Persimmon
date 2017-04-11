Type Checking
=============

Although Python has no robust type checking step it is possible for our visual
language to have hard guarantees of correctness at write time, meaning that
we can avoid the building of incorrect pipelines altogether.

Gradual Typing
--------------
Python allows for gradual typing since
[PEP 484](https://www.python.org/dev/peps/pep-0484/), meaning that function
parameters can be specified and tools such as mypy will check for possible
type errors, if some parameter or function type is not specified the tool
will simply ignore the associated checks.

These tools provide a useful tool to introduce type checking in current and
new python code, however they run outside the python execution (i.e. they run
on the non-existent python compile time) and we need run time type checking
for dynamic block connections.

Nevertheless this is a useful tool for improving the code quality.


Write Time
----------
On the previous section runtime type checking was mentioned, this is because
on the python side the run time checks have to be done at runtime, the blocks
are spawned and connected dynamically. But from the visual language perspective
the checks are done even before compile time (on the literature referred as
write time).
However the actual types of the python underlying functions and parameters do
not support this, as they mostly do not reflect compatibility.
For example most algorithms accept numpy arrays, panda dataframes, scipy sparse
matrices and almost any array type that implements `__get__` in a manner
numpy understands.

