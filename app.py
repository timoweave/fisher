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


fetch_and_plot_stock("AAPL", "1mo")
fetch_and_plot_stock("NVDA", "1mo")
