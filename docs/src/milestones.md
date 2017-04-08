Milestones
==========

In order to guarantee the delivery of the software an incremental approach
has been chosen, this implies breaking down the objectives into
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

<!-- Improve Gantt Diagram according to previous feedback?. -->
![Gantt Diagram of the project development.](images/gantt.pdf)


Development Methodology
-----------------------
The chosen methodology is based on agile methodologies such as **Scrum** or
**Extreme Programming**, meaning that there is not a complete model of the
desired system like in model driven development, nor a complete planning of
every development detail such as on a Waterfall development at the start of
development, instead there are continuous iterations, faster and smaller than
traditional development iterations that allow for more opportunity to react and
adapt to change.
This iterations last two weeks and are called sprints, and a board is used to
keep track of all current and future tasks.

On a traditional Scrum methodology the product owner puts uses cases (*items*)
into the product backlog.
Each sprint the scrum master and the development team have a meeting called
*Sprint Planning event* where items the current sprint items from the product
backlog to be done are decided and broken down into tasks to be done.
Items can also be pushed back into the backlog if they are not achievable or
have a lower priority.

However this methodology does not really fit the development of the project,
since there is no team, there is no need for superfluous and unnecessary
processes.
There is no retrospective after each sprint and there is no specific weight or
cost assigned to each task.
During a sprint the next sprint tasks are moved from the product backlog into
the sprint planning column and broken down further if necessary.

Task are defined by use cases and can be broken down further by using
checklists on the tasks.

If a task is not fully completed it can be moved back onto the product backlog.

The planning board can be found at [trello](https://trello.com/b/JmG3xy0U/persimmon).


[^kaggle]: [Kaggle.com](https://www.kaggle.com/)
[^trello]: trello is a software for having a digital board where tracks can be
    pinned.

