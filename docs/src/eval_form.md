Persimmon Evaluation
====================

Preparation
-----------

Please go to [https://github.com/AlvarBer/Persimmon/releases] and
download the latest executable. You will also need to download the
iris dataset along with it.

Previous Questions
------------------
Please tell us something about yourself first.

\question How familiar are you with Machine Learning?

\xfamiliar

\question How familiar are you with Data Mining?

\sevenboxes{}{}{}{}{}{}{}

\question How familiar are you with tools such as Weka, RapidMiner,
Azure ML Studio, etc?

\sevenboxes{}{}{}{}{}{}{}


Tasks
-----

For the first task you will create a small pipeline using persimmon blocks.

* Execute `Persimmon.exe`, spawn a *"Read csv"* block from the **Input/Output**
    tab and using the file dialog locate the **iris.csv** file you have
    downloaded earlier.
* Spawn a classificator block from the **Classificators** tab (any will
    suffice), and a *"K-fold block"* (from the **Cross Validators** tabs).
* Now spawn a *"cross-validation score block"* (which can be found at the
    **Model Selection** tab) and connect the previous three blocks to the
    *"cross-validation score"* block.
* Finally pipe the result from that block into a *"print"* block (again on the
    **Input/Output** tab).

Congratulations! You just made your first pipeline.

\question Overall, how did you find this task?

\xdifficulty

For the second task you will learn about reconnecting cables, if you
have not already, you will also change the output, putting the result
into a file instead off on the screen.

* Spawn a *"Fit"* block (**Fit & Predict** tab), and reconnect the previous
    input block and the estimator to it.
    Make sure you leave the previous *"cross validation score block"*
    completely unconnected, another possiblity is to restart the program
    to delete all blocks.
* Spawn another *"Read csv"* block and load file *"iris_no_class.csv"*.
* Spawn a *"Predict"* block, and connected the result from the fit block onto
    the first input pin and the new *"Read csv"* to the second one.
* Now pipe that result into a *"Write csv"* (**Input/Output** tab) block.
    Put a valid filename on the file dialog text input and execute.

You just predicted a dataset using a previously fitted estimator!

\question Overall, how did you find this task?

\xdifficulty

For the final task you will use several complex blocks, and by doing so will
also perform hyper-parameter optimization using a grid search.

* Spawn *"Grid Search"* block from the **Model Selection** tab.
    Orphan both the *"Fit"* and *"Predict"* blocks you previously created and
    connect the first *"Read csv"* block (the one with *"iris.csv"*) to the
    *"Grid Search"* block.
* Spawn a *"SVM"* block from the **Classificators** (if you had not before).
    Connect it to the *"Grid Search"*.
* Spawn a *"Dictionary"* block (**State** tab). This block is a bit different
    to the previous, it requires that you write a Python dictionary with the
    params you want to test, write
    *"{'C': [0.03, 0.3, 1], 'tol': [0.00001, 0.0001, 0.001]}"* (without the
    outer double quotes but take care to write the iner single quotes).
    Once you are done connect the params block to the *"Grid Search"*.
* Finally pipe the **second** result of the grid search into a *"Print"* block.

The results on the screen are the best parameters along the best score.

\question Overall, how did you find this task?

\xdifficulty

Additional Feedback
-------------------
\freequestion List 2 negative aspects of the application.

\freequestion List 2 positive aspects of the application.

\freequestion Please tell us any additional feedback you may have.

Thanks for taking the time to participate on this evaluation.

[https://github.com/AlvarBer/Persimmon/releases]: https://github.com/AlvarBer/Persimmon/releases
