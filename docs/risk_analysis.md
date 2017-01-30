Risk Analysis
=============

Stakeholders
------------
I.  Project author
II.  Users (Non technical background)
III.  Academic Reviewers (Project Supervisor, Moderator...)

On the case of the project author is the main stakeholder, his aim being
developing a satisfactory project.

The users in this particular case play a particularly active role on
development and their existence influenced the design of the project,
particularly the interface for interaction.

The academic reviewers play a support role on the project, they are concerned
with ensuring the report follows the university guidelines and making sure
the development stays on course.

Prevention & Mitigation
-----------------------

| Risk Factor  |     Low Impact     |     Medium Impact    |    High Impact   |
|:------------ |:------------------:|:--------------------:|:----------------:|
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
do.


Same goes for major errors on the platform we are using, some alternatives were
considered but in case of a major failure later down the line the only real
solution is rewriting those parts. For preventing these issues a technical
analysis of the capabilities of the platform must be done before starting the
project, identifying possible faults and providing possible solutions and or
alternatives.

