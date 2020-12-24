#http://theautomatic.net/yahoo_fin-documentation/#get_analysts_info
from yahoo_fin import stock_info
from datetime import date 
from datetime import timedelta 
import pandas as pd

class Stock():
    currentPrice = 0.0
    closingPrice = 0.0

    def __init__(self, ticker, buyDate, buyPrice, amount, account) -> None:
        self.ticker = ticker
        self.buyDate = buyDate
        self.buyPrice = buyPrice
        self.amount = amount
        self.account = account
        super().__init__()

    def __str__(self) -> str:
        return f'{self.ticker:<4}  {self.buyDate}  {self.buyPrice:>7.2f}  {self.amount:>4}, Cur: {self.currentPrice:>7.2f}, Close: {self.closingPrice:>7.2f}'

    @property
    def dayGain(self):
        change = self.currentPrice - self.closingPrice
        return change * self.amount

    @property
    def dayGainPercent(self):
        change = self.currentPrice - self.closingPrice
        return change / self.closingPrice * 100

    @property
    def totalGain(self):
        change = self.currentPrice - self.buyPrice
        return change * self.amount

    @property
    def totalGainPercent(self):
        change = self.currentPrice - self.buyPrice
        return change / self.buyPrice * 100

class StockData():
    def getCurrentPrice(self, ticker):
        if ticker == 'AMZN': return 3210.0
        if ticker == 'ARKK': return 134.88
        if ticker == 'MOMO': return 13.72
        if ticker == 'QQQ': return 310.31
        if ticker == 'SPY': return 368.35
        if ticker == 'XLY': return 157.89
        # return (ticker, stock_info.get_live_price(ticker))

    def getCurrentPrices(self, tickers):
        prices = {}
        for ticker in tickers:
            prices[ticker] = self.getCurrentPrice(ticker)
        return prices

    def getPreviousClosingPrice(self, ticker):
        if ticker == 'AMZN': return 3210.0 + 10
        if ticker == 'ARKK': return 134.88 + 10
        if ticker == 'MOMO': return 13.72 + 10
        if ticker == 'QQQ': return 310.31 + 10
        if ticker == 'SPY': return 368.35 + 10
        if ticker == 'XLY': return 157.89 + 10
        # startDay = date.today() - timedelta(days = 7) 
        # endDay = date.today() 
        # data = stock_info.get_data(ticker, startDay, endDay, False)
        # rowData = data[data['date'] == data['date'].max()]
        # return (ticker, rowData.iloc[0]['close'])

    def getPreviousClosingPrices(self, tickers):
        prices = {}
        for ticker in tickers:
            prices[ticker] = self.getPreviousClosingPrice(ticker)
        return prices
        # return (ticker, stock_info.get_live_price(ticker))

    def displayAll(self, tickers):
        prices = self.getCurrentPrices(*tickers)
        for item in prices.items():
            print(f'{item[0]:<5} {item[1]:>7.2f}')

