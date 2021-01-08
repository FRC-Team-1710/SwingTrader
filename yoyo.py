import quandl

quandl.ApiConfig.api_key = "Ns3nA6dQioYiAy5owmfR"

### this line below gives us price data for the company apple
###                     dont touch                                             company ticker               date range from: 
data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['close'] }, ticker = ['AAPL'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
i = 0;

#while(i <= len(data)-1):
#    print(data.iloc[i][0])
#    i += 1

def getRSI(start, end):
    gains = []
    losses = []
    avgLoss = 0.0
    avgGain = 0.0
    print(end-start);
    x = start

    #Get gains and losses from each previous day
    while(x<=end):
        c = data.iloc[x][0]-data.iloc[x-1][0]
        if(c<0):
            losses.append(c*-1)
            gains.append(0)
        else:
            losses.append(0)
            gains.append(c)
        x+=1
    
    #Get averages
    for i in range(0,end-start):
        avgLoss+=losses[i]
        avgGain+=gains[i]

    avgLoss = avgLoss/(end-start)
    avgGain = avgGain/(end-start)
    print(avgLoss)
    print(avgGain)

    #Calculate & return RSI
    RSI = 100-(100/(1+avgGain/avgLoss))
    return RSI

print(getRSI(1,100))
