Analysis
========

Raw Data
--------
There were 167 out of 664 malformed `.xml` files. By removing the low level
log entries the number of malformed dropped to 12. This sessions have either a
final high level entry that is incomplete or a single unclosed tag. The most
appropiate procedure is to discard these.

Initial
-------
Before performing some initial analysis on the general characteristics of the
raw data because of the nature of the data much preprocessing is needed.

The data comes as a single `.xml` file per session, they contain all the
low-level inputs and high-level actions by the player in a chronological order.

The events that best represent the flow of the game and that will be used are
the high level ones.
For *La Dama Boba* the set, inc, and event type tells the score of the different
measures found on the game.

There are two strategies to tackle the data, one is getting the final values
of these measures and treat them as parameters, making it easy to collect and
save all the sessions on a single `.csv` files.

But because set events stablish a initial value and the inc, dec alter the
value the most appropriate strategy for treating the data is to take it as a
time series, this makes sense as there is autocorrelation between observations.
In turn a series of additional challenges appear, such that the space between
time measurements is not even (Although it could be transformed to do so),
the need for a cross-validation technique that takes into account time series,
etc...
