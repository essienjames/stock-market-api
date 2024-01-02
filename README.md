# Stock Market Data Retrival Project

This is a Python based project that interacts with the Alpha Vantage API to retrieve and display stock market data.
It enables you to search for a stock name and retrieve ticker symbol, current stock values and other information.
The script uses the `requests` library for making API calls and the `tabulate` library for formatting and displaying tabular data.

## Prerequisites
- Python 3.0
- `requests` library
```shell
pip install requests
```
- `tabulate` library
```shell
pip install tabulate
```
- `pwunput` library
```shell
pip install pwinput
```
- An API key from Alpha Vantage. You can sign up for a free API key on their [website](https://www.alphavantage.co/support/#api-key).

## Getting Started
1. Clone this repository to your local machine
    ```shell
    git clone https://github.com/yourusername/StockMarketAPI.git
    ```
2. Navigate to the clones directory
    ```shell
    cd StockMarketAPI
    ``` 
## Usage
1. Open a terminal and navigate to the directory where you cloned the repository.
2. Run the script using Python:
    ```shell
    python main.py
    ```
3. The script will prompt you for your Alpha Vantage API key, which you can obtain from their website.
4. Enter the name of the country you want to search for. Valid options include: United States, Canada, United Kingdom, Germany, France, Spain, Portugal, Japan, India, Mainland China, Hong Kong, Brazil, Mexico, South Africa.
5. The script will display the current market status for the selected country.
6. You can then search for a stock ticker symbol by entering the company name. The script will display a table of matching symbols and names.
7. After selecting a stock symbol from the table, the script will retrieve and display detailed information about that stock.