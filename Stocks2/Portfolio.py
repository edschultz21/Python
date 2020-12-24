from Stocks import StockData
from prettytable import PrettyTable

class Portfolio():
    def __init__(self, owner, stocks) -> None:
        self.owner = owner
        self.stocks = stocks
        self.tickers = {stock.ticker for stock in stocks}
        super().__init__()

    def __str__(self) -> str:
        result = []
        result.append(f'{self.owner} Portfolio')
        for stock in self.stocks:
            result.append(str(stock))
        return '\n'.join(result)

    def calculateChange(self, currentPrice, priceAtStart, amount):
        change = currentPrice - priceAtStart 
        gain = change * amount
        percentGain = change / priceAtStart * 100
        return gain, percentGain

    def updatePrices(self):
        stockData = StockData()
        currentPrices = stockData.getCurrentPrices(self.tickers)
        closingPrices = stockData.getPreviousClosingPrices(self.tickers)

        table = PrettyTable()
        table.field_names = ['Ticker', 'Current', 'Cost', 'Amount', 'Gain', '% Day', '% Total']
        totalDayGain = 0
        totalOverallGain = 0
        for stock in self.stocks:
            currentPrice = currentPrices[stock.ticker]
            closingPrice = closingPrices[stock.ticker]
            buyPrice = stock.buyPrice

            dayGain, dayGainPercent = self.calculateChange(currentPrice, closingPrice, stock.amount)
            totalGain, totalGainPercent = self.calculateChange(currentPrice, buyPrice, stock.amount)
            table.add_row([stock.ticker, currentPrice, buyPrice, stock.amount, dayGain, dayGainPercent, totalGainPercent])

            totalDayGain += dayGain
            totalOverallGain += totalGain
        print(f'Day Gain:   {totalDayGain:>7,.0f}')
        print(f'Total Gain: {totalOverallGain:>7,.0f}')
        print()
        table.align = 'r'
        table.align['Ticker'] = 'l'
        table.float_format = '.2'
        table.float_format['Gain'] = '.'
        print(table)