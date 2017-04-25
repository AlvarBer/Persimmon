Evaluation
==========

From the conception of the project it was intended to be tested by
participants, evaluating the usability of the prototype.
This chapter explains that evaluation process, how the survey was designed, and
the analysis of the results.

The evaluation corresponding to this system has been subjected to ethics
approval by the **SCIENCE & TECHNOLOGY ECDA** with protocol number
COM/UG/UH/02090, and titled 'An Evaluation of Persimmon' at date 22/02/17,
amended by the **HEALTH SCIENCES ENGINEERING & TECHNOLOGY ECDA** at date
20/04/2017.


Method
------
The method for conducting the evaluation is based on conducting a series
of closed tasks and giving feedback on each of them, as well as some free forms
questions at the end of the form. The complete form can be seen at appendix C.

The questionnaire selected is the Single Ease Question as explained in
@sauro201210.
It based on of asking how difficult a task was on a seven point scale after it
has been performed.
Research shows that it provides equal or greater accuracy than more difficult
measures of task-difficulty @sauro2009comparison.

Along this questions, the participant knowledge and familiarity with Data
Mining and Machine Learning is saved, as well as any additional feedback about
the system.


Proposed Tasks
--------------
The evaluation consists of three different closed tasks.
The task are defined as to gradually introduce more complex concepts, following
the seen workflows on the workflow chapter, being introduced to the
concepts of modifying an existing connection and complex block that require
more interaction from the user.

* First task is the creation of a simple workflow, the objective of
    this task being to introduce Persimmon to the participants in the simplest
    terms. Using the iris dataset they perform a cross validation evaluation
    of their chosen classificator.
* Second task is modifying the previous workflow to create a more complex
    worflow that fits and predicts using an estimator and two sources of files.
    It is only slightly more complex than the previous one, but it introduces
    the concept of re-cabling to the participants.
* Third task and final task. This one involves adding hyper-parameter tunning,
    which in turns means providing a dictionary with desired parameters.

To see the complete form please check Appendix C.

Evaluation Results
------------------
At time of submission the population of the evaluation is n = 3.

All participants showed a good level of familiarity with the subject, defining
themselves as quite familiar in the fields of Machine Learning, Data mining and
Visual Machine Learning/Data Mining tools (76%, 71.4% and 57.14% average score
respectively).

The scores for the tasks were quited good, averaging 85.71%, 90.47% and
85.71%, compared to the average score SEQ questions tends to have (which is
71.42%, or a 5 in a 7 point scale).
This means that the participants found the tasks relatively easy, they also
performed the tasks on schedule (30' or less).

The tasks standard deviation were quite uniform, with $\sigma$ equal to 1, 1.15
and 0 for tasks one, two and three respectively.
This indicates that the population largely agrees, with no visible outliers.

While these are good indicators that the interface of the system succeeded on
its intentions, the most important data from the evaluation is perhaps the free
form questions, where participants unanimously agreed on the need for the
ability to delete blocks.

Another complain is the placements of the blocks, by default they all spawn
at the same point, that can result in blocks stacking on top of each other,

The blocks participants struggled with the most are those including file
dialogs, citing how the path does not reset on cancel, sometimes responding
to single click and sometimes not responding at all, and the need for a way
to show the current selected file without clicking on the file dialog.

Some other complains/suggestions align with the suggestions on the final
interface proposed, such as adding a zoom ability, a bubble spawning block
system instead of tabs.
Also some new ideas were proposed, such as undo functionality, or visualization
options.

On the other hand participants praised the drag and drop nature of the
interface, the wide selection of ml algorithms and test options, the use of
colors to indicate types, consistent design, easy to navigate and shallow
learning curve.

The error handling and the resilience of the application were mentioned, as
well as the simple installation process without the need for dependencies
installation.
