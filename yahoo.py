import platform
import datetime
print('Python version = '+platform.python_version())
import yfinance as yf
print('yfinance version ='+yf.__version__)


def yfinancetut(tickersymbol):
	tickerdata=yf.Ticker(tickersymbol)
	tickerinfo=tickerdata.info
	investment=tickerinfo['shortName']
	print(investment)
	today=datetime.datetime.today().isoformat()
	
	


	tickerDF=tickerdata.history(period='1d',start='2021-6-1',end=today[:10])
	priceLast=tickerDF['Close'].iloc[-1]
	priceYest=tickerDF['Close'].iloc[-2]
	change=priceLast-priceYest
	print(investment+ 'price last='+str(priceLast))
	print('Price change='+ str(change))
	print(tickerDF)


yfinancetut('TSLA')
print('-------')
yfinancetut('NIO')





	
