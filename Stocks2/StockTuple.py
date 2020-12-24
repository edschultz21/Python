class StockInfo_tuple():
    def getPrice(self, ticker):
        if ticker == 'AMZN': return (ticker, 3200.1234)
        if ticker == 'ARKK': return (ticker, 123.2849)
        if ticker == 'MOMO': return (ticker, 13.5678)
        if ticker == 'QQQ': return (ticker, 320.98)
        if ticker == 'SPY': return (ticker, 325.398)
        if ticker == 'XLY': return (ticker, 158.2349)
        # return (ticker, stock_info.get_live_price(ticker))

    def getPrices(self, *tickers):
        prices = []
        for ticker in tickers:
            prices.append(self.getPrice(ticker))
        return prices

    def displayAll(self, *tickers):
        prices = self.getPrices(*tickers)
        for price in prices:
            print(f'{price[0]:<5} {price[1]:>7.2f}')