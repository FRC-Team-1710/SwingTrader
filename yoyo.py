import quandl

quandl.ApiConfig.api_key = "Ns3nA6dQioYiAy5owmfR"

### this line below gives us price data for the company apple
###                     dont touch                                             company ticker               date range from: 
data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['close'] }, ticker = ['AAPL'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
i = 0;

while(i <= len(data)-1):
    print(data.iloc[i][0])
    i += 1
