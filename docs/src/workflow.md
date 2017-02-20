Workflows
=========

What is a workflow on this context? When we talk about workflow we refer to
the typical ML exploratory work analysis, i.e. the possible pipelines we use
early on the project when we still do not know what strategies will work best
for the data.

Simple
------
The simplest workflows are those that involve no preprocessing, no adjustment,
and just either test how good the model works (validate) or predict using both
the train file and another file without class feature.

![Just validation of the model](images/simplest_workflow.pdf)

![Prediction using the whole dataset](images/simpler_workflow.pdf)

Regular
-------
A more usual workflow involves also tunning the hyper-parameters of the
selected hyper-parameters, this involves making a grid of the possible
hyper-parameters and trying all of them, resulting in finding the best
possible value.

![Adjustment of hyper parameters](images/regular_workflow.pdf)

Complex
-------
More complex workflows involve preprocessing, this varies wildly on a case by
case basis, and can involve data cleaning, feature engineering (such as
combining two features into one) or dimensionality reduction.

A extreme example can be seen in [@automatic], of course this kind of workflow
is out of scope for us, as this is far away from exploratory work.

![Fully automatic Machine Learning framework](images/fully_automatic_workflow.png)

In fact this kind of use case would result unwieldy and messy on a visual form,
visual programming gets too bloated when we try to represent programs that are
too complex. That is one of the main reasons visual programming languages never
truly fulfilled their promises and gained mainstream adoption [@unbelievable],
while they managed to be relevant in very small niches such as PLCs[^plc]
[@plc].


[^plc]: Programable Logic Controllers are industrial digital computers used for
    controlling a manufacturing process.
