from Stocks import StockData
from prettytable import PrettyTable

class Portfolio():
    totalDayGain = 0
    totalGain = 0

    def __init__(self, owner, stocks) -> None:
        self.owner = owner
        self.stocks = stocks
        self.tickers = {stock.ticker for stock in stocks}
        self.createTable()
        super().__init__()

    def __str__(self) -> str:
        result = []
        result.append(f'{self.owner} Portfolio')
        result.append(self.display())
        return '\n'.join(result)

    def createTable(self):
        table = PrettyTable()
        table.field_names = ['Ticker', 'Current', 'Cost', 'Amount', 'Day Gain', '% Day', 'Total Gain', '% Total']
        table.align = 'r'
        table.align['Ticker'] = 'l'
        table.float_format = '.2'
        table.float_format['Gain'] = '.'
        self.prettyTable = table

    def updatePrices(self):
        stockData = StockData()
        currentPrices = stockData.getCurrentPrices(self.tickers)
        closingPrices = stockData.getPreviousClosingPrices(self.tickers)
        for stock in self.stocks:
            stock.currentPrice = currentPrices[stock.ticker]
            stock.closingPrice = closingPrices[stock.ticker]
            self.totalDayGain += stock.dayGain
            self.totalGain += stock.totalGain

    def display(self):
        self.prettyTable.clear_rows()
        for stock in self.stocks:
            self.prettyTable.add_row([stock.ticker, stock.currentPrice, stock.buyPrice, stock.amount, stock.dayGain, stock.dayGainPercent, stock.totalGain, stock.totalGainPercent])

        result = []
        result.append(self.prettyTable.get_string())
        result.append('')
        result.append(f'Day Gain:   {self.totalDayGain:>7,.0f}')
        result.append(f'Total Gain: {self.totalGain:>7,.0f}')
        return '\n'.join(result)        
