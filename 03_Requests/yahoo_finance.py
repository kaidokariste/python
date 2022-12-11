import yfinance as yf

gspc = yf.Ticker('^IXIC')
previous_close = gspc.info['previousClose']
current_price = gspc.info['regularMarketPrice']
fifty_two_week_low = gspc.info['fiftyTwoWeekLow']
change_in_points = round(gspc.info['regularMarketPrice'] - gspc.info['previousClose'], 2)
change_in_percentages = round(round(gspc.info['regularMarketPrice'] - gspc.info['previousClose'], 2) / gspc.info['previousClose'] * 100, 2)

message = '*Nasdaq*\n`Yahoo finance`\nCurrent price: {}\nPrevious close: {}\nChange: {} pts, {}%\n52W Low: {}'.format(
    current_price, previous_close, change_in_points, change_in_percentages, fifty_two_week_low)
print(message)