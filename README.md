# Foreign Exchange Weighted Average Calculator
A vast majority of trading in the foreign exchange market as well as many other markets is  considered high frequency trading (HFT), where transactions are executed by machines, allowing the process to be automated and the calculations to be made at a rapid rate on a great scale.  With this notion in mind, one foreign exchange trade is usually comprised of several other smaller trades all with different notional values and different prices.  To determine the total notional value of the base currency position and the average price, a weighted average formula must be  applied.

The primary goal of this project is to provide a basic weighted average function that with a little modification, can not only be used in foreign exchange but also many other asset classes as well.

## Using the Foreign Exchange Weighted Average Calculator
First, import List from the typing library followed by holding shift and pressing enter.

Next, copy and paste the fx_weighted_average function into a cell and again hold shift and press enter.  If you would like to enter amounts over 100 units, please comment out (enter # next to each line) the assert statement in the code block "an amount in amounts must be between 1 and 100".  In addition, if you would like to change the multiplier value of the asset, modify the constant value of 1,000,000 in the amounts_1_mio local variable.

Lastly, type fx_weighted_average() and within the paranthesis, enter two lists seperated by a comma with one representing the values of each amount and the other with prices.  Please note that each value should be in the same order in the list as its corresponding price otherwise the weights will be missasinged.
