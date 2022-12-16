# Foreign Exchange Weighted Average Calculator
A vast majority of trading in the foreign exchange market as well as many other markets are considered high frequency trading (HFT), where transactions are executed by machines, allowing the process to be automated and the calculations to be made at a rapid rate on a great scale.  With this notion in mind, one foreign exchange trade is usually comprised of several other smaller trades all with different notional values and prices.  To determine the total notional value of the base currency position and the average price, a weighted average formula must be applied.

The primary goal of this project is to provide a basic weighted average function that can not only be used in foreign exchange but also many other asset classes as well.

## Using the Foreign Exchange Weighted Average Calculator
First, import List from the typing library followed by holding shift and pressing enter.

<img src="images/Screen Shot 2021-12-06 at 12.15.26 PM.png" width="210" height="20">

Next, copy and paste the fx_weighted_average function into a cell and again hold shift and press enter.

If you would like to enter an amount over 100, please comment out the entire assert statement in the code block below (enter # next to each line) or change the constant 100 to the desired threshold.

<img src="images/Screen Shot 2021-12-06 at 12.15.45 PM.png" width="585" height="55">

In addition, amount represents 1,000,000 units.  If you would like to change the size, simply modify the constant value of 1,000,000 in the amounts_1_mio local variable.

<img src="images/Screen Shot 2021-12-06 at 12.16.09 PM.png" width="385" height="25">

Lastly, type fx_weighted_average() and within the parenthesis, enter two lists separated by a comma with one representing all the transacted amounts and the other with the corresponding prices.  Please note that each amount should be in the same order of the list as its associated price or the weights will be incorrect.

<img src="images/Screen Shot 2021-12-06 at 12.17.02 PM.png" width="400" height="23">

Using the provided example above, the output should look like this: 6,000,000 @ 1.11290

## Risk Disclosure
Gregory DeSantis is not a registered broker, analyst, investment advisor or anything of that sort.  This project is purely for guidance, informational and educational purposes.  All information contained herein should be independently verified and confirmed.  I do not accept any liability for any loss or damage whatsoever caused in reliance upon such information or services.  Please be aware of the risks involved with any trading done in any financial market.  Do not trade with money that you cannot afford to lose.  When in doubt, you should consult a qualified financial advisor before making any investment decisions.

## Disclaimer
Trading and investing in the foreign exchange market involves substantial risk of loss and is not suitable for every investor.  The valuation of currencies and futures may fluctuate, and, as a result, you may lose more than your original investment.  The highly leveraged nature of futures trading means that small market movements will have a great impact on your trading account and this can work against you, leading to large losses or can work for you, leading to large gains.

If the market moves against you, you may sustain a total loss greater than the amount you deposited into your account.  You are responsible for all the risks and financial resources you use and for the chosen trading system.  You should not engage in trading unless you fully understand the nature of the transactions you are entering into and the extent of your exposure to loss.  If you do not fully understand these risks you must seek independent advice from your financial advisor.

All trading strategies are used at your own risk.

Any content in this project should not be relied upon as advice or construed as providing recommendations of any kind.  It is your responsibility to confirm and decide which trades to make.  Trade only with risk capital; that is, trade with money that, if lost, will not adversely impact your lifestyle and your ability to meet your financial obligations.  Past results are no indication of future performance.  In no event should the content of this correspondence be construed as an express or implied promise or guarantee.

Gregory DeSantis is not responsible for any losses incurred as a result of using any of our trading strategies.  Loss-limiting strategies such as stop loss orders may not be effective because market conditions or technological issues may make it impossible to execute such orders.  Information provided in this correspondence is intended solely for informational purposes and is obtained from sources believed to be reliable. Information is in no way guaranteed.  No guarantee of any kind is implied or possible where projections of future conditions are attempted.

None of the content published in this project constitutes a recommendation that any particular currency, portfolio of currencies, transaction or investment strategy is suitable for any specific person.  None of the information providers or their affiliates will advise you personally concerning the nature, potential, value or suitability of any particular currency, portfolio of currencies, transaction, investment strategy or other matter.

The content provided in this project is solely for educational purposes.  The generic market recommendations provided are based solely on my personal judgment and should be considered as such.  You acknowledge that you enter into any transactions relying on your own judgment.  Any market recommendations provided are generic only and may or may not be consistent with the market positions or intentions of myself.  Any opinions, news, research, analyses, prices, or other information contained in this project are provided as general market commentary, and do not constitute an investment advice.

CFTC RULE 4.41 – HYPOTHETICAL OR SIMULATED PERFORMANCE RESULTS HAVE CERTAIN LIMITATIONS. UNLIKE AN ACTUAL PERFORMANCE RECORD, SIMULATED RESULTS DO NOT REPRESENT ACTUAL TRADING. ALSO, SINCE THE TRADES HAVE NOT BEEN EXECUTED, THE RESULTS MAY HAVE UNDER-OR-OVER COMPENSATED FOR THE IMPACT, IF ANY, OF CERTAIN MARKET FACTORS, SUCH AS LACK OF LIQUIDITY. SIMULATED TRADING PROGRAMS IN GENERAL ARE ALSO SUBJECT TO THE FACT THAT THEY ARE DESIGNED WITH THE BENEFIT OF HINDSIGHT. NO REPRESENTATION IS BEING MADE THAT ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFIT OR LOSSES SIMILAR TO THOSE SHOWN.
