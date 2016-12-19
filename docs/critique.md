Project Critique
================

### Acknowledgments
To [@pandoc] for providing Pandoc, the tool to produce quality reports from
Markdown, [@pgfgantt] for the pgfgantt package for LaTeX that allows drawing
gantt diagrams, and [@emerald] for providing the csl style for Harvard style 
citations.


Project Description
-------------------
On the project **Smart Data: Using web Applications to Demonstrate Term
Frequency** the author tackles the problem of data mining on text, a topic
that has found recently a lot of demand thanks to the boom of Big Data and
datascience.
The abstract gives us a good overview of what the project is going to be,
and there is an extensive investigation of tools, previous systems, ethics 
concerns and literature on both the topic and project development itself.

The hypothesis is that the ability for the output to be viewed in a graphical 
form on web browsers will allow non-technical users to reap knowledge of the 
data without requiring them to become experts at the methods or the processing 
of the corpus.
Coupled with the ability to specify on-line text streams such as twitter means
that the user does not need to worry about converting the data into csv files 
or creating a database to process.
The author sets to use the `R` programming language for this task, a tool came 
out as the most suitable on the existing systems analysis.

Although the approach to the problem is supported by various sources, mostly the
method of analysing and filtering the data, the author commits a few acts that 
go against what is perceived as good practices on the field, such as using
a small dataset for both performance and logistic reasons, as this has 
drawbacks such as producing a high bias which is more prone to appear in smaller
datasets [@pitfalls] and becoming more vulnerable to common pitfalls such as biased slices 
in cross-validation [@failures].

Evaluation of Project
---------------------
The implementation of this project was a textual analysis system that would gain
knowledge of an individual in a hiring process, particularly whether the account
owner is a team player or they work better on their own, in order to predict 
that the frequency of words terms is extracted and presented, using the package
`twitteR` the information was extracted from the account, followed by a 
preprocessing phase in which tasks such as removing non-alphabetical characters
would be performed on the text, then the KNN[^KNN] algorithm would be applied to 
the data, giving us the desired information off the corpus. Finally the 
information is given to the user through graphs on a website.

The testing of the implementation (Specifically the classification algorithm)
was done using classic out-of-sample evaluation, however the percentages of the
split are not specified.
In designing the web interface the **Tufle's** and **Bertin's Principles** were used as
a reference on the information architecture, how whitespace and information
density must be handled, and has to remain consistent through the whole 
application, while the graphs were made following **Gestalt Theory**, focusing first
on the whole object rather than the small details we perceive later.

The Scientific Method is applied to different parts of the project (The 
algorithm, the preprocessing) and the set of principles the main hypothesis
will be tested again is explained, but there is not any kind of external
evaluation by potential users, just the satisfaction of the developers with
the system, which is positive and valid, but is subject to bias and 
subjectivity.
The original Hypothesis is considered proven right by the author.

In my opinion the project has a solid basis, the hypothesis, as previously 
stated, is (at least partially) supported by the literature, and it proves that
the developed solution is suitable for the task proposed, but because the system
is never fully tested there are possible faults that can be undetected, such as 
using a more "exotic" set of tweets on which the preprocessing may fail or the 
Machine Learning doesn't performs as well [@understand], and because the final output is not 
evaluated by potential users the resulting interface can probably be improved 
according to their feedback.

In fact because only one use case was presented it is hard to imagine the 
variety of other scenarios where this system could be applied without knowledge 
of the underlying statistical principles, which is against the project goal.
On the other side the successful integration of the whole systems positively 
impacts the usefulness of the software.

Assessment of Conclusions
-------------------------
The conclusions derived from the project seem to indicate this kinds of system
do help gaining this kinds of insight, even when the data is not that big.
Despite the performance limitations the ability to visualize in easy to consume
formats such as multivariate graphs, bar plots or pie graphs seems to helps 
gaining the desired information by the user. This idea is supported by 
[@principles] and [@fry2007visualizing].

The proposed further study/possible improvements focus mostly on the corpus
extraction function, as there were some limitations to both the `twitteR` 
package and the filtering methods, as these seem to not be as extensive and
customizable as expected. In fact it is shown that there is a need for a custom
grammatical rules for more complex needs. But for the smaller cases of study the
default seems to work good enough.

Risks
-----
In order to analyse the risks and the prevention and countermeasures we first 
need to identify all the stakeholders that this projects involved

### Stakeholders
I.  Project author
II.  Users (Non technical background)
III.  Academic Reviewers (Project Supervisor, Moderator...)

On the case of the project author is the main stakeholder, his aim being 
developing a satisfactory project.

