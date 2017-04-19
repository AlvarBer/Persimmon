Type Checking
=============

Although Python has no robust type checking step it is possible for our visual
language to have hard guarantees of correctness at write time, meaning that
the building of incorrect pipelines can be avoiding altogether.

Gradual Typing
--------------
Python allows for gradual typing since
[PEP 484](https://www.python.org/dev/peps/pep-0484/), meaning that function
parameters can be specified and tools such as mypy will check for possible
type errors, if some parameter or function type is not specified the tool
will simply ignore the associated checks.

These tools provide a useful tool to introduce type checking in current and
new python code, however they run outside the python execution (i.e. they run
on the non-existent python compile time) and Persimmon needs run time type
checking for dynamic block connections.

Nevertheless this is a useful tool for improving the code quality, specially
for the backend code, because it is much pure that the frontend.
It is also an inspiration to look at Persimmon type system.


Write Time
----------
On the previous section runtime type checking was mentioned, this is because
on the python side the type checks have to be done at runtime due to blocks
being spawned and connected dynamically.
But from the visual language perspective the checks are done even before
compile time (on the literature referred as write time).


The two languages
-----------------
As seen on the previous sections and the implementation chapter Python and
Persimmon are essentially two different languages, but just how different are
they?

|                   |      Python      |       Persimmon      |
|:------------------|:----------------:|:--------------------:|
|      Paradigm     |    Imperative    |Functional (Dataflow) |
| Dynamic or Static |      Dynamic     |        Static        |
|   Strong or Weak  |Weak (Duck typing)|        Strong        |
|Evaluation strategy|       Eager      |      Non-strict      |

* Paradigm. Although Python is multi-paradigm (it supports OOP, Module
    programming) and it even has some functional tools (map/filter/functool)
    they are very weak compared to a truly functional language, even Python
    creator Guido van Rossum has hesitations with the current state of
    functional programming in Python [@biancuzzi2009masterminds].
    On the other hand Persimmon is functional, as there is no asignment, nor
    statements, there is only functions.
* Dynamic or Static. Static types refers to the notion of the language using
    the type information to check for type safety on compilation time/before
    runtime. The only close thing Python has to this is type hinting, but
    it is still a relative young addition to the language, most of the
    existings codebases have not been annotated yet, and the community debates
    whether it is necesary or not.
    Persimmon on the other hand checks the type safety of the relations on
    write time, meaning before execution.
    Dynamic types is the oposite concept, where type information is used at
    run time, this can be useful for concepts such as dynamic dispatch.
* Strong or Weak. This refer to the notion of the language coercing the types
    or certain expresions without the explicit command of the programmer.
    On some languages this is done only where the type conversion is always
    safe (most common example is converting an integer to a float) and it is
    known as *upcasting*.
    A very strong language does not perform implicit type coercions
    [madsen1990strong].
* Evaluation strategy. Most imperative languages have eager evaluation,
    meaning that expressions and statements are evaluated as soon as
    encountered.
    It is also possible to have a non-strict evaluation, meaning that
    expressions are evaluated on a latter time.
    When exactly depends on the exact strategy, optimistic evaluation for
    example tries to run statements early only if they are are fast, if they
    fail to complete before a certain time they are pushed to a later time
    [@ennals2003optimistic].
    In fact the extreme version of non-strictness is lazy evaluation, that
    evaluates only at the last possible time (and only if needed)
    [@launchbury1993natural].

Actual Types
------------
As explained before the type checks must be done before the execution of the
pipeline.
However the actual types of the python code underlying functions and parameters
do not support this, as duck typing makes interfaces not defined on explicit
manners but on the methods used by the underlying code.
For example most algorithms accept Numpy arrays, panda dataframes, Scipy sparse
matrices and almost any array type that implements `__get__` in a manner Numpy
understands, but there is no actual interface that can be used to know which
objects will run without crashing unless the code is executed.

<!-- Explain the type safety as it is implemented -->
