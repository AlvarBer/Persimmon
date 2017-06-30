Postmortem
==========

After the evaluation it is time to make a retrospective, look what Persimmon
has achieved.


Objectives Review
-----------------
<!--
Research:
:   Background research was conducted on fields covered by the
    system. It was particularly interesting learning about the dataflow paradigm,
    because it is a niche I was not familiar with.
    It was also great looking at the available commercial solutions, they prove
    that there is a lot of enterprise interests on this kind of systems.

Requirements:
:   The bi-weekly iterations worked reasonably well, there was not
    anything that got stuck or delayed more than one additional iteration.
    It also proved useful for having a usable system from even the first iteration.

Testing:
:   Probably the weakest part of the project because all the backend
    is based around visual elements unit testing proved pretty useless, and this
    part comprised the biggest part of the code.
-->

Feasibility:
:   Evaluation seems to show that it is possible to create a machine learning
    visual interface that is both flexible and relatively easy to use, even
    for learners, including a type system and errors in compilation time.

Design and Usability:
:   The final implementation closely followed the initial sketches, proving the
    initial design had solid fundamentals.
    The good evaluation scores, and final remarks given by participants, seem to
    demonstrate that the interface has accomplished its objectives of
    producing a powerful yet simple to use interface.

Evaluation:
:   Despite having a low number of participants the evaluation
    resulted in a mostly unanimous good reviews of the software, as well as
    providing very useful feedback for future improvements.

Learning Tool:
:   Because most of the milestones were achieved the final system has reached a
    state where it is useful enough for its use as a learning tool thanks to
    supporting the simplest (and most common) workflows, it was even
    remarked by two participants how easy it was to use, and how easy it was to do
    complex actions (such as hyper-parameter tuning) compared to other
    frameworks/libraries.

Faster Exploratory Work:
:   Like last objective thanks to the current state of the system it is pretty
    fast to perform early ml analysis, when limited by the lack of a block it
    was pretty easy and fast adding a block that solved the problem (in around
    ~20 lines of code).

Implementation:
:   At the end of the project the non-functional requirements have been met,
    delivering a windows single executable file that participants used for the
    evaluation, while keeping a good performance, handling many blocks without
    a hitch, and keeping the frame rate steady while modifying connections and
    running the execution of the pipeline simultaneously.

Retrospective
-------------
With over 7k lines of code, 10 [releases], and more than 200 commits, Persimmon
stands as a medium size codebase, since its inception it has gathered
attention, with over 3000 visits, and more than 90 stars on [Github].

<!--
![Lines of code](images/loc.png)
-->

It has been featured on [multiple], [websites], and even won [best project] at
the 2017 compshow at University of Hertfordshire.

![Chinese machine learning forum](images/china.png)


Conclusion
----------
In conclusion the system has managed to reach a testable state in which
participants have remarked its usability, flexibility and potential.
This seems to indicate that is is possible for small improvements on visual
machine learning tools do make an impact on the user experience
Features like the smart bubble that use introspection to suggest suitable
blocks to connect leverage the type system to help the user create the
pipelines faster and easier.

This corresponds with the hypothesis of the project, as well as the objective
that the system should not only make it hard or impossible to construct
incorrect graphs, but should make it easier and faster to create correct graphs.

Giving more power to the user does not mean convoluting the interface,
in fact it can be the opposite.


Future Work
-----------
* Surface of optional parameters.
* Visual Polish.
    - Smart Bubble breakdown by category.
    - More indicators when dragging/dropping.
* Graph Serialization.
* Support move and zoom in background.
* Automatic block generation from Python function.
* Undo functionality (Command pattern).
* Area drag select.
* Skeletons of common workflows.
* Unit/Integration/End to end testing.
* Automatic windows deployment.
* Continuous integration.
* Cache results similar to a REPL[^REPL].

Bibliography
============

[Github]: htttps://github.com/AlvarBer/Persimmon
[releases]: htttps://github.com/AlvarBer/Persimmon/releases
[multiple]: http://mailchi.mp/pythonweekly/python-weekly-issue-295
[websites]: http://forum.ai100.com.cn/blog/thread/ml-2017-05-10/
[best project]: https://twitter.com/HertfordshireCS/status/857266574356598785

[^REPL]: A Read Eval Print Loop is an interactive console many modern
    programming languages that allows for the interactive execution of
    expressions, saving the results in a local session.

