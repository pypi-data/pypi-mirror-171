# Fin Crawler


## Features
- Fetch Finalcial data like stock price or future price etc.

## Current Support List
- Taiwan stock price (daily stock price for all stocks)
- Taiwan stock price (monthly stock price for specific stock)

## Example

### Supported List
```
>>> from fin_crawler import FinCrawler
>>> FinCrawler.crawler_list
['tw_stock_price_daily',
 'tw_stock_price',
 'tw_institutional_investors_daily',
 'tw_stock_info']
```

### Get Crawler Params Example
For each crawler you should pass in params and this will get you example of params
```
>>> params_example = FinCrawler.params_example('tw_stock_price_all')
爬取其中一天全部股票的價格
ex:{'date': '20220920'}
>>> params_example
{'date': '20220920'}
```

### Get Data Example
```
# get stock data
>>> stock_price = FinCrawler.get('tw_stock_price_all',{'date':'20220920'})
# check stock data keys
>>> stock_price.keys()
dict_keys(['stock_id', 'stock_name', 'vol', 'trade_num', 'trade_amount', 'open', 'close', 'high', 'low', 'spread', 'date'])
# get first stock id
>>> stock_price['stock_id'][0]
'0050'
# get first stock name
>>> stock_price['stock_name'][0]
'元大台灣50'
# get first stock open price
>>> stock_price['open'][0]
112.55
# get first stock close price
>>> stock_price['close'][0]
113.05
```