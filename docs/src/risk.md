Risk Analysis
=============

Since there is a significant number of different stakeholders with different
interest on the project it is necessary to lay down the risk associated and
planning for the biggest and more probable risks.


Stakeholders
------------
I.  Project author.
II.  Academic Reviewers (Project Supervisor, Moderator...).
III.  Users.

On the case of the project author is the main stakeholder, his aim being
developing a satisfactory project.

The academic reviewers play a support role on the project, they are concerned
with ensuring the report follows the university guidelines and making sure
the development stays on course.

The users play an active role on development and their existence influences the
design of the project, particularly the interface.


Prevention & Mitigation
-----------------------
Using [@boehm1991software] let's create a table of risks ordered by impact and
risk factor. Take into account all risks presented on the table are probable.

| Risk Factor  |     Low Impact     |     Medium Impact    |    High Impact   |
|:------------ |:------------------:|:--------------------:|:----------------:|
|   Project    |                    |    Ethics Denial     |  Project Denial  |
| Requirements | Not defined enough | Change at late stage | Unreachable goal |
|  Technology  | Performance issues |   Interoperability   |   Major errors   |

Starting with Project Risks the denial of the proposed hypothesis would be
fatal.
In order to mitigate this mistake a solid report skeleton has to be made early
on, and getting in contact with suitable project supervisors in order to start
morphing the project as soon as possible if required.

Same goes for Ethics Approval denial, in the worst case self-experience of the
software would have to be the main tool to measure user engagement.

For the not defined enough requirements a break by user goals (exemplified by
the use case diagrams) can help make clear what the requirement is exactly.
If a requirement change appears at a late stage the impact is mitigated by the
employment of an agile methodology that allows working on smalls sprints and
refocus on ever-changing requirements.

In the case of an unreachable goal partial objectives could established that
would be easier to archive, splitting the main goal into several smaller goals,
making it easier to at least accomplish some, if not all.
This is explored on the milestones chapter.

Performance issues can be countered reducing the data used for processing,
making it more of a proof of concept while retaining the validity of the
project claims.
Another solution is caching the results of the bottlenecks (expensive
operations) and using those results in the final application.
On the other hand there is no easy solution for interoperability issues,
besides changing development platform/core language there is not a lot that
could be done.

Same goes for major errors on the used platform, some alternatives were
considered but in case of a major failure later down the line the only real
solution is rewriting those parts.
For preventing these issues a technical analysis of the capabilities of the
platform must be carried out before starting the project, identifying possible
faults and providing possible solutions and or alternatives.

<!-- Technical assessment of Kivy / compare kivy to other frameworks -->
