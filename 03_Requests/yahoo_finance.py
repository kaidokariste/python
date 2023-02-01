import yfinance as yf

gspc = yf.Ticker('^GSPC')
print(gspc.fast_info)
previous_close = round(gspc.fast_info['previous_close'],2)
current_price = round(gspc.fast_info['last_price'],2)
fifty_two_week_low = round(gspc.fast_info['year_low'],2)
change_in_points = round(current_price - previous_close, 2)
change_in_percentages = round(round(current_price - previous_close, 2) / previous_close * 100, 2)

message = '*Nasdaq*\n`Yahoo finance`\nCurrent price: {}\nPrevious close: {}\nChange: {} pts, {}%\n52W Low: {}'.format(
    current_price, previous_close, change_in_points, change_in_percentages, fifty_two_week_low)

print(current_price)
print(previous_close)
print(fifty_two_week_low)
print(change_in_points)
print(message)