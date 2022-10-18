# import module for Yahoo Finance (data source) and matplotlib (chart plotter)
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# disable warnings (you do not need to study this block)
import warnings
warnings.filterwarnings("ignore")

# user input asset to enquire
asset = input("Please input asset: ")

# download data from Yahoo
print("Connecting to Yahoo, please wait...")
# get latest 60 rows only
data = yf.download(asset)[-60:]
# calculate daily price change
data['Change'] = data.Close.pct_change().apply(lambda x: f'{x * 100:.2f}%')
# display latest 15 rows in console
print(f'\n{asset:-^120}')
print(data[-15:])
print('-'*120 + '\n\n')

# codes to draw the price chart
fig, dt = plt.subplots()
dt.set_xlabel('Date') 
dt.set_ylabel('Price(USD)') 
dt.set_title(f'{asset} 60D PRICE CHART', fontsize = 14, fontweight ='bold') 
dt.xaxis.set_major_locator(mdates.DayLocator(interval=5))   
dt.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
dt.xaxis.set_minor_locator(mdates.DayLocator())
dt.plot(data.index,data.loc[:,['Close']],color='C1')
fig.autofmt_xdate()
# save chart as a pdf to current folder
fig.savefig(f'{asset}.jpg')

print('{:-^120}'.format('END OF DATA'))
print("Press enter to exit...")
input()