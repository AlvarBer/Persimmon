Postmortem
==========

After the evaluation it is time to make a retrospective, and look what has
been achieved and what not.

On the introduction several objectives were mentioned, let's revisit those.

* Research. There was a literature review on all the fields covered by the
system. It was particularly interesting learning about the dataflow paradigm,
because it is a niche I was not familiar with.
It was also great looking at the available commercial solutions, they prove
that there is a lot of enterprise interests on this kind of systems.

* Requirements. The bi-weekly iterations worked reasonably well, there was not
anything that got stuck or delayed more than one additional iteration.
It also proved useful for having a usable system from even the first iteration.

* Design. The final implementation followed the initial sketches pretty
closely, proving the initial design had solid fundamentals, the good evaluation
score, and the remarks given by the users demonstrates that while there are
plenty of improvements that can be done it remains a good interface to use.

* Implementation. At the end of the project the non-functional requirements
have been met, delivering a windows single executable file that participants
used for the evaluation, while keeping a good performance, handling many
blocks without a hitch, and keeping the frame rate steady while modifying
connections and running the execution of the pipeline simultaneously.

* Testing. Probably the weakest part of the project because all the backend
is based around visual elements unit testing proved pretty useless, and this
part comprised the biggest part of the code.

* Evaluation. Despite having a low number of participants the evaluation
resulted in a mostly unanimous good reviews of the software, as well as
providing very useful feedback for future improvements.

* Learning. Because most of the milestones were achieved the final system has
proved to be useful enough for its use as a learning tool, it was even
remarked by two participants how easy it was to use, and how easy it was to do
complex actions (such as hyper-parameter tuning) compared to other
frameworks/libraries.

* Faster exploratory work. I personally used the software for performing
ml analysis, finding it worked pretty well for early exploratory work, when
limited by the lack of a block it was pretty easy and fast adding a block
that solved the problem (in around ~20 lines of code).
During this use I realized another possible improvement, caching operations,
with this the results of pipelines are not recalculated unless something
changes upstream, this provides the closest thing to a visual REPL[^REPL].

All the mayor milestones were reached but the compilation feature, this is
because deciding the order in which blocks get translated means settling
the current evaluation strategy, while leaving undecided means that some
interesting such as optimistic evaluation can be implemented on the feature,
for more on this check the type chapters, two languages section.

In conclusion Persimmon has achieved most of the settled objectives, proving
there is room for improvement on the field of visual languages for machine
learning, and that small improvements make a significant impact on the user
experience.
Giving more power to the user should not mean making the interface more
complicated.


Bibliography
============

[^REPL]: A Read Eval Print Loop is an interactive console many modern
    programming languages that allows for the interactive execution of
    expressions, saving the results in a local session.
