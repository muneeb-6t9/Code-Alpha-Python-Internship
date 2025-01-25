#Stock Protfolio

#Requirements
## yfinanca library to fetch real time stock data
## Pretty table to display data in a good way
# Function to add stock in protfolio add_stock()
# Function to remove existing stock remove_stock()
# A function to display protfolio display_protfolio()
# A function to get real time data get_real_time_price()
# menu for user interface 

import yfinance as yf
from prettytable import PrettyTable

protfolio = []


#function to add stock
def add_stock(symbol,quantity,purchase_price):
    stock={
        'symbol':symbol.upper(),
        'quantity':quantity,
        'purchase_price':purchase_price,
    }
    protfolio.append(stock)
    print(f"Added {quantity} shares of {symbol.upper()} at ${purchase_price :.2f} per share. ")


#function to remove stock
def remove_stock(symbol):
    global protfolio
    protfolio = [stock for stock in protfolio if stock['symbol'] != symbol.upper()]
    print(f"Succefully Removed {symbol.upper()} from the protfolio")

# function to fetch real time data
def get_real_time_price(symbol):
    try:
        stock_data = yf.Ticker(symbol)
        return stock_data.history(period="1d")['Close'][0]
    except Exception as e:
        print(f" Error fetching data for{symbol}: {e}")
        return None

#funtion to dusplay protfolio
def display_protfolio():
    table = PrettyTable()
    table.field_names = ["Symbol", "Quantity" , "Purchase Price" , "Current Price" , "Value" , "Profit/Loss"]

    total_value=0
    total_cost=0

    for stock in protfolio:
        symbol = stock["symbol"]
        quantity = stock["quantity"]
        purchase_price = stock["purchase_price"]
        current_price = get_real_time_price(symbol)

        if current_price:
            value = quantity * current_price
            profit_loss = value - ( quantity * purchase_price)
            total_value += value
            total_cost+= quantity * purchase_price  

            table.add_row([
                symbol,
                quantity,
                f"${purchase_price:.2f}",
                f"${current_price:.2f}",
                f"${value:.2f}",
                f"${profit_loss:.2f}"
            ])
        else:
            table.add_row([symbol,quantity,f"${purchase_price:.2f}", "N/A" , "N/A" , "N/A"])

        print(table)
        print(f"Total Protfolio Value $ {total_value:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Profit/Loss : ${total_value-total_cost:.2f}")


#Menu for user interface
def menu():
    while True:
        print("\n Strock protfolio Tracker")
        print("1 . to add stock")
        print("2 . to remove stock")
        print("3 . to display Protfolio")
        print("4 . to Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            symbol=input("Enter Stock Symbol :  ")
            quantity= float(input("Enter stock quantity : "))
            purchase_price= float(input("Enter purchase price : "))
            add_stock(symbol,quantity,purchase_price)

        elif choice=="2":
            symbol = input("Enter symbol of stock you want to remove : ")
            remove_stock(symbol)

        elif choice=="3":
            display_protfolio()      

        elif choice=="4":
            print("Exiting......") 
            break
        else:
            print("Invalid choice. Please Try Again")     

#Run the menu
if __name__ == "__main__":
    menu()