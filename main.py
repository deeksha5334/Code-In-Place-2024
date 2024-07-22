#Program that fetches stock market data from Alpha Vantage API and displays the information to the user. This program also uses ExchangeRate API to convert currencies based on existing exchange rates. 
#This program utilises formatted strings
#All the GET requests are made using the requests library. Common HTTP code: 200

"""
Functions - STOCK MARKET ANALYSER

1. Search_Stocks(symbol): 
Searches for stocks based on the user-entered stock symbol
returns a list of dictionaries containing the stock data

2. Display_Stocks(stocks): 
Displays the stocks that were fetched from the API for the user-entered stock symbol

3. Get_Stock_Quote(symbol): 
Displays the stock quote that was fetched from the API with a list of elements
returns a dictionary containing stock quote data

4. Get_Stock_History(symbol): 
Retrieves the stock history of past 100 days for the user-entered stock symbol
returns dictionary containing stock data

5. Display_Stock_History(stocks): Displays the stock history
6. Currency_Conversion(amount, from, to): 
Converts the currency based on the user-entered amount, from currency and to currency
returns the converted amount

7. Evaluate_Stock(symbol): 
Evaluates the stock based on recent performance, and closing values
returns evaluation message about whether it is a good idea to invest in that stock 
(Needs further improvisation for accuracy, this is a basic implementation)

8. Recommend_Stocks(): A Pseudo implementation using currently exisitng recommendations from Yahoo Finance
9. main(): Runs the main program and displays the menu of options for the user to choose from
"""


#Importing the requests library to make HTTP requests to the API
import requests

#Base URL and API keys
ALPHA_VANTAGE_BASE_URL = 'https://www.alphavantage.co/query'
ALPHA_VANTAGE_API_KEY = 'Your-AlphaVantageAPI-Key' 
EXCHANGE_RATE_API_KEY = 'Your-ExchangeRateAPI-Key'

#FUNCTION: Fetches the details of the stock based on the symbol
#Required user input: Stock symbol
def Search_Stocks(symbol):
    #API Endpoint: Fetches stock data based on the user-entered stock symbol
    function = 'SYMBOL_SEARCH'

    #Parameters to be passed to the API endpoint
    params = {'function': function, 'keywords': symbol, 'apikey': ALPHA_VANTAGE_API_KEY}
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params)
    
    #Returns a list of Dictionaries containing the data fetched from the API
    return response.json().get('bestMatches', [])
    
    

#FUNCTION: Displays the results that were fetched from the API
def Display_Stocks(stocks):
    #ERROR HANDLING: If stock symbol is not found in the list, the error message is printed
    if not stocks:
        print("No stocks found.")
        return
    
    #Iterating through the list of stocks and displaying the data
    for stock in stocks:

        #Printing the title
        print("-" * 80)
        print("STOCK INFORMATION")
        print("-" * 80)

        #Gets the details of the stock from the dictionary by accessing the respective keys 
        """
        EXAMPLE FORMAT of data fetched from the API endpoint in .json format: 
        {
            "1. symbol": "SAIC",
            "2. name": "Science Applications International Corp",
            "3. type": "Equity",
            "4. region": "United States",
            "5. marketOpen": "09:30",
            "6. marketClose": "16:00",
            "7. timezone": "UTC-04",
            "8. currency": "USD",
            "9. matchScore": "1.0000"
        }
        """

        #Printing the data by accessing the dictionary keys
        print("Symbol:", stock.get('1. symbol'))
        print("Name:", stock.get('2. name'))
        print("Type:", stock.get('3. type'))
        print("Region:", stock.get('4. region'))
        print("Currency:", stock.get('8. currency'))
        print("-" * 80)


