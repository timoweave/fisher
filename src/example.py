import matplotlib.pyplot as plt
import yfinance as yf


def fetch_and_plot_stock(ticker, period="1y"):
    # Fetch stock data
    stock = yf.Ticker(ticker)
    hist = stock.history(period)

    # Plot the closing prices
    plt.plot(hist.index, hist["Close"], label="Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.title(f"{ticker} Stock Price Over the Last Year")
    plt.legend()
    plt.grid(True)
    plt.show()


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
