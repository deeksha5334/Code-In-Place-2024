# Code-In-Place-2024
Stock Market Analyzer using APIs

Stanford Code In Place 2024 – Final Project Python
(Documentation)
STOCK MARKET ANALYSER
This program was an introductory attempt to inculcate use of APIs to develop more robust applications. I have made use of two APIs - Alpha Vantage API (Stock Market Data) and ExchangeRate API (Exchange Rates for various currencies). I have implemented basic API endpoints to extract real-time stock market data. Accessing the data (in form of dictionaries) from the json file and implementing them into the program, making HTTPS requests to the API and implementing API endpoints are some of the methods involved.
Understanding the stock market is not as difficult as it seems to be. This program serves as a Stock market Analyser which helps users evaluate the rapidly changing behavior of the stock market and helps them make better investing decisions.
The program is menu driven and displays a numbered list of options for the user to choose from. If the user enters an invalid choice, the program asks for input again. This takes place until the user enters a correct choice. The user can search for stocks, get stock quotes, get stock history, evaluate a stock, print global stock status, convert currency, and get top stock recommendations based on the choices.

Alpha Vantage Endpoints used
1. QUOTE ENDPOINT
   Function: GLOBAL QUOTE
   https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=dem o

2. SEARCHENDPOINT
   Function: SYMBOL_SEARCH
   https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=SAIC&apikey= demo

3. TIME SERIES DATA
   Function: TIME SERIES DAILY
   https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey= demo

Functionality of the program
• Search_Stocks(symbol)
function = 'SYMBOL_SEARCH'
This function was implemented to search for a stock based on the symbol provided by the user. It is useful for identification of stocks of various companies.

• Display_Stocks(stocks)
This function displays the following elements of the stock after extracting the data from the endpoints of the API. This is based on updated real time data.
− Symbol of the stock
− Name of the stock
− Type of the stock
− Region the stock is based from
− Currency the stock is in

• Get_Stock_Quote(symbol)
The stock quote provides a summary of the stock price. It displays the following elements:
− Symbol of the stock
− Price of the stock at the beginning of the day (Open)
− Price of the stock at the closing of the day (Close)
− Highest price the stock has been traded for
− Lowest price the stock has been traded for
− Price of the stock
− Number of shares traded in a stock (Volume)
− Latest Trading Day
− Change Percent, which indicates the percent change of the stock price since the
close of the previous day

• Get_Stock_History(symbol)
This function retrieves the stock history for the past 100 days.
• Display_Stock_History
This function prints the history of stock data since the last 100 days.
  
• Currency_Conversion
Takes input from the user for the amount to be converted along with the currency From and currency To. Returns the current exchange rate, and the converted amount for that rate.

• Evaluate_Stock
Provides an evaluation of the stock using the following elements:
− The stock’s recent closing prices
− The average close price
− The latest close price
− Prints a result about whether it is a good idea to invest in the stock.

• Recommend_Stocks
Recommends the list of Top 5 stock recommendations to trade in.

• The main() function
Implements a menu for the user to choose from.

Applications
This program would also serve as an educational tool to the users who are beginning to acquaint themselves with the stock market. By getting real-time data and detailed stock quotes, they can understand how trends are being influenced by exchange rates, fluctuations, supply and demand.
Investors would be able to track the stocks they are interested in and analyze the daily trends. It helps them make investing decisions. Users can also track their personal finances and observe the trends of their favourite stocks. It helps learners understand and evaluate the behavior of the stock market by studying the characteristics of stock data.
Currency conversion was implemented for the users’ convenience, so that they can convert the currencies of the stocks into their local currencies. Moreover, with the exchange rates it gives an idea about how these rates have been impacting the value of investments in different currencies. With currency conversion, an investor in the US for instance, can invest in stocks from the European Trade market by following the suitable conversion.

Scope for improvement Accuracy in Analysis
My program does not yet provide accurate recommendations to the user. This is a basic implementation which evaluates the latest close and average close of the stock and determines the result. The range over which the results are based of is limited. However there is a huge scope for improvement in terms of analysis and evaluation of stocks. The program can use deeper data analyzing tools available in Python.

Visualizing the data
The program can be improvised to plot the trends the stock market is undergoing real-time, by using python libraries like Matplotlib and Plotly. We can add elements of visual representation to the program so that it is more accurate when studying the behavior of the stock market. There is always room for implementing more APIs to enhance the functionality.

Implementation of top recommendations
In the program, I have implemented just a sample function for “Top 5 Stock recommendations” (Data temporarily fetched from Yahoo Finance). However this function would be useful for the user to make choices based on real-time stock trends that are fetched from the API. Several elements like “relative strength index (RSI)”, averages and closing quotes can be used to draw the concussion.

Error Handling
We can implement a more advanced error handling mechanism which would give the return codes while fetching data from the API so that the user can identify where the access is being denied. Error handling is needed to support technical difficulties, when the API limits requests and when the data encounters an issue.

REFERENCES
Exchange Rate API
[https://www.exchangerate-api.com](https://www.exchangerate-api.com)

Exchange Rate Documentation
[https://www.exchangerate-api.com/docs/overview](https://www.exchangerate-api.com/docs/overview)

Exchange Rate Example Request:
[https://v6.exchangerate-api.com/v6/66bbe3895a8ece0cb430aca9/latest/USD](https://v6.exchangerate-api.com/v6/66bbe3895a8ece0cb430aca9/latest/USD)

Alpha Vantage API
[https://www.alphavantage.co](https://www.alphavantage.co)
    
Alpha Vantage Documentation
[https://www.alphavantage.co/documentation/](https://www.alphavantage.co/documentation/)

Current top 5 stock recommendations (Sample implementation in the program)
[Most Active Stocks Today -](https://finance.yahoo.com/most-active/) Yahoo Finance

Understanding a stock quote - Investopedia
[How to Understand a Stock Quote](https://www.investopedia.com/articles/investing/093014/stock-quotes-explained.asp)
