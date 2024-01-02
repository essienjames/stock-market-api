# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import sys
from tabulate import tabulate
from pwinput import pwinput


def main():
    api_value = api_key()

    # Request Country Name as input, remove all trailing white space and auto capitalise
    print("\nEnter Country Name:")
    country_name = input("Country: ").strip().title()

    # Check for validity of Country Name input
    valid_country_bool = valid_country_name(country_name)

    # If an invalid Country Name is provided, print error message to console and exit the program
    if not valid_country_bool:
        sys.exit("Invalid Country Name")

    # If a valid Country Name is provided, print Market data to console
    status = market_status(country_name)
    print(f"\nMarket is {status.title()}\n")

    # Request a Stock Ticker Symbol, remove all trailing white space and auto capitalise
    print("Search Stock Ticker Symbol: ")
    company_name = input("Search: ").strip().title()

    stock_search(company_name, country_name, api_value)

    display_result(api_value)


# COUNTRY NAME VALIDATOR FUNCTION
def valid_country_name(country_name):
    valid_countries = [
        "United States",
        "Canada",
        "United Kingdom",
        "Germany",
        "France",
        "Spain",
        "Portugal",
        "Japan",
        "India",
        "Mainland China",
        "Hong Kong",
        "Brazil",
        "Mexico",
        "South Africa",
    ]

    return country_name in valid_countries


# MARKET STATUS FUNCTION
def market_status(country_name):
    response = requests.get(
        "https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo"
    )
    data = response.json()

    # Check the market is open in the country provided by validating data in the "markets" entity
    for market in data["markets"]:
        if market["region"] == country_name:
            if market["current_status"] == "open":
                return market["current_status"]

            else:
                return market["current_status"]
        else:
            continue


# EXTRACT AND AGGREGATE RELEVANT REGION BASED DATA
def stock_search(ticker, country_name, api_value):
    try:
        response = requests.get(
            f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={api_value}"
        )
        data = response.json()

        # Extract all entries inside the "bestMatches" entity
        best_matches_data = data["bestMatches"]

        # Filter all entries based on the region provided
        filtered_entries = [
            entry for entry in best_matches_data if entry["4. region"] == country_name
        ]

        # Convert each filtered entry into a list of key-value pairs
        table_data = [
            [f"{entry['1. symbol']}: {entry['2. name']}", entry["8. currency"]]
            for entry in filtered_entries
        ]

        # Print the data in tabular format
        table_headers = ["Symbol and Name", "Currency"]
        table = tabulate(table_data, headers=table_headers, tablefmt="rounded_grid")

        # Print the formatted table
        print(table)

    except KeyError:
        sys.exit("Try Again with API KEY")


def api_key():
    print("\nRequests Limit ==> up to 5 API requests per minute and 100 requests per day")

    api_key_value = pwinput(prompt="API Key: ", mask="E18EWE37QMPRLZCN")

    return api_key_value


#
def display_result(api_value):
    stock_name = input("\nTICKER: ")
    try:
        response = requests.get(
            f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_value}"
        )
        data = response.json()

        # Extract the inner dictionary under "Global Quote"
        quote_data = data["Global Quote"]

        # Convert the inner dictionary into a list of key-value pairs
        table_data = [[key, value] for key, value in quote_data.items()]

        # Print the data in tabular format
        table_headers = ["Field", "Value"]
        table = tabulate(table_data, headers=table_headers, tablefmt="rounded_grid")

        # Print the formatted table
        print(table)

    except KeyError:
        sys.exit("Try again with API KEY")

    if __name__ == "__main__":
        main()
