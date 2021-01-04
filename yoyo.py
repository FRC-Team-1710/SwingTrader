import quandl

quandl.ApiConfig.api_key = "Ns3nA6dQioYiAy5owmfR"

### this line below gives us price data for the company apple
###                     dont touch                                             company ticker               date range from: 
data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['close'] }, ticker = ['AAPL'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })

i = 1
N = 7
closeRow = 0
close1 = 0.0
close2 = 0.0
Up = 0.0
Down = 0.0
sevenPlus = 0
avgUp = 0.0
avgDown = 0.0
RS = 0.0
RSI = 0.0

#ii = 0
#while(ii < len(data)):
#    print(data.iloc[i][0])
#    i += 1

#print(len(data))

while(i <= (len(data))/7):
    for closeRow in range(sevenPlus, sevenPlus+N):
        close1 = data.iloc[closeRow][0]
        close2 = data.iloc[closeRow + 1][0]
        if close2 > close1:
            Up += 1
        elif close2 < close1:
            Down += 1
    avgUp = Up/N
    avgDown = Down/N
    RS = avgUp/avgDown
    RSI = 100 - (100/(1+RS))
    Up = 0.0
    Down = 0.0
    sevenPlus += 7
    if i == 35:
        N = 6
    print('RSI for the ' + str(i) + 'st/nd/rd/th seven day period is ' + str(RSI))
    i += 1