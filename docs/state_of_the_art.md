State of the art
================

> Those who forget the past are condemned to 
> repeat their mistakes in the future.
Some dude a long time ago.

Before we start working on Persimmon let's take a look at the previous works
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



Here is where we thought about contacting the *"e-learning UCM"* research group 
at our university because we saw an opportunity to bring the power of the data 
science to the educational world, in this case via the educative games. We 
thought that was a perfect idea because we will try to help them with a tool 
that makes easy to measure if the educational-games were getting to where they 
are expected to, meaning if they are really helping to teach their users what 
they are supposed to. At the same time we finally decided to make our project 
open source since many educational games do not have a big budget and in this 
way our program would be accessible to all of them and they can even tweak some 
parts of our project if they really need to.  
  
Here is where we started thinking about which technology to use and the first 
part was very clear, we both have already worked with Python for data science 
in the past and we thought it has a quite good environment for it, but our main
goal for the project was to give all the power of the data science to people 
that may have rarely been working with data science so we needed to find a way 
of representing it so it was easy to understand and use. So after looking for 
several Python UI libraries we finally chose _kivy_ because we thought it could
fit quite well with what we want to do.  
The last remaining thing to do before starting with the project itself was to 
think in which way we would like to represent the information because for our 
purpose of doing a very accessible and easy to use understand and use program 
that part was very important. The main idea we got to was an interface in which
you have all the different data science algorithms and just by dragging and 
dropping them you can build build more complicated algorithms by concatenating 
them. At the same time you can configure each of the algorithms that you drag to
have the desired parameters. In this part we got the idea by looking at the 
Microsoft Azure platform that in a sense is some similar to what we want to do
when talking about the interface. We thought that was a really good way of 
handling the several machine learning algorithms and it makes it so easy to add
new ones, or to move them from one place to another, but at the same time we saw
an opportunity to improve the part that we really don't like about
Microsoft Azure platform and this part is that the whole computation is done in
the "cloud", meaning this at the Microsoft servers and we wanted to give the 
whole power to the actual end user.

