name = "hyjt"
stock_price = 6.66
stock_code = 728467  #数字不能以0开头；  "002546"  
stock_price_daily_growth_factor = 1.3
growth_days = 9

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}, 股票代码{stock_code} ,当前股价{stock_price}")

print("每日的增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
print("每日的增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,finally_stock_price))