Evaluation
==========

On this chapter the evaluation process and how the survey was designed is
explained.

Method
------
Based on in place recollection, mainly based on a questionnaire, plus some
additional information that is harvested by the system (mainly timings).

The questionnaire selected is the System Usability Scale.


Proposed tasks
--------------
The evaluation is composed by three different closed tasks.

* First task is the creation of a simple workflow, the objective of
    this task being to introduce Persimmon to the participants in the simplest
    terms.
    - First the participants have to load the iris file, using the csv input
        block and navigating the filesystem to get the file `iris.csv`.
    - Then they have to spawn the SVM block and connect the previous input
        block to this block, they do not need to change any of the parameters
        of the block.
    - After the SMV block has been placed a cross validation block has to be
        spawned and connected to the result of the SVM block.
    - Finally the result of the cross validation has to be connected to a
        print output block.
* Second task is modifying the previous workflow to create a more complex
    worflow. It is only slightly more complex than the previous one, but it
    introduces the concept of re-cabling to the participants.
    - Add a prediction block.
    - Save to file.
* Third task and final task. This one involves adding hyper-parameter tunning,
    which in turns means providing a dictionary with desired parameters.
<!--
    - Create an entirely new workflow, either by putting it on the same
        blackboard or on a new one.
-->
    - Use `gridsearch` for hyper-parameter tunning.
    - Use print output block again to return best hyper-parameters.

<!-- Actual evaluation -->
