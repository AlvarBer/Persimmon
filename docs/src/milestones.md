Milestones
==========

In order to guarantee the delivery of the software a incremental software
development has been chosen, this implies breaking down the objectives into
smaller milestones that can be reached more easily, so in case the last
milestone is not reached there is still a substantial product to submit.


Tree
----

![Milestones Tree](images/objectives.pdf)

**Capped** is more than a minimum viable product, a extensive proof-of-concept,
with a few limited algorithms and the ability of inputing `.csv` files, with a
restricted interface in which we don't drag & drop algorithms but merely select
buttons.

**Parity** means a more or less complete parity in terms of features and visual
interaction. It is not very important to have the same number of
underlying algorithms because that's not the focus of the project.

And the final milestone is **Compilation**, the ability to get the python
source code from the visual representation, also improving the interface to
have a better flow, such as in unreal blueprints, which provide a very
intuitive interface [@shah2014mastering].

This milestone would bring Persimmon utility outside just the realm of
learning, as it would be a convenient tool for the exploratory work of any
ML solution (Business case, a Kaggle[^kaggle] competition, etc...

Out of scope, but possible further applications of the system are **web/junyper**
integration that means the system would be accessible from a website interface,
and script **synthesization**, which is the opposite of compilation, meaning
the ability to visualize on persimmon a python source file.

Gantt Diagram
-------------


With the settled milestones a Gantt diagram of the project development can be
drawn.

<!-- Improve Gantt Diagram according to previous feedback. -->
![Gantt Diagram of the project development.](images/gantt.pdf)


Development Methodology
-----------------------
The chosen methodology is based on agile methodologies such as **Scrum** or
**Extreme Programming**, with two weeks sprints, using a board to keep track of
all current and future tasks.

However there are some fundamental changes, since there is no team and there is
no need for superfluous and unnecessary processes. There is no retrospective
after each sprint, there is no specific weight or cost assigned to each task.
During a sprint the next sprint tasks are moved from the product backlog into
the sprint planning column and broken down further if necessary.

Task are defined by use cases and can be broken down further by using
checklists on the tasks.

If a task is not fully completed it can be moved back onto the product backlog.

The trello board can be found at [trello](https://trello.com/b/JmG3xy0U/persimmon).


[^kaggle]: [Kaggle.com](https://www.kaggle.com/)
[^trello]: trello is a software for having a digital board where tracks can be
    pinned.

