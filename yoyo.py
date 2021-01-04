import quandl

quandl.ApiConfig.api_key = "Ns3nA6dQioYiAy5owmfR"

### this line below gives us price data for the company apple
###                     dont touch                                             company ticker               date range from: 
data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['close'] }, ticker = ['AAPL'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })

#Varible initialization
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

while(i <= (len(data))/7): #Divides the 252 array elements by seven to make the loop iterate 36 times.

    for closeRow in range(sevenPlus, sevenPlus+N): #Iterates through 7 rows to get the sum of the ups and downs
        close1 = data.iloc[closeRow][0] #Gets the value of the current rows price
        close2 = data.iloc[closeRow + 1][0] #Gets the value of the next rows price
        if close2 > close1: #If the price increased, then varible Up goes up by 1
            Up += 1
        elif close2 < close1: #If the price decreased, then varible Down goes up by 1
            Down += 1

    avgUp = Up/N
    avgDown = Down/N #Gets the average of the ups & downs
    RS = avgUp/avgDown #Finds the Relative Strength
    RSI = 100 - (100/(1+RS)) #Final RSI calculation
    Up = 0.0
    Down = 0.0 #Resets the varibles so they don't carry over their value to the next iteration
    sevenPlus += 7 #Adds 7 so the next 7 rows are calculated

    if i == 35: #Due to arrays ending at one less than their length,
        N = 6   #the last iteration will result in an error since row 252 does not exist. This makes it stop at 251

    print('RSI for the ' + str(i) + 'st/nd/rd/th seven day period is ' + str(RSI)) #Prints the RSI
    i += 1 #Increases so the loop can iterate