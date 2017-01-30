State of the art
================

Before we start working on the system let's take a look at the previous works
for both inspiration and avoiding pitfalls.

Azure ML
--------
The most obvious inspiration and arguably the most successful, is undeniable
that Microsoft product managed to hit the market with a product nobody know
they wanted but everybody needed. As a platform has a lot that we like,
a lot of different preprocessing steps, runs on the cloud, has a web interface.


But some of these features are also shortcomings, the web interface feels a
bit clunky, low FPS and lack of native support means that dragging and dropping
don't feel as smooth as they should. Cloud support is very good, but for
sensitive such as financial or medical data a self hosted version is a must.
The variety of algorithms is interesting, but the lack of ability to extend
them is a pity, we know that azure is written on R, but because is closed
source we can't extend the code in any meaningful way.


Unreal Engine 4
---------------
This one may be a bit unexpected, but the inspiration here comes from the
Blueprint system. Arguably the best visual programming interface to come on the
last years, it strives to be a complete programming language, even going as far
as presenting conditionals as blocks.


The flow of the interface is impressive, when one cable is dragged from a block
a prompt appears with only the blocks that make sense to be connected to the
previous block. This little feature makes creating complex programs a breeze,
allowing the user to forget about the exact details of the API.

