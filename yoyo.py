import quandl

quandl.ApiConfig.api_key = "Ns3nA6dQioYiAy5owmfR"

### this line below gives us price data for the company apple
###                     dont touch                                             company ticker               date range from: 
data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['close'] }, ticker = ['AAPL'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
i = 0;

#List daily prices throughout 2016
#while(i <= len(data)-1):
#    print(data.iloc[i][0])
#    i += 1

def printRSI(start, end):
    gains = []
    losses = []
    x = start - 14

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
    
    #Calculate Daily RSI
    for i in range(start,end+1):
        #Get averages
        avgLoss = 0.0
        avgGain = 0.0
        for j in range(i-14,i):
            avgGain+=gains[j]
            avgLoss+=losses[j]
        avgGain /= 14
        avgLoss /= 14

        #Calculate & print RSI
        RSI = 100-(100/(1+avgGain/avgLoss))
        print("Day" + str(i) + ": " + str(RSI))
        
printRSI(15,28)
