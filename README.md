# Foreign Exchange Weighted Average Calculator
A vast majority of trading in the foreign exchange market as well as many other markets is  considered high frequency trading (HFT), where transactions are executed by machines, allowing the process to be automated and the calculations to be made at a rapid rate on a great scale.  With this notion in mind, one foreign exchange trade is usually comprised of several other smaller trades all with different notional values and prices.  To determine the total notional value of the base currency position and the average price, a weighted average formula must be  applied.

The primary goal of this project is to provide a basic weighted average function that can not only be used in foreign exchange but also many other asset classes as well.


## Using the Foreign Exchange Weighted Average Calculator
First, import List from the typing library followed by holding shift and pressing enter.


Next, copy and paste the fx_weighted_average function into a cell and again hold shift and press enter.

If you would like to enter a lot over 100, please comment out the entire assert statement in the code block (enter # next to each line) or change the constant 100 to the desired threshold.

In addition, in currency trading, a lot represents a certain amount of units which in this case is 1,000,000.  If you would like to change the unit size, simply modify the constant value of 1,000,000 in the lots_1_mio local variable.

Lastly, type fx_weighted_average() and within the parenthesis, enter two lists separated by a comma with one representing all the transacted lots and the other with the corresponding prices.  Please note that each lot should be in the same order of the last as its associated price or the weights will be incorrect.