#FUNCTION: Displays the stock quote
#Required user input: Stock symbol
def Get_Stock_Quote(symbol):
    #API Endpoint: Fetches stock quote based on the user-entered stock symbol
    function = 'GLOBAL_QUOTE'
    #Parameters to be passed to the API endpoint
    params = {'function': function, 'symbol': symbol, 'apikey': ALPHA_VANTAGE_API_KEY}
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params)
    
    #Fetches the data from the API endpoint in .json format and stores in the variable "data"
    data = response.json().get('Global Quote')

    #Accessing the datapoints through dictionary indexing
    """
    EXAMPLE FORMAT of data fetched from the API endpoint in .json format: 
    "Global Quote": {
    "01. symbol": "IBM",
    "02. open": "170.0000",
    "03. high": "170.7500",
    "04. low": "168.3800",
    "05. price": "170.5500",
    "06. volume": "3386442",
    "07. latest trading day": "2024-06-18",
    "08. previous close": "169.5000",
    "09. change": "1.0500",
    "10. change percent": "0.6195%"
    }
    """
    if data:
        return {
            'Symbol': data.get('01. symbol'),
            'Open': data.get('02. open'),
            'High': data.get('03. high'),
            'Low': data.get('04. low'),
            'Price': data.get('05. price'),
            'Volume': data.get('06. volume'),
            'Latest Trading Day': data.get('07. latest trading day'),
            'Previous Close': data.get('08. previous close'),
            'Change': data.get('09. change'),
            'Change Percent': data.get('10. change percent'),
        }
    
    #If data is not found, return empty
    else:
        print("No data found for stock symbol", symbol, ".")
        return None



#FUNCTION: Gets everyday "as-traded" data for a stock
#Required user input: Stock symbol
def Get_Stock_History(symbol):
    function = 'TIME_SERIES_DAILY'
    #Parameters to be passed to the API endpoint
    params = {'function': function, 'symbol': symbol, 'apikey': ALPHA_VANTAGE_API_KEY}
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params)

    #Returns a dictionary containing the data fetched from the API
    return response.json().get('Time Series (Daily)', {})
    

#FUNCTION: Displays the stock history that is retrieved from the API
def Display_Stock_History(stock_history):
    if not stock_history:
        print("No historical data found.")
        return
    
    #Prints the header for the tabular format
    print("Date\t\t\tOpen\t\tHigh\t\tLow\t\tClose\t\tVolume")

    #Accessing the items of the dictionary corresponding to the keys 
    """EXAMPLE FORMAT of data fetched from the API endpoint in .json format: 
    "2024-02-13": {
            "1. open": "184.2800",
            "2. high": "184.7700",
            "3. low": "182.3600",
            "4. close": "183.7000",
            "5. volume": "4290453"
        }"""
    for date, data in stock_history.items():
        #Prints the stock history from the past 100 days formatted like a table
        print(date, "\t", data['1. open'], "\t", data['2. high'], "\t", data['3. low'], "\t", data['4. close'], "\t", data['5. volume'])

#FUNCTION: Converts the currency to the desired
#Required user input: Amount, From currency, To currency
def Currency_Conversion(amount, from_currency, to_currency):

    #Base URL used for conversion using the ExchangeRate API
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}'
    response = requests.get(url)
    
    #Fetches the current exchange rate from the API
    rate = response.json().get('conversion_rate', 1)
    print("Current Exchange rate:", rate)

    #Returns the converted amount based on the exchange rate
    return amount * rate
    

#FUNCTION: Evaluates the stock based on recent performance
#Required user input: Stock symbol
def Evaluate_Stock(symbol):

    #Fetches the stock history from the API
    time_series = Get_Stock_History(symbol)

    #ERROR HANDLING: If stock history is not found, it will print error message
    if not time_series:
        print("Failed to fetch data for", symbol + ".")
        return

    #Get the recent 5 days of closing prices
    #Getting the corresponding values from the list by accessing the index values from the ending represented by "[:5]"
    recent_days = list(time_series.items())[:5]

    #ERROR HANDLING: If recent days is not found, it will print error message
    if not recent_days:
        print("No recent data available for", symbol + ".")
        return

    # Get the closing prices for the last 5 days and converting it to float type
    #List comprehension to get the closing prices of the stock for the last 5 days
    recent_closes = []

    for day in recent_days:
        # Accessing the dictionary with stock data for the day
        stock_data = day[1]
        
        # Retrieve the closing price as a string
        closing_price_str = stock_data['4. close']
        
        # Convert string to float
        closing_price_float = float(closing_price_str)
        
        #Adding the closing price to the recent_closes list to calculate the average
        recent_closes.append(closing_price_float)


    # Calculate the average close price
    average_close = sum(recent_closes) / len(recent_closes)
    latest_close = recent_closes[-1]

    # Define a threshold for evaluating the stock and set it to 5%
    threshold = 1.05

    # Evaluate the stock based on recent performance 
    # If the latest close price is more than 5% higher than the average close price for the last 5 days,then the stock is a good investment. Otherwise, it is not a good investment.
    message = ""
    if latest_close > average_close * threshold:
        message = symbol + " looks like a good investment based on recent performance."
    else:
        message = symbol + " might not be a good investment based on recent performance."

    # Display evaluation details
    print("This is an evaluation of the stock:", symbol)
    print("Recent closing prices:", recent_closes)
    print("Average close price:", round(average_close, 2))
    print("Latest close price:", round(latest_close, 2))

    return message


