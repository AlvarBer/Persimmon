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
:   Using evaluation it can be concluded that it is possible to create a
    machine learning visual interface that is as flexible as a language,
    including a type system and errors in compilation time, and yet remains
    simple to use, even for newcomers.

Design and Usability:
:   The final implementation closely followed the initial sketches, proving the
    initial design had solid fundamentals.
    The good evaluation scores, and final remarks given by participants
    demonstrates that the interface has accomplished its objectives of
    producing a powerful yet simple to use interface.
    Features like the smart bubble that use instrospection to suggest suitable
    blocks to connect leverage the type system to help the user create the
    pipelines faster and easier.

Evaluation:
:   Despite having a low number of participants the evaluation
    resulted in a mostly unanimous good reviews of the software, as well as
    providing very useful feedback for future improvements.

Learning Tool:
:   Because most of the milestones were achieved the final system has
    proved to be useful enough for its use as a learning tool, it was even
    remarked by two participants how easy it was to use, and how easy it was to do
    complex actions (such as hyper-parameter tuning) compared to other
    frameworks/libraries.

Faster Exploratory Work:
:   I personally used the software for performing
    ml analysis, finding it worked pretty well for early exploratory work, when
    limited by the lack of a block it was pretty easy and fast adding a block
    that solved the problem (in around ~20 lines of code).
    During this use I realized another possible improvement, caching operations,
    with this the results of pipelines are not recalculated unless something
    changes upstream, this provides the closest thing to a visual REPL[^REPL].

Implementation:
:   At the end of the project the non-functional requirements have been met,
    delivering a windows single executable file that participants used for the
    evaluation, while keeping a good performance, handling many blocks without
    a hitch, and keeping the frame rate steady while modifying connections and
    running the execution of the pipeline simultaneously.

Retrospective
-------------
With over 7k lines of code 10 releases, and more than 200 commits, Persimmon
stands as a medium size codebase, since its inception it has gathered
attention, with over 3000 visits, and more than 90 stars on [Github].

<!--
![Lines of code](images/loc.png)
-->

It has been featured on [multiple], [websites], and even won [best project] at
the compshow 2017 at the University of Hertfordshire.

![Chinese machine learning forum](images/china.png)

Conclusion
----------
In conclusion Persimmon has achieved all proposed objectives, proving
there is room for improvement on the field of visual languages for machine
learning, and that small improvements make a significant impact on the user
experience.
In fact a system should not only make it hard or impossible to construct
incorrect graphs, but should make it easier and faster to create correct graph.

Giving more power to the user does not mean making the interface more
complicated, in fact it can be the opposite.


Bibliography
============

[Github]: htttps://github.com/AlvarBer/Persimmon
[multiple]: http://mailchi.mp/pythonweekly/python-weekly-issue-295
[websites]: http://forum.ai100.com.cn/blog/thread/ml-2017-05-10/
[best project]: https://twitter.com/HertfordshireCS/status/857266574356598785

[^REPL]: A Read Eval Print Loop is an interactive console many modern
    programming languages that allows for the interactive execution of
    expressions, saving the results in a local session.

