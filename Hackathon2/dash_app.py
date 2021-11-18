import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import dash
from dash import Input, Output

# app.layout = Div([
#     H3("Stock Tickers"),
    
#     user_input(
#         id = "user_input"),
#     graph (id= "my_graph")
#     ])

# Input(
#     user_input = "Enter a publicly traded stock",
#     value = ""
# )

# @app.react("my_graph", "user_input")
# def update_graph(user_input):
#     selected_value = user_input

#     df = web.DataReader(
#         user_input, "yahoo",
#         dt(2021, 1, 1), dt.now()
#     )

#     return {
#         "figure": go.figure(
#             data = [
#                 Scatter(
#                     x= df.index,
#                     y = df.Close,
#                     name = selected_value
#                 )
#             ]
#         )
#     }


user_input= input("List any publicly traded company")
df= yf.download(user_input)
print(df.head())
# comp_info = yf.Ticker(user_input)
# print(type(df))
# name = input("Full name of Stock")
# # get historical market data
# hist = comp_info.history(period="max")
# print(hist)
# # show actions (dividends, splits)
# print(comp_info.actions)


# # show dividends
# print(comp_info.dividends)

# # show splits
# comp_info.splits

# # show financials
# print(comp_info.financials)
# print(comp_info.quarterly_financials)

# # show major holders
# print(comp_info.major_holders)

# # show institutional holders
# comp_info.institutional_holders

# # show balance sheet
# print(comp_info.balance_sheet)
# print(comp_info.quarterly_balance_sheet)

# # show cashflow
# print(comp_info.cashflow)
# print(comp_info.quarterly_cashflow)

# # show earnings
# print(comp_info.earnings)
# print(comp_info.quarterly_earnings)

# # show sustainability
# comp_info.sustainability

# # show analysts recommendations
# comp_info.recommendations

# # show next event (earnings, etc)
# comp_info.calendar

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# print(comp_info.isin)

# # show options expirations
# print(comp_info.options)


# df = px.data.stocks()
# fig = px.line(df, x='date', y= user_input)
# fig.show()

# # df = px.data.stocks()
# # fig = px.line(df, x='date', y= f"{user_input}High")
# # fig.show()


# # df = pd.read_csv(f'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-{name}.csv')
# # fig = go.Figure([go.Scatter(x=df['Date'], y=df[f'{user_input}.High'])])
# # fig.show()

# # show news
# # comp_info.news

# # get stock info
# # print(comp_info.info)