#Sample implementation of a function that recommends top 5 stocks based on recent performance
#Source: Yahoo Finance 
def Recommend_Stocks():
    stocks = ['NVDA', 'AAPL', 'TSLA', 'SIRI', 'PLTR']
    prices = [135.58, 214.29, 184.86, 2.7700, 25.82]
    
    #Printing the top 5 stock recommendations
    print("Top 5 Stock Recommendations: ")
    if len(stocks) == len(prices):
        for i in range(len(stocks)):
            print("#",i+1, stocks[i], "is a good investment at $", prices[i], "per share.")
    
    #ERROR HANDLING: If stock recommendations are not available, it will print error message
    else:
        print("No Stock recommendations are available at the moment.")


def main():

    #The program will run until the user chooses to exit, keeps looping
    while True:
       
       #Printing the title of the program
        print("=" * 80)
        print("STOCK MARKET ANALYSER")
        print("=" * 80)

        #Displaying the menu of options for the user to choose from
        print("Services: ")
        print("1. Search Stocks")
        print("2. Get Stock Quote")
        print("3. Get Stock History (Last 100 Days)")
        print("4. Evaluate a stock (display recent stock data and also evaluate)")
        print("5. Convert currency")
        print("6. Top 5 stock recommendations")
        print("7. Exit")

        #Taking input from the user for the required function
        user_choice = input("Choose an option: ")
        
        #Using if-elif conditional statements to perform the action based on the user's user_choice
        if user_choice == '1':
            #Display purposes
            print("-" * 80)

            #Taking input from the user for the stock symbol
            symbol = input("Enter a symbol or keywords to search for stocks: ")

            #Calling the Search_Stocks function to search for stocks
            stocks = Search_Stocks(symbol)

            #Calling the Display_Stocks function to display stocks
            Display_Stocks(stocks)


        elif user_choice == '2':
            #Display purposes
            print("-" * 80)

            #Taking input from the user for the stock symbol
            symbol = input("Enter a stock symbol to get quote: ")

            #Calling the Get_Stock_Quote function to get the stock quote
            stock_quote = Get_Stock_Quote(symbol)

            if stock_quote:

                #Printing the Title
                print("STOCK QUOTE: ")

                #Iterating through the dictionary and displaying the stock quote
                for key, value in stock_quote.items():
                    print(key + ":", value)

            #ERROR HANDLING: If stock quote is not found, it will print error message
            else:
                print("Failed to retrieve stock quote for", symbol + ".")


        elif user_choice == '3':
            #Display purposes
            print("-" * 80)

            #Taking input from the user for the stock symbol
            symbol = input("Enter a stock symbol to get history: ")

            #Calling the Get_Stock_History function to get the stock history
            stock_history = Get_Stock_History(symbol)

            #Calling the Display_Stock_History function to display the stock history
            Display_Stock_History(stock_history)


        elif user_choice == '4':
            #Display purposes
            print("-" * 80)

            #Taking input from the user for the stock symbol
            symbol = input("Enter stock symbol: ")

            #Calling the Evaluate_Stock function to evaluate the stock
            result = Evaluate_Stock(symbol)
            print(result)



        elif user_choice == '5':
            #Display purposes
            print("-" * 80)

            #Taking input from the user for the amount, from currency and to currency
            amount = float(input("Enter amount: "))

            #Converting the values of the currencies to UPPERCASE to match the format of the data avaliable through the ExchangeRate API
            from_currency = input("From currency (e.g., USD): ").upper()
            to_currency = input("To currency (e.g., EUR): ").upper()

            #Calling the Currency_Conversion function to convert the currency
            converted_amount = Currency_Conversion(amount, from_currency, to_currency)

            #Printing the converted amount with a decimal precision of 2 places
            print(amount, from_currency, "=", round(converted_amount, 2), to_currency)


        elif user_choice == '6':
            #Display purposes
            print("-" * 80)
            Recommend_Stocks()

        elif user_choice == '7':
            #Display purposes
            print("-" * 80)
            print("Thank you for using the Stock Market Analyser.")
            break

        #Handles the case when the user enters an incorrect choice which is not there in the menu
        else:
            print("This choice is invalid. Please try again.")

if __name__ == "__main__":
    main()
