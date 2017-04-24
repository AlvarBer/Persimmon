Type Checking
=============

Although Python has no robust type checking step it is possible for our visual
language to have hard guarantees of correctness at write time, meaning that
the building of incorrect pipelines can be avoiding altogether.

Gradual Typing
--------------
Python allows for gradual typing since 2014 [@pep484], meaning that function
parameters can be specified and tools such as `mypy` will check for possible
type errors, if some parameter or function type is not specified the tool
will simply ignore the associated checks.

These tools provide a useful tool to introduce type checking in current and
new python code, however they run outside the python execution (i.e. they run
on the non-existent python compile time) and Persimmon needs run time type
checking for dynamic block connections.

Nevertheless, this is a useful tool for improving the code quality, specially
for the backend code, because it is much pure that the frontend.
It is also a reference for Persimmon type system.


Write Time
----------
On the previous section runtime type checking was mentioned, this is because
on the Python side the type checks have to be done at runtime due to blocks
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
* Dynamic or Static. Static types refer to the notion of the language using
    the type information to check for type safety on compilation time/before
    runtime. The only close thing Python has to this is type hinting, but
    it is still a relative young addition to the language, most of the
    existing codebases have not been annotated yet, and the community debates
    whether it is necessary or not.
    Persimmon on the other hand checks the type safety of the relations on
    write time, meaning before execution.
    Dynamic types is the oposite concept, where type information is used at
    run time, this can be useful for concepts such as dynamic dispatch.
* Strong or Weak. This refer to the notion of the language coercing the types
    or certain expressions without the explicit command of the programmer.
    On some languages this is done only where the type conversion is always
    safe (most common example is converting an integer to a float) and it is
    known as *upcasting*.
    A very strong language does not perform implicit type coercions
    [madsen1990strong].
* Evaluation strategy. Most imperative languages have eager evaluation,
    meaning that expressions and statements are evaluated as soon as
    encountered.
    It is also possible to have a non-strict evaluation, meaning that
    expressions are evaluated at a latter time.
    When exactly depends on the exact strategy, optimistic evaluation for
    example tries to run statements early only if they are fast, if they
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
For example, most algorithms accept Numpy arrays, panda dataframes, Scipy sparse
matrices and almost any array type that implements `__get__` in a manner Numpy
understands, but there is no actual interface that can be used to know which
objects will run without crashing unless the code is executed.

![Type hierarchy](images/type_hierarchy.pdf)

Because of this, types had to be invented, sometimes they correspond to
underlying duck typing based interfaces, but sometimes they do not have a
direct equivalent on Python.
Types on Persimmon follow a simple tree structure, checking whether a
connection is safe on the notion of the types having a is-consistent-with
relation, this is based on @pep483.
A is-consistent-with notion extends the more typically used is-subtype-of
relation used in type theory, with $Any$ representing the notion of a type that
is-consistent-with every type (meaning that it is not a subtype of other types
but all types are consistent with any and vice versa).
Adding to this blocks of the respective edges of a connection must be
different, one of the pins must be an `InputPin` and the other an `OutputPin`,
and the `InputPin` must have no connection already.

These are all the rules used for checking if a connection is safe, it is a
primitive type system, with further improvements ranging from the ability to
define arbitrary subtypes to type classes.


Intermediate Representation
---------------------------
The visual blocks represent a visual-dataflow language, however the backend
uses a simpler representation of the relations between the blocks, this in turn
helps decoupling backend and frontend.

The frontend blocks are translated on function `to_ir`, which aparts from
translating the blocks it avoids considering orphaned blocks to achieve the
desired intermediate representation. Runs on $\mathcal{O}(n)$ with n being the
number of pins.

Let's represent the types on a more strongly typed language than Python.

~~~haskell
type Id = Int -- The hash is an integer
data Inputs = Inputs {origin :: Id, block :: Id}
data Blocks = Blocks {inputs :: [Id], function :: IO a -> IO a,
                      outputs :: [Id]}
data Outputs = Outputs {destinations :: [Id], block :: Id}
data IR = IR {inputs :: Map Id Inputs, blocks :: Map Id Blocks,
              outputs :: Map Id Outputs}
~~~
\begin{figure}
\caption{IR definition on Haskell}
\end{figure}

As we seen on figure 8.2 the intermediation representation is just three
Maps[^Map], one for blocks, one for input pins and one for output pins.
But the maps do not contain pins themselves, merely unique hashes (Int on
this case).
This reflects the fact that pins model only relationships, not state.
The only non-hash value on `IR` are the blocks functions.
These functions are indeed impure[^impure], but earlier on the literature
review it was established that dataflow programming was mainly side-effect
free, so why do they involve side effects[^side-effects]?.

There are two reasons, first on the actual python programs this
types do not exist, at least not on an enforceable way, so when translating
them to Haskell the `function` field represents the "worst case", that is to
say only a few functions will actually end up producing side-effects.
The second and more important reason is that blocks actually execute
themselves, meaning the block function does not has parameters, it relays on
getting the values from the pins values and sets the values of the output
values, leaving us with the work of setting those input pins and retrieving
results from the output pins.

This goes against the previously stated "pins represent relationships, not
state", in fact an alternative implementation was created in which the
function returned a tuple of results, and it is the compiler job to now
associate the output pins to each of the elements on the tuple.
This was done using the same current mechanism, saving into a dictionary, the
difference being that while currently the values appear on the output pins and
have to be moved into the dictionary (or otherwise a reference to the pin
itself must be kept on the dictionary) on this case the values were fed
directly to the algorithm.
However, this proved limiting, as code became more complex since more checks
have to be done, there was no obvious advantage and side-effects did not
disappeared but merely were harder to do.

With this kind of language it is possible to create arbitrary functions as a
composition of functions, all the inputs are either omitted if they are
connected through the blocks, else they are promoted to the output of the new
function.
This works as long as side effects blocks do not depend on each other, this
only happens when having both *"entry"* and *"exit"* blocks.


[^impure]: The term purity here refers to the absence of side effects on a
    function, so a impure function is a function that performs side effects,
[^side-effects]: Value manipulations other than the arguments passed and the
    returned value.
