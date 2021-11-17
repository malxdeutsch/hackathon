import yfinance as yf

user_input= input("List any publicly traded company")

comp_info = yf.Ticker(user_input)

print(comp_info.info)


# get stock info
comp_info.info

# get historical market data
hist = comp_info.history(period="max")

# show actions (dividends, splits)
comp_info.actions

# show dividends
comp_info.dividends

# show splits
comp_info.splits

# show financials
comp_info.financials
comp_info.quarterly_financials

# show major holders
comp_info.major_holders

# show institutional holders
comp_info.institutional_holders

# show balance sheet
comp_info.balance_sheet
comp_info.quarterly_balance_sheet

# show cashflow
comp_info.cashflow
comp_info.quarterly_cashflow

# show earnings
comp_info.earnings
comp_info.quarterly_earnings

# show sustainability
comp_info.sustainability

# show analysts recommendations
comp_info.recommendations

# show next event (earnings, etc)
comp_info.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
comp_info.isin

# show options expirations
comp_info.options

# show news
comp_info.news

# get option chain for specific expiration
opt = comp_info.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
