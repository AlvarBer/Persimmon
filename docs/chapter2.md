Objectives
==========
The best way we can describe the project is by dividing the objectives.
and the best way to understand the progression of those and their relation
is with a diagram.


\begin{figure}
	\centering
	\caption{Objectives Tree}
	\begin{tikzpicture}
	\draw (-1, 1.4) rectangle (1, 2.1) node[midway, gray] {Capped};
	\draw [->, gray, thick] (0, 2.2) -- (0, 2.7);
	\draw (-1, 2.8) rectangle (1, 3.5) node[midway, gray] {Parity};
	\draw [->, gray, thick] (0, 3.6) -- (0, 4.3);
	\draw (-1, 4.4) rectangle (1, 5.1) node[midway, gray] {Compilation};
	\draw [red, dashed] (-3, 5.5) -- (3, 5.5) node[below left] {Out of scope};
	\draw [->, gray, thick] (-0.1, 5.2) -- (-2, 5.9);
	\draw [->, gray, thick] (0.1, 5.2) -- (2, 5.9);
	\draw (-3, 6) rectangle (-1, 6.7) node[midway, gray] {Web};
	\draw (1, 6) rectangle (3, 6.7) node[midway, gray] {Synthesis};
	\end{tikzpicture}
\end{figure}

**Capped** is more than a minimum viable product, a extensive proof-of-concept, 
with a few limited algorithms and the ability of inputing `.csv` files. with a
restricted interface in which we don't drag & drop algorithms but merely select
buttons.

**Parity** means a more or less complete parity in terms of features and visual
interaction. we don't really care much about having the same number of 
underlying algorithms because that's not the focus of the project.

And the final objective is **compilation**, the ability to get the python 
source code from the visual representation. also improving the interface to
have a better flow, such as in unreal blueprints, which provide a very 
intuitive interface [@shah2014mastering].

Out of scope, but further applications of the system are **web/junyper**
integration that means the system would be accesible from a website interface,
and script **synthesization**, which is the opposite of compilation, meaning
the ability to visualize on persimmon a python source file.

Now that we understand the objectives we can draw a much detailed gantt diagram.

\begin{figure}
\caption{Gantt Diagram}
\begin{ganttchart}[
	hgrid,
	vgrid,
	time slot format=isodate-yearmonth,
	x unit=2cm,
	compress calendar,
	inline,
	]{2016-10}{2017-04}
	\gantttitlecalendar{year, month=name} \\
	\ganttbar{Distil Idea}{2016-10}{2016-10} \\
	\ganttbar{Planning}{2016-11}{2016-12} \\
	\ganttgroup{Implementation}{2016-12}{2017-03} \\
	\ganttbar{Iteration 1}{2016-12}{2017-01} \\
	\ganttlinkedmilestone{Capped}{2017-01} \\
	\ganttlinkedbar{Iteration 2}{2017-02}{2017-02} \\
	\ganttlinkedmilestone{Parity}{2017-02} \\
	\ganttlinkedbar{Iteration 3}{2017-03}{2017-03} \\
	\ganttlinkedmilestone{Compilation}{2017-03} \\
	\ganttbar{Report Building}{2016-10}{2017-03}
	\ganttbar{Refinement}{2017-04}{2017-04} \\
\end{ganttchart}
\end{figure}

We ommited previous months that included idea refinement but are not 
interesting for us.

