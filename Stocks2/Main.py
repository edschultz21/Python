from Stocks import StockData, Stock
from Portfolio import Portfolio
from datetime import date, timedelta
from yahoo_fin import stock_info

def creatPortfolio():
    stocks = []
    stocks.append(Stock('MOMO', date(2018, 6, 4), 50.37, 100, 'Ellie Roth'))
    stocks.append(Stock('QQQ', date(2020, 6, 5), 240.14, 150, 'Ellie Roth'))
    stocks.append(Stock('QQQ', date(2020, 6, 5), 240.08, 170, 'Ed Roth'))
    stocks.append(Stock('AMZN', date(2020, 10, 7), 3135.00, 66, 'Ellie Stock'))
    stocks.append(Stock('QQQ', date(2020, 10, 7), 277.89, 40, 'Ellie IRA'))
    stocks.append(Stock('QQQ', date(2020, 10, 7), 277.89, 200, '401K'))
    stocks.append(Stock('QQQ', date(2020, 10, 7), 277.89, 265, 'Ed IRA'))
    stocks.append(Stock('ARKK', date(2020, 10, 7), 97.10, 350, 'Ed Stock'))
    stocks.append(Stock('SPY', date(2020, 11, 16), 361.10, 550, 'Chase'))
    stocks.append(Stock('XLY', date(2020, 11, 16), 155.00, 1250, 'Chase'))
    return Portfolio('Dads', stocks)

portfolio = creatPortfolio()
portfolio.updatePrices()
print(portfolio)


