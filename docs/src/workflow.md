Workflows
=========

A workflow in the context of this project refers to the typical ML exploratory
work analysis, i.e. the pipelines that are used early on the project when it is
still not known what strategies will work best for the given data.

This concept is generalization of sklearn [pipelines](http://scikit-learn.org/stable/modules/pipeline.html).

Simple
------
The simplest workflows are those that involve no pre-processing, no adjustment,
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
More complex workflows involve pre-processing, or automating multiple
classifiers hyper-parameter tuning at the same time through the use of
pipelines, this varies widely on a case by case basis, and can often involve
data cleaning, feature engineering (such as combining two features into one) or
dimensionality reduction (like PCA).

However, there are even further examples of pipelines where the whole process is
automated to the maximum, even going as far as identifying the suitable data
features, selecting classifiers for bagging, boosting and other
meta-classifiers, etc... [@automatic].

It should be noted that this kind of workflow is outside the scope of the
project, as this is far away from exploratory work, and either requires manual
data cleaning anyway or an extremely complex pipeline.

In fact, this kind of use case would result unwieldy and messy on a visual form,
visual programming gets too bloated when representing programs that are too
complex.
On @2003DalkeVisualProgramming some workarounds are proposed,
such as modules, different shapes for different kinds of blocks, etc...
But even with these techniques visual programming languages never truly
fulfilled their promises and gained mainstream adoption [@unbelievable].

However, visual languages managed to become relevant in small niches such as
PLCs design [@plc] or music composition [@musicprogramming].
Presumably because the complexity can be predicted and accounted for when the
number of actions is limited, this is the basis for the project programming
interface being limited on the number of blocks, as not to allow the graphs to
become inscrutable, and as mentioned on the introduction this also allows
making assumptions about the interface which reduce the complexity such as
not needing an explicit flow line, more on the explicit flow line can be read
in the implementation chapter.


[^plc]: Programable Logic Controllers are industrial digital computers used for
    controlling a manufacturing process.