The users in this particular case didn't play a particular active role on 
development but their existence influenced the design of the project, 
particularly the appearance of the final output (Web interface, graphs, etc...)

The academic reviewers play a support role on the project, they are concerned 
with ensuring the report follows the university guidelines and making sure
the development stays on course.

### Prevention & Mitigation

| Risk Factor  |     Low Impact     |     Medium Impact    |    High Impact   |
|--------------|--------------------|----------------------|------------------|
| Requirements | Not defined enough | Change at late stage | Unreachable goal |
|  Technology  | Performance issues |   Interoperability   |   Major errors   |

For the not defined enough requirements a break by user goals (exemplified by
the use case diagrams) can help make clear what the requirement is exactly.
If a requirement change appears at a late stage we can mitigate the impact by 
employing an agile methodology (Like **Scrum** or **Kanban**) that allows us to work
on smalls sprints and refocus on ever-changing requirements.
In the case of an unreachable goal we could stablish partial objectives that 
can be archived, splitting our goal into several smaller goals, making it 
easier to at least some, if not all.

Performance issues like the ones the project suffered can be countered with 
reducing the data we use to do the processing, making it more of a proof of 
concept while retaining the validity of the project claims. Another solution is
caching the results of the bottlenecks (Expensive operations) and using those
results in the final application.
On the other hand there is no easy solution for interoperability issues, 
besides changing development platform/core language there is not a lot we could
do. On this project a lot of these kind of issues are avoided by delivering
the results through a website.

Same goes for major errors on the platform we are using, some alternatives are
considered but in case of a major failure later down the line the only real
solution is rewriting those parts. For preventing these issues a technical 
analysis of the capabilities of the platform must be done before starting the
project, identifying possible faults and providing possible solutions and or 
alternatives.

Project Plan
------------

### Motivation, Context and Purpose
I started thinking about my final project at the end of last course, consulting
with both different teachers and colleagues. I just learned about Machine 
Learning and was very excited about the possibilities.
At that time I was thinking in doing a study of different ML techniques applied
to serious/learning games in order to determine if players of a game were 
archiving the objectives the developers were trying with those games.

But this summer I worked on a financial company, doing mostly algorithmic 
trading and market analysis. There, amongst other duties, I aided with 
moving the codebase from `MATLAB` to `Python`, and during that process I 
realised many of my co-workers struggled with the transition, as they were not
computer scientists, but came from a variety of backgrounds such as Maths, 
Physics, Electric Engineering, Statistics, etc...

Yet they were the whole of the department, as this topic requires a high 
level of theoretical maths knowledge, and so happens that these subjects tend 
to not have a lot of general programming skills, they mostly work with 
specialized languages, tailored to these tasks such as `MATLAB`, `R`, `Julia`,
etc, and moving to a general purpose language such as Python involves learning
about a plethora of additional topics.

The situation is even more complicated for newcomers to Machine Learning from 
these backgrounds, as they not only have the programming barrier but also have
to overcome the difficulties of the algorithms themselves, something Computer 
Scientists also struggle with (In many cases even more because their weaker 
maths skills)

So this project servers a double purpose, it helps with the programming 
barrier, and aids with the Machine Learning process as it allows the learner to
focus on the connections, intuitions and mathematical basis and not on the 
implementation details and the quirks of the concrete language.

### Key Tasks
The best way we can describe the project is by dividing the objectives.
And the best way to understand the progression of those and their relation
is with a diagram.

![Objectives Tree](objectives.png)

**Capped** is more than a Minimum Viable Product, a extensive proof-of-concept, 
with a few limited algorithms and the ability of inputing `.csv` files. With a
restricted interface in which we don't drag & drop algorithms but merely select
buttons.

**Parity** means a more or less complete parity in terms of features and visual
interaction. We don't really care much about having the same number of 
underlying algorithms because that's not the focus of the project.

And the final objective is **Compilation**, the ability to get the Python 
source code from the visual representation. Also improving the interface to
have a better flow, such as in Unreal Blueprints, which provide a very 
intuitive interface [@shah2014mastering].

Out of the scope, but further applications of the system are **Web/Junyper**
integration that means the system would be accesible from a website interface,
and script **Synthesization**, which is the opposite of Compilation, meaning
the ability to visualize on Persimmon a Python source file.

Now that we understand the objectives we can draw a much detailed Gantt Diagram.

![Gantt Diagram](gantt.png)

We ommited previous months that included idea refinement but are not 
interesting for us.

Bibliography
------------

[^KNN]: K-nearest neighbors, a classification and regression algorithm that
	classifies data by the closest training examples found
